# Django imports
from django.conf import settings

# Pip imports
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

# App imports
from .services import BlocksCoutClient
from .services import EthereumClient
from .services.blockscout_client import RequestMaker as BlocksCoutRequestMaker
from .tasks import fetch_transactions_info
from .tasks import load_voting_details_logs
from .tasks import load_votes
from .models import EthVoter
from .models import VoteLog
from .models import VotingDetailsLog
from .contracts import VotingManagerContract

# Project imports
from eip.models import EIP



class BlocksCoutClientTestCase(APITestCase):

    blockscout_client = None

    blockscout_base_url = 'https://blockscout.com/eth/rinkeby/api'

    def setUp(self):
        settings.BLOCKSCOUT_BASE_URL = self.blockscout_base_url
        request_maker = BlocksCoutRequestMaker(base_url=self.blockscout_base_url)
        self.blockscout_client = BlocksCoutClient(request_maker)

    def test_should_load_at_least_one_tx(self):
        address = '0xc116fBb7453514e1ee545974DFC1796c704E1365'

        result = self.blockscout_client.load_transactions(address, 0, 3488294)

        self.assertTrue(isinstance(result, list))
        self.assertGreater(len(result), 1)

    def test_should_tx_contain_tx_info(self):
        address = '0xc116fBb7453514e1ee545974DFC1796c704E1365'
        raw_tx = {
          "value": "2024271009402738838",
          "txreceipt_status": "1",
          "transactionIndex": "7",
          "to": "0xc116fbb7453514e1ee545974dfc1796c704e1365",
          "timeStamp": "1544107413",
          "nonce": "1101",
          "isError": "0",
          "input": "0x",
          "hash": "0xf4d31c4a72eba01f0d03c59e3f8e59cfe25a337b88ebd198b75c49c6395a37cd",
          "gasUsed": "21000",
          "gasPrice": "10000000000",
          "gas": "21000",
          "from": "0x4a944c2ca92001cafaf31d41c548f77008e31581",
          "cumulativeGasUsed": "406949",
          "contractAddress": "",
          "confirmations": "110218",
          "blockNumber": "3465249",
          "blockHash": "0xb5ab0035d8e8bdc0cfc547b10035dbf948b90b48cfa96fa92b96c4d58ee172d8"
        }

        result = self.blockscout_client.load_transactions(address, 0, 3488294)

        self.assertTrue(isinstance(result, list))
        self.assertGreater(len(result), 1)

        oldest_tx = result[0]
        self.assertEqual(oldest_tx['nonce'],                raw_tx['nonce'])
        self.assertEqual(oldest_tx['hash'],                 raw_tx['hash'])
        self.assertEqual(oldest_tx['gasUsed'],              raw_tx['gasUsed'])
        self.assertEqual(oldest_tx['cumulativeGasUsed'],    raw_tx['cumulativeGasUsed'])
        self.assertEqual(oldest_tx['blockHash'],            raw_tx['blockHash'])

    def test_should_load_right_amount_of_gas(self):
        voter_raw = {
            'address': '0xc116fBb7453514e1ee545974DFC1796c704E1365',
        }
        EthVoter.objects.create(**voter_raw)
        voters = EthVoter.objects.all()
        voter = voters[0]
        self.assertEqual(len(voters), 1)
        self.assertEqual(voter.used_gas, 0)

        fetch_transactions_info()
        voter = EthVoter.objects.get(id=voter.id)

        fetch_transactions_info()
        voter2 = EthVoter.objects.get(id=voter.id)

        # This is gas of each transactions on https://rinkeby.etherscan.io/address/0xc116fbb7453514e1ee545974dfc1796c704e1365
        # Last transaction was made on block: 3488294
        gas_used = 30731 + 25256 + 129833 + 773419 + 129833 + 773419 + 788419 + 1884894 + 1873560 + 21000
        self.assertGreaterEqual(voter.used_gas, gas_used)
        self.assertEqual(voter.used_gas, voter2.used_gas)




