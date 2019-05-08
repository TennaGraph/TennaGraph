# Pip imports
from rest_framework import serializers

# App imports
from ..models import VotingDetailsLog


class VotingDetailsLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = VotingDetailsLog
        fields = "__all__"