const shouldFail = require('openzeppelin-solidity/test/helpers/shouldFail');
const { ethGetBalance, ethSendTransaction } = require('openzeppelin-solidity/test/helpers/web3');

const BigNumber = web3.BigNumber;

require('chai')
  .use(require('chai-as-promised'))
  .use(require('chai-bignumber')(BigNumber))
  .should();


const VotingManager = artifacts.require('VotingManager');
const VotingOption = artifacts.require('VotingOption');


contract('VotingContract', function ([owner, user1, user2]) {
    const PROPOSAL_NUM = new BigNumber(20);
    const IS_VOTING_OPEN = true;


    beforeEach(async function () {
        // Voting Manger
        this.votingManager = await VotingManager.new({ from: owner });

        // Create proposal
        await this.votingManager.addProposal(PROPOSAL_NUM, IS_VOTING_OPEN, { from: owner }).should.be.fulfilled;
    });

    it('should create votingManager with correct parameters', async function () {
        this.votingManager.should.exist;

        const proposalsCount = await this.votingManager.proposalsCount();

        proposalsCount.should.be.bignumber.equal(1);
    });

    it('should create proposal in the votingManager with correct parameters', async function () {
        const proposalNum20 = await this.votingManager.proposals(PROPOSAL_NUM);

        proposalNum20[0].should.be.bignumber.equal(PROPOSAL_NUM);
        proposalNum20[1].should.equal(true);
        proposalNum20[2].should.exist;
        proposalNum20[3].should.exist;
        proposalNum20[4].should.exist;
    });

    it('should not allow owner of votingManager change voting', async function () {
        const isAuthorized = await this.votingManager.isAuthorized();

        isAuthorized.should.equal(false);
    });

    it('should proposal exists', async function () {
        const isProposalExists = await this.votingManager.isProposalExists(PROPOSAL_NUM);

        isProposalExists.should.equal(true);
    });

    it('should allow creating proposals for anyone', async function () {
        // prepare
        const proposalNum = 721;
        const isVotingActive = false;
        const notAuthorizedContractAddress = "0x1111111111111111111111111111111111111111";
        (await this.votingManager.proposalsCount()).should.be.bignumber.equal(1);

        // action
        await this.votingManager.addProposal(proposalNum, false, { from: user1 }).should.be.fulfilled;

        // result
        (await this.votingManager.proposalsCount()).should.be.bignumber.equal(2);
        const proposalResponse = await this.votingManager.proposals(proposalNum);

        const propResponseNum = proposalResponse[0];
        const propResponseIsVotingActive = proposalResponse[1];
        const propResponsevotingCreatedAt = proposalResponse[2];
        const propResponseYayAddress = proposalResponse[3];
        const propResponseNayAddress = proposalResponse[4];
        const propResponseAbstainAddress = proposalResponse[5];

        // check proposal response
        propResponseNum.should.be.bignumber.equal(proposalNum);
        propResponseIsVotingActive.should.equal(isVotingActive);
        propResponsevotingCreatedAt.should.exist;
        propResponseYayAddress.should.exist;
        propResponseNayAddress.should.exist;
        propResponseAbstainAddress.should.exist;

        // check weather addresses are authorized in votingManger
        (await this.votingManager.authorizedContracts(propResponseYayAddress)).should.be.equal(true);
        (await this.votingManager.authorizedContracts(propResponseNayAddress)).should.be.equal(true);
        (await this.votingManager.authorizedContracts(propResponseAbstainAddress)).should.be.equal(true);
        (await this.votingManager.authorizedContracts(notAuthorizedContractAddress)).should.be.equal(false);
    });

    it('should allow voting when the voting is active', async function () {
        // prepare
        const proposalResponse = await this.votingManager.proposals(PROPOSAL_NUM);
        const propResponseYay = await VotingOption.at(proposalResponse[3]);
        const propResponseNay = await VotingOption.at(proposalResponse[4]);
        const propResponseAbstain = await VotingOption.at(proposalResponse[5]);

        // action
        await propResponseYay.vote().should.be.fulfilled;

        // results
        const votingResults = await this.votingManager.votingResults(PROPOSAL_NUM, {from: user1});
        const votingResultYay = votingResults[0];
        const votingResultNay = votingResults[1];
        const votingResultAbstain = votingResults[2];

        const ownerBalance = await ethGetBalance(owner);

        votingResultYay.should.be.bignumber.equal(ownerBalance);
        votingResultNay.should.be.bignumber.equal(0);
        votingResultAbstain.should.be.bignumber.equal(0);
    });

    it('should allow set voting status by votingManager owner', async function () {
        // prepare
        const proposalResponse = await this.votingManager.proposals(PROPOSAL_NUM);
        const propResponseIsVotingActive = proposalResponse[1];
        propResponseIsVotingActive.should.equal(true);

        // action
        await this.votingManager.changeProposalStatus(PROPOSAL_NUM, false, {from: owner});

        // results
        const proposalResponseRes = await this.votingManager.proposals(PROPOSAL_NUM);
        const propResponseIsVotingActiveRes = proposalResponseRes[1];
        propResponseIsVotingActiveRes.should.equal(false);
    });

    it('should not allow set voting status by not votingManager owner', async function () {
        // prepare
        const proposalResponse = await this.votingManager.proposals(PROPOSAL_NUM);
        const propResponseIsVotingActive = proposalResponse[1];
        propResponseIsVotingActive.should.equal(true);

        // action
        await shouldFail.reverting(this.votingManager.changeProposalStatus(PROPOSAL_NUM, false, {from: user1}));
    });

    it('should deny voting when the voting is not active', async function () {
        // prepare
        const proposalResponse = await this.votingManager.proposals(PROPOSAL_NUM);
        const propResponseYay = await VotingOption.at(proposalResponse[3]);
        const propResponseNay = await VotingOption.at(proposalResponse[4]);
        const propResponseAbstain = await VotingOption.at(proposalResponse[5]);

        // action
        await this.votingManager.changeProposalStatus(PROPOSAL_NUM, false, {from: owner});

        // results
        await shouldFail.reverting(propResponseYay.vote());
        await shouldFail.reverting(propResponseNay.vote());
        await shouldFail.reverting(propResponseAbstain.vote());
    });

    it('should allow resubmit voting from yay to nay when the voting is active', async function () {
        // prepare
        const proposalResponse = await this.votingManager.proposals(PROPOSAL_NUM);
        const propResponseYay = await VotingOption.at(proposalResponse[3]);
        const propResponseNay = await VotingOption.at(proposalResponse[4]);

        // action
        await propResponseYay.vote().should.be.fulfilled;
        await propResponseNay.vote().should.be.fulfilled;

        // results
        const votingResults = await this.votingManager.votingResults(PROPOSAL_NUM, {from: user1});
        const votingResultYay = votingResults[0];
        const votingResultNay = votingResults[1];
        const votingResultAbstain = votingResults[2];

        const ownerBalance = await ethGetBalance(owner);

        votingResultYay.should.be.bignumber.equal(0);
        votingResultNay.should.be.bignumber.equal(ownerBalance);
        votingResultAbstain.should.be.bignumber.equal(0);
    });

    it('should allow resubmit voting from yay to abstain when the voting is active', async function () {
        // prepare
        const proposalResponse = await this.votingManager.proposals(PROPOSAL_NUM);
        const propResponseYay = await VotingOption.at(proposalResponse[3]);
        const propResponseAbstain = await VotingOption.at(proposalResponse[5]);

        // action
        await propResponseYay.vote().should.be.fulfilled;
        await propResponseAbstain.vote().should.be.fulfilled;

        // results
        const votingResults = await this.votingManager.votingResults(PROPOSAL_NUM, {from: user1});
        const votingResultYay = votingResults[0];
        const votingResultNay = votingResults[1];
        const votingResultAbstain = votingResults[2];

        const ownerBalance = await ethGetBalance(owner);

        votingResultYay.should.be.bignumber.equal(0);
        votingResultNay.should.be.bignumber.equal(0);
        votingResultAbstain.should.be.bignumber.equal(ownerBalance);
    });

});