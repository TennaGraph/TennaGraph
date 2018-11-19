# Django imports
from django.db import models

# Project imports
from base.models import TimeStampedModel
from eip.models import EIP


class Stance(TimeStampedModel):

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

    author      = models.CharField(max_length=255)
    proof_url   = models.URLField()
    choice      = models.CharField(choices=CHOICES, max_length=7)
    status      = models.CharField(choices=STATUSES, max_length=8, default=PENDING)
    eip         = models.ForeignKey(EIP, on_delete=models.CASCADE)




