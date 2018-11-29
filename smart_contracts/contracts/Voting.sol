pragma solidity ^0.4.24;

import 'openzeppelin-solidity/contracts/ownership/Ownable.sol';


contract VotingOption {

    uint8 optionId;
    uint proposalId;

    VotingManager votingManager;

    constructor(uint8 _optionId, uint _proposalId, VotingManager _votingManager) public {
        require(_optionId == 1 || _optionId == 2 || _optionId == 3, 'Option does not exist');
        require(_votingManager != address(0), 'Voting can not have 0x address');

        optionId = _optionId;
        proposalId = _proposalId;
        votingManager = _votingManager;
    }

    function () external {
        vote();
    }

    function vote() internal {
        votingManager.vote(proposalId, optionId, msg.sender);
    }

}


/**
 * @title AuthorizedContracts
 * @dev The AuthorizedContracts contract has map of addresses, and provides basic authorization control
 * functions, this simplifies the implementation of "voting permissions".
 */
contract AuthorizedContracts {
    mapping(address => bool) public authorizedContracts;

    /**
    * @dev Throws if called by any contract which is not in authorizedContracts.
    */
    modifier onlyAllowedContracts() {
        require(isAuthorized());
        _;
    }

    /**
    * @return true if `msg.sender` is in allowedContracts of the contract.
    */
    function isAuthorized() public view returns(bool) {
        return authorizedContracts[msg.sender];
    }
}


/**
 * @title VotingManager
 * @dev Smart contract which gives ability to take participation in EIPs
 */
contract VotingManager is Ownable, AuthorizedContracts {

    struct Voter {
        bool voted;
        uint8 selectedOption;
    }

    struct Proposal {
        uint id;
        bool isVotingOpen;
        address[] participants;
        mapping(address => Voter) voters;

        VotingOption yay;
        VotingOption nay;
        VotingOption obstain;
    }

    mapping(uint => Proposal) public proposals;


    function addProposal(uint _proposalId, bool _isVotingOpen) onlyOwner public {
        require(proposals[_proposalId].id != _proposalId, 'Proposal already exists');

        // create proposal
        Proposal storage proposal = proposals[_proposalId];
        proposal.id = _proposalId;
        proposal.isVotingOpen = _isVotingOpen;

        // create contracts to allow voting just with simple transaction to contract address
        proposal.yay = new VotingOption(1, _proposalId, this);
        proposal.nay = new VotingOption(2, _proposalId, this);
        proposal.obstain = new VotingOption(3, _proposalId, this);

        // authorize contracts
        authorizedContracts[address(proposal.yay)] = true;
        authorizedContracts[address(proposal.nay)] = true;
        authorizedContracts[address(proposal.obstain)] = true;

        proposals[_proposalId] = proposal;
    }

    function changeProposalStatus(uint _proposalId, bool _isVotingOpen) onlyOwner public {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id == _proposalId, 'Proposal does not exist');
        require(proposal.isVotingOpen != _isVotingOpen, 'Proposal already has this status');

        proposal.isVotingOpen = _isVotingOpen;
    }

    /// Give a single vote to proposal.
    function vote(uint _proposalId, uint8 _selectedOption, address _sender) onlyAllowedContracts public {
        Proposal storage proposal = proposals[_proposalId];
        Voter storage voter = proposal.voters[_sender];

        // check requirements
        require(proposal.id == _proposalId, 'Proposal does not exists');
        require(proposal.isVotingOpen == true, 'Voting is closed');
        require(voter.selectedOption != _selectedOption, 'Already voted for this option');

        // set voting
        voter.voted = true;
        voter.selectedOption = _selectedOption;

        // save results
        proposals[_proposalId] = proposal;
        proposal.participants.push(_sender);
    }

    function votingResults(uint _proposalId) public view returns (uint[] memory) {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id == _proposalId, 'Proposal does not exist');

        address[] storage participants = proposal.participants;

        uint[] memory results = new uint[](3);

        for (uint8 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            Voter storage voter = proposal.voters[participant];

            results[voter.selectedOption-1] = results[voter.selectedOption-1] + address(participant).balance;
        }

        return results;
    }

    function votingAddresess(uint _proposalId) public view returns (address[3]) {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.id == _proposalId, 'Proposal does not exist');

        return [address(proposal.yay), address(proposal.nay), address(proposal.obstain)];
    }
}

