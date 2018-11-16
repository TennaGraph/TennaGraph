# Pip imports
from rest_framework import serializers

# Project imports
from base.utils import ChoiceDisplayField

# App imports
from ..models import Stance


class StanceSerializer(serializers.ModelSerializer):

    choice = ChoiceDisplayField(Stance.CHOICES)

    status = ChoiceDisplayField(Stance.STATUSES, read_only=True)

    class Meta:
        model = Stance
        fields = "__all__"