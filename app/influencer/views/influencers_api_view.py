# Pip imports
from rest_framework import generics
from rest_framework import permissions

# App imports
from ..serializers import InfluencerSerializer
from ..models import Influencer


class InfluencersAPIView(generics.ListAPIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = InfluencerSerializer
    queryset = Influencer.objects.order_by('-score').all()