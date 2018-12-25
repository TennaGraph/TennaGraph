# Django imports
from django.db import models

# Project imports
from base.models import TimeStampedModel


class EthVoter(TimeStampedModel):
    """
    Stores information about voter and how mach he has accumulated fired gas till last block

    """

    # voter address
    address             = models.CharField(max_length=42)

    # last block which was included
    last_block          = models.BigIntegerField(default=0)

    # accumulated gas value
    spent_gas           = models.BigIntegerField(default=0)

    def __str__(self):
        return "{}, {}".format(self.address, self.spent_gas)