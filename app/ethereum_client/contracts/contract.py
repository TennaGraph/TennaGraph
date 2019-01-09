
class Contract(object):
    """Ethereum Smart Contract representation class

        It is assumed you'll subclass this class for each of your contracts
        and implement appropriate .transact(), .call(), .estimateGas() methods there.
        See http://web3py.readthedocs.io/en/stable/contracts.html for details

    """

    client = None

    # address
    address = None

    # Contract handler
    # See http://web3py.readthedocs.io/en/stable/contracts.html for handler methods
    handler = None

    def __init__(self, client, abi, address):
        """Contract class constructor.

        Args:
            client (EthereumClient): ethereum_app client handler
            abi (str): serialized json code of the contract
            address (str): contract actual address we're working on

        """
        self.abi = abi
        self.address = address
        self.client = client
        self.handler = self._contract_handler()

    def _contract_handler(self):
        return self.client.fetch_contract(self.abi, self.address)

    def fetch_events(self, event_name, from_block, to_block='latest'):
        log_filter = self.handler.eventFilter(event_name, {'fromBlock': from_block, 'toBlock': to_block})
        return log_filter.get_all_entries()
