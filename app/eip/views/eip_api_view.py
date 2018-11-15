# Pip imports
from rest_framework import generics
from rest_framework import permissions

# App imports
from ..serializers import EIPSerializer
from ..models import EIP


class EIPAPIView(generics.ListAPIView):

    serializer_class = EIPSerializer
    permission_classes = [permissions.AllowAny]
    queryset = EIP.objects.all()