# Stdlib imports
import logging

# Django imports
from django.db import transaction

# Pip imports
from celery import task

# App imports
from github_client.services import GitHubEIP
from .models import EIP


logger = logging.getLogger(__name__)


@task()
def fetch_eips_from_official_repo():
    """
    All EIPs stored in official repo: https://github.com/ethereum/EIPs/tree/master/EIPS

    :return:
    """
    gh = GitHubEIP()
    eips = gh.eips_list()

    for eip in eips:
        file_name = eip.name
        file_sha = eip.sha

        # Check weather this EIP exists in out db
        if not EIP.objects.filter(file_name=file_name).exists():
            try:
                with transaction.atomic():
                    gh.load_eip(eip).save()
            except Exception as ex:
                logger.error("Can't parse EIP with file name: '{}', error occurred: '{}'".format(file_name, ex))

        # check weather EIP was updated
        elif not EIP.objects.filter(file_name=file_name, file_sha=file_sha).exists():
            eip_to_update = EIP.objects.filter(file_name=file_name).first()
            eip_to_update.update_with_eip(gh.load_eip(eip)).save()





