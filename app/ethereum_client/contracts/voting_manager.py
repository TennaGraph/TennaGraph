# Stdlib imports
import os
import json

# Django imports
from django.conf import settings
from django.core.files import File

# Pip imports
from web3 import Web3

# App imports
from .contract import Contract


class VotingManagerContract(Contract):

    def __init__(self, client, abi=None, address=None):
        """
        :param client: (EthClient)
        :param abi: contract abi
        :param address: contract address
        """
        if not abi:
            abi = self.load_default_abi()

        if not address:
            address = settings.VOTING_MANAGER_CONTRACT_ADDRESS

        super().__init__(client, abi, address)

    @classmethod
    def voting_details_log_parser(cls, log):
        args = log.get('args')
        return {
            "proposal_id": args["proposalId"],
            "is_voting_open": args["isVotingOpen"],
            "block_number": log["blockNumber"]
        }

    @classmethod
    def votes_log_parser(cls, log):
        args = log.get('args')
        return {
            "proposal_id": args["proposalId"],
            "voter": Web3.toChecksumAddress(args["voter"]),
            "selected_option": args["selectedOption"],
            "block_number": log["blockNumber"]
        }

    def load_voting_details_logs(self, from_block):
        logs = super().fetch_events('VotingDetails', from_block)
        return map(lambda l: self.voting_details_log_parser(l), logs)

    def load_votes_logs(self, from_block):
        logs = super().fetch_events('Vote', from_block)
        return map(lambda l: self.votes_log_parser(l), logs)

    def load_default_abi(self):
        artifacts_path = os.path.join(settings.STATIC_ROOT, 'contracts/VotingManager.json')
        artifacts = json.load(open(artifacts_path, 'rb'))

        return artifacts.get('abi')