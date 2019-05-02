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

    def load_influencers(self, network='ETH', offset=0):
        """
        Old version of response
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


        New version of response
        {
          "data": {
            "people": {
              "edges": [
                {
                  "node": {
                    "id": 295218901,
                    "rank": 1,
                    "name": "Vitalik Non-giver of Ether",
                    "screenName": "VitalikButerin",
                    "imageUrl": "https://pbs.twimg.com/profile_images/977496875887558661/L86xyLF4.jpg",
                    "score": 915.448484715576,
                    "following": 135,
                    "followers": 852157,
                    "changeWeek": 0.6222103482880357
                  }
                },
                ...
                ],
              "cursor": {
                "after": 20,
                "hasNextCursor": true
              }
            }
          }
        }

        """

        headers = {'Content-Type': 'application/json'}
        url = "{}/influencers/people/{}/{}/".format(self.hive_one_api_url, network, offset)
        r = requests.get(url, headers=headers)
        response_raw = r.json()
        if "error" in response_raw:
            raise Exception(response_raw["error"]["message"])

        people = response_raw.get("data").get("people")
        edges = people.get("edges")
        cursor = people.get("cursor")
        influencers = [Influencer.create(node.get("node")) for node in edges]

        # ranked_at = iso8601.parse_date(response_raw["rankedAt"])

        return influencers, cursor