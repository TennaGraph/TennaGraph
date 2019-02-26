# Pip imports
from rest_framework import generics
from rest_framework import permissions

# App imports
from ..serializers import EIPSerializer
from ..models import EIP


class EIPAPIView(generics.RetrieveAPIView):

    lookup_field = 'eip_num'
    permission_classes = [permissions.AllowAny]
    serializer_class = EIPSerializer
    queryset = EIP.objects.all()