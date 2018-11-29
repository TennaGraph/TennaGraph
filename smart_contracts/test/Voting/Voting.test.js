require('babel-register');
require('babel-polyfill');

import ether from 'zeppelin-solidity/test/helpers/ether';
import {advanceBlock} from 'zeppelin-solidity/test/helpers/advanceToBlock';
import {increaseTimeTo, duration} from 'zeppelin-solidity/test/helpers/increaseTime';
import latestTime from 'zeppelin-solidity/test/helpers/latestTime';
import EVMRevert from 'zeppelin-solidity/test/helpers/EVMRevert';


const BigNumber = web3.BigNumber;

require('chai')
  .use(require('chai-as-promised'))
  .use(require('chai-bignumber')(BigNumber))
  .should();

const Voting = artifacts.require('Voting');

contract('VotingContract', function ([owner, wallet, investor]) {
    const RATE = new BigNumber(2);
    const TOTAL_SUPPLY = new BigNumber(1000000e18);
    const TOKENS_HOLDER_ADDRESS = owner;
    const TOKEN_NAME = "ICONX - Crowdsale token";
    const TOKEN_SYMBOL = "ICNX";
    const CAP = new BigNumber(100000e18);

    before(async function () {
        // Advance to the next block to correctly read time in the solidity "now" function interpreted by testrpc
        await advanceBlock();
    });

    beforeEach(async function () {
        // Token
        this.token = await CrowdsaleTokenContract.new(TOTAL_SUPPLY, TOKENS_HOLDER_ADDRESS, TOKEN_NAME, TOKEN_SYMBOL);

        // Bank
        this.startDepositDate = latestTime() + duration.weeks(1);
        this.startWithdrawDate = latestTime() + duration.weeks(4);
        this.bank = await IconxTokensBank.new(this.startDepositDate, this.startWithdrawDate, TOKENS_HOLDER_ADDRESS,
            this.token.address);

        // Crowdsale
        this.startTime = this.startDepositDate;
        this.endTime = this.startTime + duration.weeks(1);
        this.crowdsale = await CrowdsaleContract.new(this.startTime, this.endTime, RATE, CAP, wallet,
            this.token.address, this.bank.address);

        // Settings
        await this.token.approve(this.bank.address, TOTAL_SUPPLY, { from: owner }).should.be.fulfilled;
    });

    it('should create token with correct parameters', async function () {
        this.token.should.exist;

        const totalSupply = await this.token.totalSupply();
        const tokenName = await this.token.name();
        const tokenSymbol = await this.token.symbol();
        const allowance = await this.token.allowance(owner, this.bank.address);

        tokenName.should.be.equal(TOKEN_NAME);
        tokenSymbol.should.be.equal(TOKEN_SYMBOL);
        totalSupply.should.be.bignumber.equal(TOTAL_SUPPLY);
        allowance.should.be.bignumber.equal(TOTAL_SUPPLY)
    });

    it('should create crowdsale with correct parameters', async function () {
        this.crowdsale.should.exist;

        const startTime = await this.crowdsale.openingTime();
        const endTime = await this.crowdsale.closingTime();
        const rate = await this.crowdsale.rate();
        const walletAddress = await this.crowdsale.wallet();

        startTime.should.be.bignumber.equal(this.startTime);
        endTime.should.be.bignumber.equal(this.endTime);
        rate.should.be.bignumber.equal(RATE);
        walletAddress.should.be.equal(wallet);
    });

    it('should not accept payments before start', async function () {
        await this.crowdsale.send(ether(1)).should.be.rejectedWith(EVMRevert);
        await this.crowdsale.buyTokens(investor, { from: investor, value: ether(1) }).should.be.rejectedWith(EVMRevert);
    });

    it('should not accept payments during the sale if crowdsale doesnt have BANK_MANAGER role in bank', async function () {
        const investmentAmount = ether(1);
        await increaseTimeTo(this.startTime);
        await this.crowdsale.buyTokens(investor, { value: investmentAmount, from: investor }).should.be.rejectedWith(EVMRevert);
    });

    it('should accept payments during the sale', async function () {
        const investmentAmount = ether(1);
        const expectedTokenAmount = RATE.mul(investmentAmount);
        await increaseTimeTo(this.startTime);
        await addRole(this.bank, this.crowdsale.address, ROLE_BANK_MANAGER);
        await this.crowdsale.buyTokens(investor, { value: investmentAmount, from: investor }).should.be.fulfilled;

        (await this.token.balanceOf(investor)).should.be.bignumber.equal(0);
        (await this.bank.balanceOf(investor)).should.be.bignumber.equal(expectedTokenAmount);
        (await this.token.totalSupply()).should.be.bignumber.equal(TOTAL_SUPPLY);
    });

    it('should reject payments after end', async function () {
        await increaseTimeTo(this.afterEnd);
        await addRole(this.bank, this.crowdsale.address, ROLE_BANK_MANAGER);
        await this.crowdsale.send(ether(1)).should.be.rejectedWith(EVMRevert);
        await this.crowdsale.buyTokens(investor, { value: ether(1), from: investor }).should.be.rejectedWith(EVMRevert);
    });

    it('should allow owner change rate', async function () {
        const rateBefore = await this.crowdsale.rate();
        rateBefore.should.be.bignumber.equal(RATE);

        // new rate is different
        const newRate = new BigNumber(23);
        rateBefore.should.not.be.bignumber.equal(newRate);

        // set new rate
        await this.crowdsale.changeRate(newRate, { from: owner }).should.be.fulfilled;

        const rateAfter = await this.crowdsale.rate();
        rateAfter.should.be.bignumber.equal(newRate);
    });

    it('should not allow not owner change rate', async function () {
        // new rate is different
        const newRate = new BigNumber(23);

        // set new rate
        await this.crowdsale.changeRate(newRate, { from: investor }).should.be.rejectedWith(EVMRevert);
    });

    // it('should send tokens to beneficiary by owner during crowdsale', async function () {
    //     const investmentAmount = ether(1);
    //     await increaseTimeTo(this.startTime);
    //     const expectedTokenAmount = RATE.mul(investmentAmount);
    //
    //     await this.crowdsale.sendTokensTo(investor, expectedTokenAmount, { from: owner }).should.be.fulfilled;
    //
    //     (await this.token.balanceOf(investor)).should.be.bignumber.equal(expectedTokenAmount);
    //     (await this.token.totalSupply()).should.be.bignumber.equal(TOTAL_SUPPLY);
    // });
    //
    // it('should send tokens to beneficiary by owner before crowdsale', async function () {
    //     const investmentAmount = ether(1);
    //     const tokenAmount = RATE.mul(investmentAmount);
    //
    //     await this.crowdsale.sendTokensTo(investor, tokenAmount, { from: owner }).should.be.fulfilled;
    //
    //     (await this.token.balanceOf(investor)).should.be.bignumber.equal(tokenAmount);
    //     (await this.token.totalSupply()).should.be.bignumber.equal(TOTAL_SUPPLY);
    // });
    //
    // it('should not send tokens to beneficiary by NOT owner', async function () {
    //     const investmentAmount = ether(1);
    //     await increaseTimeTo(this.startTime);
    //     await addRole(this.bank, this.crowdsale.address, ROLE_BANK_MANAGER);
    //     await this.crowdsale.sendTokensTo(owner, investmentAmount, { from: investor }).should.be.rejectedWith(EVMRevert);
    // });
});