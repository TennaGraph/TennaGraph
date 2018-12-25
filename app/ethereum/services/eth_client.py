# Stdlib imports
import logging
from enum import Enum

from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

# Django imports
from django.conf import settings


logger = logging.getLogger(__name__)

ETHEREUM_URL_WEB3_PROVIDER = getattr(settings, 'ETHEREUM_URL_WEB3_PROVIDER', None)


class Web3Provider(Enum):
    GETH    = 0
    PARITY  = 1


class EthereumClient(object):
    """Ethereum client class"""

    # Handler for Ethereum connection via Web3 HTTP
    connection = None

    info = None

    def __init__(self, http_provider_url=ETHEREUM_URL_WEB3_PROVIDER):
        self.connection = Web3(HTTPProvider(http_provider_url, request_kwargs={'timeout': 40}))

        if settings.APP_ENV == 'production' or settings.APP_ENV == 'testing':
            # for PoA and Rinkeby we have to add middleware
            self.connection.middleware_stack.inject(geth_poa_middleware, layer=0)

    def provider(self):
        connected = self.connection.isConnected()

        if connected and self.connection.version.node.startswith('Parity'):
            node = Web3Provider.PARITY

        elif connected and (self.connection.version.node.startswith('Geth') or self.connection.version.node.startswith('ethermint')):
            node = Web3Provider.GETH

        else:
            node = None

        return node

    def get_block(self, block_number='latest'):
        """Get block data

        Args:
            block_number (Optional[int]): block number, uses latest if not specified

        """
        return self.connection.eth.getBlock(block_number)

    def get_transaction_сount(self, address, block_number='latest'):
        return self.connection.eth.getTransactionCount(address)

    def transaction_receipt(self, tx_hash):
        return self.connection.eth.getTransactionReceipt(tx_hash)
