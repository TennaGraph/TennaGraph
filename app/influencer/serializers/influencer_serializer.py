# Pip imports
from rest_framework import serializers

# App imports
from ..models import Influencer


class InfluencerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Influencer
        fields = "__all__"