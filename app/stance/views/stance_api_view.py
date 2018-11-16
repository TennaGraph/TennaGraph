# Pip imports
from rest_framework import generics
from rest_framework import permissions

# App imports
from ..serializers import StanceSerializer
from ..models import Stance


class StanceAPIView(generics.RetrieveAPIView):

    lookup_field = 'pk'
    permission_classes = [permissions.AllowAny]
    serializer_class = StanceSerializer
    queryset = Stance.objects.all()