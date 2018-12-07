# Django imports
from django.db import models
from django.core.exceptions import ValidationError

# Pip imports
from web3 import Web3


def validate_address(value):
    is_address = Web3.isAddress(value)
    if not is_address:
        raise ValidationError("Not valid Eth address. Please check it again")

    if not Web3.isChecksumAddress(value):
        raise ValidationError('Address has an invalid EIP checksum')


class SystemSettings(models.Model):
    is_maintenance = models.BooleanField(default=False)

    support_email = models.EmailField(default="test@gmail.com")

    contract_vot_manager_address = models.CharField(max_length=42, validators=[validate_address], null=True, blank=True)

    last_update_influencers = models.DateTimeField(null=True, blank=True)