class VotingManagerContractTestCase(APITestCase):

    ethereum_provider_url = 'wss://rinkeby.infura.io/ws'

    voting_manager_address = '0x4B97C18916F288A4b0A6a14ed7732031395b8f7F'

    contract_deploy_block = 3620085

    voting_manager = None

    def setUp(self):
        self.eth_client = EthereumClient(self.ethereum_provider_url)
        self.voting_manager = VotingManagerContract(self.eth_client, address=self.voting_manager_address)

    def test_should_load_more_than_0_votes_logs(self):

        events = list(self.voting_manager.load_votes_logs(from_block=self.contract_deploy_block))
        event = events[0]

        self.assertGreaterEqual(len(events), 1)

        self.assertEqual(event.get('proposal_id'), 20)
        self.assertEqual(event.get('voter'), '0xc116fBb7453514e1ee545974DFC1796c704E1365')
        self.assertEqual(event.get('selected_option'), 1)

    def test_should_load_more_than_0_voting_details_logs(self):

        events = list(self.voting_manager.load_voting_details_logs(from_block=self.contract_deploy_block))
        event = events[0]

        self.assertGreaterEqual(len(events), 1)

        self.assertEqual(event.get('proposal_id'), 20)
        self.assertIsNotNone(event.get('is_voting_open', None))

    def test_should_load_voting_details_logs(self):
        eip_dict = {
            'eip_num': '20',
            'eip_title': 'Title of EIP',
            'eip_status': EIP.ACTIVE,
            'eip_type': EIP.INFORMATIONAL,
            'eip_category': EIP.ERC,
            'eip_authors': 'Authors here',
            'eip_created': '2015-10-27',

            'file_name': 'File name here',
            'file_download_url': 'https://google.com.ua/',
            'file_content': 'Here markdown text from md file',
            'file_sha': '0xjsfidsfseuiui34893hbsfo2i2ifeg',
        }
        EIP.objects.create(**eip_dict)
        logs_count = VotingDetailsLog.objects.count()
        self.assertEqual(logs_count, 0)

        load_voting_details_logs()

        eip = EIP.objects.get(eip_num=eip_dict['eip_num'])
        logs_count = VotingDetailsLog.objects.count()

        self.assertGreaterEqual(logs_count, 1)
        self.assertIsNotNone(eip.voting_details)
        self.assertGreaterEqual(eip.voting_details.block_number, 3620085)
        self.assertGreaterEqual(eip.voting_details.block_number, 3620085)
        self.assertIsNotNone(eip.voting_details.is_voting_open)

    def test_should_load_votes_logs(self):
        logs_count = VoteLog.objects.count()
        voters_count = EthVoter.objects.count()
        self.assertEqual(logs_count, 0)
        self.assertEqual(voters_count, 0)

        load_votes()

        logs_count = VoteLog.objects.count()
        voters_count = EthVoter.objects.count()
        self.assertGreaterEqual(logs_count, 1)
        self.assertEqual(voters_count, 1)

        # check weather it is not storing duplicates
        load_votes()

        logs_count2 = VoteLog.objects.count()
        voters_count2 = EthVoter.objects.count()
        self.assertEqual(logs_count, logs_count2)
        self.assertEqual(voters_count, voters_count2)

    def test_should_not_load_logs_from_blocks_less_than_configured(self):
        eth_client = EthereumClient()
        voting_manager = VotingManagerContract(client=eth_client)

        from_block = 3620132

        logs = voting_manager.load_votes_logs(from_block=from_block)
        logs = list(map(lambda l: VoteLog.objects.create(**l), logs))

        for log in logs:
            self.assertNotEqual(log.block_number, from_block)



class VotingResultsTestCase(APITestCase):


    def test_should_retrieve_right_results(self):
        proposal_id = 20
        yay_address = '0xf883902811f21934ff9d930e18bdbabef7111111'
        yay_used_gas = 12300
        vote_yay = {
            'voter': yay_address,
            'selected_option': VoteLog.YAY,
            'proposal_id': proposal_id,
            'block_number': 399,
        }
        eth_voter_yay = {
            'address': yay_address,
            'last_block': 25,
            'last_tx_hash': '0x0',
            'used_gas': yay_used_gas,
        }
        VoteLog.objects.create(**vote_yay)
        EthVoter.objects.create(**eth_voter_yay)


        nay_address = '0xf883902811f21934ff9d930e18bdbabef7222222'
        nay_used_gas = 3456435
        vote_nay = {
            'voter': nay_address,
            'selected_option': VoteLog.NAY,
            'proposal_id': proposal_id,
            'block_number': 399,
        }
        eth_voter_nay = {
            'address': nay_address,
            'last_block': 25,
            'last_tx_hash': '0x0',
            'used_gas': nay_used_gas,
        }
        VoteLog.objects.create(**vote_nay)
        EthVoter.objects.create(**eth_voter_nay)


        abstain_address = '0xf883902811f21934ff9d930e18bdbabef7333333'
        abstain_used_gas = 567734
        vote_abstain = {
            'voter': abstain_address,
            'selected_option': VoteLog.ABSTAIN,
            'proposal_id': proposal_id,
            'block_number': 399,
        }
        eth_voter_abstain = {
            'address': abstain_address,
            'last_block': 25,
            'last_tx_hash': '0x0',
            'used_gas': abstain_used_gas,
        }
        VoteLog.objects.create(**vote_abstain)
        EthVoter.objects.create(**eth_voter_abstain)


        url = reverse("ethereum_client:gas_voting", kwargs={'proposal_id': proposal_id})

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, dict))

        eip_response = response.data

        self.assertEqual(eip_response['yay'],         yay_used_gas)
        self.assertEqual(eip_response['nay'],         nay_used_gas)
        self.assertEqual(eip_response['abstain'],     abstain_used_gas)

