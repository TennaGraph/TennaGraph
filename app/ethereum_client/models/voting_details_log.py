# Django imports
from django.db import models

# Project imports
from base.models import TimeStampedModel


class VotingDetailsLog(TimeStampedModel):
    """
    Stores information about proposal voting, weather it is active or not

    """

    proposal_id             = models.IntegerField()

    is_voting_open          = models.BooleanField()

    block_number            = models.IntegerField()

    def __str__(self):
        return "Proposal: {}, active: {}, block: {}".format(self.proposal_id, self.is_voting_open, self.block_number)

