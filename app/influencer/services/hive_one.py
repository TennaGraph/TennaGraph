# Stdlib imports
import base64

# Django imports
from django.conf import settings

# Pip imports
import requests

# App imports
from ..models import Influencer


HIVE_ONE_API_URL = settings.HIVE_ONE_API_URL


class HiveOne:

    hive_one_api_url = None

    def __init__(self, hive_one_api_url=HIVE_ONE_API_URL):
        self.hive_one_api_url = hive_one_api_url

    def load_influencers(self, network='eth'):
        headers = {'Content-Type': 'application/json'}
        url = "{}/lists/{}".format(self.hive_one_api_url, network)
        r = requests.get(url, headers=headers)
        response_raw = r.json()
        if "error" in response_raw:
            raise Exception(response_raw["error"]["message"])

        influencers_raw = response_raw["influencersData"]
        influencers = [Influencer.create(influencer_raw) for influencer_raw in influencers_raw]

        return influencers