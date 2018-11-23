# Django imports
from django.conf import settings

# Pip imports
import requests
import iso8601

# App imports
from ..models import Influencer


HIVE_ONE_API_URL = settings.HIVE_ONE_API_URL


class HiveOne:

    hive_one_api_url = None

    def __init__(self, hive_one_api_url=HIVE_ONE_API_URL):
        self.hive_one_api_url = hive_one_api_url

    def load_influencers(self, network='eth'):
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

        headers = {'Content-Type': 'application/json'}
        url = "{}/lists/{}".format(self.hive_one_api_url, network)
        r = requests.get(url, headers=headers)
        response_raw = r.json()
        if "error" in response_raw:
            raise Exception(response_raw["error"]["message"])

        influencers_raw = response_raw["influencersData"]
        influencers = [Influencer.create(influencer_raw) for influencer_raw in influencers_raw]

        ranked_at = iso8601.parse_date(response_raw["rankedAt"])

        return influencers, ranked_at