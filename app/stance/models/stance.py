# Django imports
from django.db import models

# Project imports
from base.models import TimeStampedModel
from eip.models import EIP
from influencer.models import Influencer
from github_client.abstract import GitHubCompatible


class Stance(TimeStampedModel, GitHubCompatible):

    YAY     = 'YAY'
    NAY     = 'NAY'
    ABSTAIN = 'ABSTAIN'

    CHOICES = (
        (YAY, 'yay'),
        (NAY, 'nay'),
        (ABSTAIN, 'abstain'),
    )

    """
    All new stances will be with pending status
    """
    PENDING = 'PENDING'

    """
    All inappropriate stances will be with rejected status
    """
    REJECTED = 'REJECTED'

    """
    Reviewed and appropriate stance wil be calculated in general statistics
    """
    APPROVED = 'APPROVED'

    STATUSES = (
        (PENDING,  'pending'),
        (REJECTED, 'rejected'),
        (APPROVED, 'approved'),
    )


    TWITTER = 'TWITTER'
    OTHER = 'OTHER'

    PROOF_CHOICES = (
        (TWITTER, 'twitter'),
        (OTHER, 'other'),
    )


    author              = models.CharField(max_length=255)

    """ This field filled if the author above is influencer """
    influencer          = models.ForeignKey(Influencer, on_delete=models.SET_NULL, null=True, blank=True)

    proof_url           = models.URLField()

    proof_type          = models.CharField(max_length=20, choices=PROOF_CHOICES, default=OTHER)

    proof_last_check    = models.DateTimeField(null=True, blank=True)

    choice              = models.CharField(choices=CHOICES, max_length=7)

    status              = models.CharField(choices=STATUSES, max_length=8, default=PENDING)

    eip                 = models.ForeignKey(EIP, on_delete=models.CASCADE)

    """
    
    """

    def git_options(self):
        from ..serializers import StanceSerializer

        return {
            'folder': 'stances',
            'serializer': StanceSerializer
        }

    def git_fields(self):
        pass



