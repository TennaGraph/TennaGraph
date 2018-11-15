# Pip imports
from rest_framework import serializers

# App imports
from ..models import EIP


class EIPSerializer(serializers.ModelSerializer):

    class Meta:
        model = EIP
        fields = "__all__"