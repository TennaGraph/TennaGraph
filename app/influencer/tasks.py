# Stdlib imports
import logging

# Django imports
from django.db import transaction

# Pip imports
from celery import task

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

    """
    {
      "rankedAt": "2018-11-22T01:53:23.395793+00:00",
      "influencersData": [
        {
          "twitterId": "295218901",
          "score": 909.108104040976,
          "name": "Vitalik Non-giver of Ether",
          "screenName": "VitalikButerin",
          "friendsCount": 163,
          "followersCount": 822257,
          "clusters": [
            {
              "abbr": "BCH",
              "display": "Bitcoin Cash",
              "score": 676.747951670349
            }
          ],
          "changeWeek": -0.028517707088099087,
          "changeMonth": -3.587503012500065
        },
        ....
      ]
    }
    
    """
    gh = HiveOne()
    influencers = gh.load_influencers()

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





