# Stdlib imports
import logging
from decimal import Decimal
from datetime import timedelta

# Django imports
from django.db import transaction
from django.utils import timezone

# Pip imports
from celery import task

# Project imports
from system.models import SystemSettings

# App imports
from .services import HiveOne
from .models import Influencer


logger = logging.getLogger(__name__)


@task()
def fetch_influencers_from_hive_one():
    """
    API: GET https://hive.one/api/lists/eth

    :return:
    """

    system_settings = SystemSettings.objects.first()
    if not system_settings:
        logger.critical("No SystemSettings in db")

    """ If we have already actual information about influencers we skip it """
    last_update_influencers = system_settings.last_update_influencers
    yesterday = timezone.now() - timedelta(days=1)
    if last_update_influencers and last_update_influencers > yesterday:
        return

    ho = HiveOne()
    influencers = []
    max_influencers = 480
    cursor = {"after": 0, "hasNextCursor": True}

    while len(influencers) < max_influencers and cursor.get("hasNextCursor"):
        batch_influencers, cursor = ho.load_influencers(offset=cursor.get("after"))

        current_len = len(influencers)
        if current_len + len(batch_influencers) <= max_influencers:
            influencers = influencers + batch_influencers
        else:
            influencers = influencers + batch_influencers[:(current_len + len(batch_influencers) - max_influencers)]

    Influencer.objects.update(score=Decimal('0'))

    for influencer in influencers:
        influencer_twitter_id = influencer.twitter_id

        try:
            # Check weather this EIP exists in out db. If exists then update fields
            if not Influencer.objects.filter(twitter_id=influencer_twitter_id).exists():
                influencer.save()
            else:
                influencer_to_update = Influencer.objects.filter(twitter_id=influencer_twitter_id).first()
                influencer_to_update.update_with_influencer(influencer).save()
        except Exception as ex:
            logger.error(
                "Can't save Influencer with twitter ID: '{}', error occurred: '{}'".format(influencer_twitter_id, ex))

    system_settings.last_update_influencers = timezone.now()
    system_settings.save()




