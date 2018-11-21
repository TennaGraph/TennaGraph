# Pip imports
from rest_framework import generics
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend

# App imports
from ..serializers import StanceSerializer
from ..models import Stance


class StancesAPIView(generics.ListCreateAPIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = StanceSerializer
    queryset = Stance.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('eip_id',)


