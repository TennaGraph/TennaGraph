# Stdlib imports
import logging
from datetime import timedelta

# Django imports
from django.utils import timezone

# Pip imports
from celery import task

# App imports
from .models import Stance

# Project imports
from twitter_client.utils import weather_is_twitter_link
from twitter_client.utils import get_twitter_status_id
from twitter_client.services import TwitterClient


logger = logging.getLogger(__name__)


@task()
def check_availability_proofs_of_stances():
    """
    :return:
    """

    # Returns all TWITTER Stances which were checked more than one day ago
    yesterday = timezone.now() - timedelta(days=1)
    stances = Stance.objects.filter(proof_type=Stance.TWITTER).exclude(proof_last_check__gt=yesterday).all()

    if len(stances) == 0:
        return

    tw = TwitterClient()

    for stance in stances:

        # check weather the proof link was changed through admin panel to incorrect link
        if not weather_is_twitter_link(stance.proof_url):
            stance.proof_type = Stance.OTHER
            stance.proof_last_check = timezone.now()
            stance.save()
            continue

        # if the stance is not exists => remove it
        status_id = get_twitter_status_id(stance.proof_url)
        if not tw.is_status_exists(status_id):
            stance.delete()
            continue

        stance.proof_last_check = timezone.now()
        stance.save()











