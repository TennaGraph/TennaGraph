# Pip imports
from rest_framework.test import APITestCase

# App imports
from .services import EthereumClient
from .services import BlocksCoutClient
from .services.blockscout_client import RequestMaker as BlocksCoutRequestMaker


# class EthereumClientTestCase(APITestCase):
#
#     eth_client = None
#
#     def setUp(self):
#         self.eth_client = EthereumClient()
#
#
# class EthereumUtilsTestCase(APITestCase):
#     eth_client = None
#
#     def setUp(self):
#         self.eth_client = EthereumClient()
#
#     def test_should_find_nearest_block_with_first_transaction(self):
#         pass
#


class BlocksCoutClientTestCase(APITestCase):

    blockscout_client = None

    def setUp(self):
        request_maker = BlocksCoutRequestMaker(base_url='https://blockscout.com/eth/rinkeby/api')
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






