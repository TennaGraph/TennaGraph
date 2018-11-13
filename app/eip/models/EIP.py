# Django imports
from django.db import models

# Project imports
from base.models import TimeStampedModel


class EIP(TimeStampedModel):
    title = models.TextField(max_length=100)