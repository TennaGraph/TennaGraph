# Django imports
from django.db import models

# Project imports
from base.models import TimeStampedModel


class VoteLog(TimeStampedModel):
    """
    Stores information about voter and how mach he has accumulated fired gas till last block

    """

    YAY = 1
    NAY = 2
    ABSTAIN = 3

    CHOICES = (
        (YAY, 'yay'),
        (NAY, 'nay'),
        (ABSTAIN, 'abstain'),
    )


    # voter address
    voter               = models.CharField(max_length=42)

    selected_option     = models.IntegerField(choices=CHOICES)

    proposal_id         = models.IntegerField()

    block_number        = models.IntegerField()

    def __str__(self):
        return "{}, {}".format(self.voter, self.selected_option)

