# Pip imports
from rest_framework import serializers

# Project imports
from base.utils import ChoiceDisplayField

# App imports
from ..models import EIP


class EIPSerializer(serializers.ModelSerializer):

    eip_status = ChoiceDisplayField(choices=EIP.PROPOSAL_STATUSES)

    eip_type = ChoiceDisplayField(choices=EIP.PROPOSAL_STATUSES)

    eip_category = ChoiceDisplayField(choices=EIP.PROPOSAL_STATUSES)

    class Meta:
        model = EIP
        fields = "__all__"