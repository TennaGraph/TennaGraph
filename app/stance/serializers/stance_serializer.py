# Pip imports
from rest_framework import serializers

# Project imports
from base.utils import ChoiceDisplayField
from eip.models import EIP

# App imports
from ..models import Stance


class StanceSerializer(serializers.ModelSerializer):

    choice = ChoiceDisplayField(Stance.CHOICES)

    status = ChoiceDisplayField(Stance.STATUSES, read_only=True)

    eip_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Stance
        fields = ['id', 'author', 'proof_url', 'choice', 'status', 'eip_id']

    """
    Validators
    """

    def validate_eip_id(self, eip_id):
        if not EIP.objects.filter(id=eip_id).exists():
            raise serializers.ValidationError("No EIP with such id")
        return  eip_id

    def validate(self, attrs):
        proof_url = attrs.get('proof_url', None)
        eip_id = attrs.get('eip_id', None)
        if Stance.objects.filter(eip_id=eip_id, proof_url=proof_url).exists():
            raise serializers.ValidationError("This url already submitted")

        return attrs

