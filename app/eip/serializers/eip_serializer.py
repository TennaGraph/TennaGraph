# Pip imports
from rest_framework import serializers

# Project imports
from base.utils import ChoiceDisplayField
from ethereum_client.serializers import VotingDetailsLogSerializer
from ethereum_client.models import VotingDetailsLog

# App imports
from ..models import EIP


class EIPSerializer(serializers.ModelSerializer):

    eip_status = ChoiceDisplayField(choices=EIP.PROPOSAL_STATUSES)

    eip_type = ChoiceDisplayField(choices=EIP.TYPES)

    eip_category = ChoiceDisplayField(choices=EIP.CATEGORIES)

    voting_details = serializers.SerializerMethodField(read_only=True, required=False)

    class Meta:
        model = EIP
        fields = "__all__"


    """
    Getters
    """

    def get_voting_details(self, obj):
        try:
            serializer = VotingDetailsLogSerializer(
                instance=VotingDetailsLog.objects.get(proposal_id=obj.eip_num),
                many = False
            )
            return serializer.data
        except VotingDetailsLog.DoesNotExist:
            return None
