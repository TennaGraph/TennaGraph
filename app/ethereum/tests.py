# Pip imports
from rest_framework.test import APITestCase

# App imports
from .services import EthereumClient


class EthereumClientTestCase(APITestCase):

    eth_client = None

    def setUp(self):
        self.eth_client = EthereumClient()


class EthereumUtilsTestCase(APITestCase):
    eth_client = None

    def setUp(self):
        self.eth_client = EthereumClient()

    def test_should_find_nearest_block_with_first_transaction(self):
        pass

