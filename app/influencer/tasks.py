# Stdlib imports
import logging
from decimal import Decimal

# Django imports
from django.db import transaction

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

    gh = HiveOne()
    influencers, ranked_at = gh.load_influencers()

    """ If we have already actual information about influencers we skip it """
    last_ranked_at = system_settings.last_update_influencers
    if last_ranked_at and last_ranked_at == last_ranked_at:
        return

    system_settings.last_update_influencers = ranked_at
    system_settings.save()

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





