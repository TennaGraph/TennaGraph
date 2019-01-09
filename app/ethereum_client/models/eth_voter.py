# Django imports
from django.db import models

# Project imports
from base.models import TimeStampedModel


class EthVoter(TimeStampedModel):
    """
    Stores information about voter and how mach he has accumulated fired gas till last block

    """

    # voter address
    address             = models.CharField(max_length=42, unique=True)

    # last block which was included
    last_block          = models.BigIntegerField(default=0)

    # last tx hash which was included
    last_tx_hash        = models.CharField(max_length=66, null=True, blank=True)

    # accumulated gas value
    used_gas           = models.BigIntegerField(default=0)

    def __str__(self):
        return "{}, {}".format(self.address, self.used_gas)

    def append_used_gas(self, used_gas, last_tx_raw):
        """
        {
          "blockHash": "0x373d339e45a701447367d7b9c7cef84aab79c2b2714271b908cda0ab3ad0849b",
          "blockNumber": "65204",
          "confirmations": "5994246",
          "contractAddress": "",
          "cumulativeGasUsed": "122207",
          "from": "0x3fb1cd2cd96c6d5c0b5eb3322d807b34482481d4",
          "gas": "122261",
          "gasPrice": "50000000000",
          "gasUsed": "122207",
          "hash": "0x98beb27135aa0a25650557005ad962919d6a278c4b3dde7f4f6a3a1e65aa746c",
          "input": "0xf00d4b5d000000000000000000000000036c8cecce8d8bbf0831d840d7f29c9e3ddefa63000000000000000000000000c5a96db085dda36ffbe390f455315d30d6d3dc52",
          "isError": "0",
          "nonce": "0",
          "timeStamp": "1439232889",
          "to": "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",
          "transactionIndex": "0",
          "txreceipt_status": "1",
          "value": "0"
        }

        :param used_gas:
        :param last_tx_raw:
        :return:
        """

        self.used_gas += used_gas
        self.last_block = last_tx_raw.get('blockNumber')
        self.last_tx_hash = last_tx_raw.get('hash')
