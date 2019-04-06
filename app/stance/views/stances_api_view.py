# Pip imports
from rest_framework import generics
from rest_framework import permissions

# App imports
from ..serializers import StanceSerializer
from ..models import Stance


class StancesAPIView(generics.ListCreateAPIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = StanceSerializer
    queryset = Stance.objects.filter(status=Stance.APPROVED)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = self.queryset
        eip_num = self.request.query_params.get('eip_num', None)
        if eip_num is not None:
            queryset = self.queryset.filter(eip__eip_num=eip_num)
        return queryset.all()


