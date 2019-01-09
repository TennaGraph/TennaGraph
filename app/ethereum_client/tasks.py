# Stdlib imports
import logging
import operator
from functools import reduce

# Pip imports
from celery import task

# App imports
from .services import BlocksCoutClient
from .services import EthereumClient
from .models import EthVoter
from .models import VotingDetailsLog
from .models import VoteLog
from .contracts import VotingManagerContract

# Project imports
from eip.models import EIP


logger = logging.getLogger(__name__)


@task()
def fetch_transactions_info():
    """
    See details of params and limitations
    https://blockscout.com/eth/rinkeby/api_docs

    :return:
    """
    const_blocks = 20
    max_transactions_per_request = 1000

    eth_client = EthereumClient()
    blocks_count = eth_client.blocks_count()

    voters = EthVoter.objects.filter(last_block__lte=blocks_count-const_blocks)

    if voters.count() == 0:
        return

    bc_client = BlocksCoutClient()

    for voter in voters:
        from_block = ++voter.last_block

        is_need_load_more = True
        while is_need_load_more:
            transactions = bc_client.load_transactions(voter.address, from_block)

            # get last transaction
            last_tx = transactions[-1]
            is_need_load_more = len(transactions) >= max_transactions_per_request

            transactions_gas = list(map(lambda tx: int(tx.get('gasUsed')), transactions))
            transactions_gas = reduce(operator.add, transactions_gas)

            voter.append_used_gas(transactions_gas, last_tx)
            voter.save()


@task()
def load_voting_details_logs():
    """
    This worker loads all events about modified proposals to know which proposals
    are in active voting phase
    :return:
    """
    eth_client = EthereumClient()
    voting_manager = VotingManagerContract(client=eth_client)
    from_log = VotingDetailsLog.objects.order_by('block_number').last()
    from_block = 0 if not from_log else from_log.block_number + 1

    logs = voting_manager.load_voting_details_logs(from_block=from_block)
    logs = list(map(lambda l: VotingDetailsLog.objects.create(**l), logs))

    [l.save() for l in logs]

    cache = {}
    for log in logs:
        eip_num = str(log.proposal_id)

        try:
            if not cache.get(eip_num) or cache.get(eip_num) < log.block_number:
                eip = EIP.objects.get(eip_num=eip_num)
                cache[eip_num] = log.block_number
                if not eip.voting_details or eip.voting_details.block_number < log.block_number:
                    eip.voting_details = log
                    eip.save()

        except EIP.DoesNotExist:
            logger.error("Can't update EIP, the EIP with id: {} does not exists".format(eip_num))


@task()
def load_votes():
    """
    Loads all votes to know which addresses took part in coinvoting
    :return:
    """
    eth_client = EthereumClient()
    voting_manager = VotingManagerContract(client=eth_client)
    from_log = VoteLog.objects.order_by('block_number').last()
    from_block = 0 if not from_log else from_log.block_number + 1

    logs = voting_manager.load_votes_logs(from_block=from_block)
    logs = list(map(lambda l: VoteLog.objects.create(**l), logs))

    for log in logs:
        log.save()
        if not EthVoter.objects.filter(address=log.voter).exists():
            EthVoter.objects.create(address=log.voter)
