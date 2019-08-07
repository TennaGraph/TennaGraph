# Pip imports
from rest_framework import generics
from rest_framework import permissions
from rest_framework import serializers
from django.db.models import Subquery

# App imports
from ..serializers import EIPSerializer
from ..models import EIP
from base import date_utils
from ethereum_client.models import VotingDetailsLog


def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

class EIPsAPIView(generics.ListAPIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = EIPSerializer
    queryset = EIP.objects.all()

    def get_queryset(self):
        """
        Optionally restricts the returned eips to a gived filters,
        by filtering against a `updated_at` query parameter in the URL.
        """
        queryset = self.queryset
        updated_after_timestamp = self.request.query_params.get('updated_after_timestamp', None)
        if updated_after_timestamp is not None:
            try:
                updated_at = date_utils.utcfromtimestamp(int(updated_after_timestamp))
                queryset = queryset.filter(updated_at__gt=updated_at)
            except Exception as err:
                raise serializers.ValidationError("Parameter `updated_after_timestamp` must be in the timestamp format (10 digits). Error: {}".format(err))

        is_voting_enabled = self.request.query_params.get('is_voting_enabled', None)
        if is_voting_enabled is not None:
            is_voting_enabled = str2bool(is_voting_enabled)
            queryset = queryset.filter(voting_details__isnull=False)\
                .filter(voting_details__in=Subquery(VotingDetailsLog.objects.filter(is_voting_open=is_voting_enabled).values('pk')))

        return queryset.all()
