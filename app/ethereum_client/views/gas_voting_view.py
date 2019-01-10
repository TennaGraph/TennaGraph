# Stdlib imports
import logging

# Django imports
from django.db.models import Sum

# Pip imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

# App imports
from ..models import EthVoter
from ..models import VoteLog

logger = logging.getLogger(__name__)


@api_view(['GET'])
def gas_voting_view(request, proposal_id):
    vote_addresses = VoteLog.objects.filter(proposal_id=proposal_id).values_list('voter', flat=True)

    vote_addresses_yay = vote_addresses.filter(selected_option=VoteLog.YAY)
    vote_addresses_nay = vote_addresses.filter(selected_option=VoteLog.NAY)
    vote_addresses_abstain = vote_addresses.filter(selected_option=VoteLog.ABSTAIN)

    used_gas_yay = EthVoter.objects.filter(address__in=vote_addresses_yay).aggregate(Sum('used_gas'))["used_gas__sum"]
    used_gas_yay = 0 if not used_gas_yay else used_gas_yay

    used_gas_nay = EthVoter.objects.filter(address__in=vote_addresses_nay).aggregate(Sum('used_gas'))["used_gas__sum"]
    used_gas_nay = 0 if not used_gas_nay else used_gas_nay

    used_gas_abstain = EthVoter.objects.filter(address__in=vote_addresses_abstain).aggregate(Sum('used_gas'))["used_gas__sum"]
    used_gas_abstain = 0 if not used_gas_abstain else used_gas_abstain


    return Response({
        'yay': used_gas_yay,
        'nay': used_gas_nay,
        'abstain': used_gas_abstain,
    })