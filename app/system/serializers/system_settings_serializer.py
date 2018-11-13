# Pip imports
from rest_framework import serializers

# App imports
from ..models import SystemSettings


class SystemSettingsSerializer(serializers.ModelSerializer):


    class Meta(object):
        model = SystemSettings
        fields = "__all__"

    """
    Getters
    
    """
