# Django imports
from django.conf import settings

# Pip imports
import requests



class RequestMaker(object):

    base_url = None

    def __init__(self, base_url=settings.BLOCKSCOUT_BASE_URL):
        self.base_url = base_url

    def get(self, payload):
        headers = {'Content-Type': 'application/json'}
        r = requests.get(self.base_url, params=payload, headers=headers)
        response_raw = r.json()

        if not response_raw.get('status') == '1':
            raise Exception(response_raw.get('message'))

        return response_raw.get('result')


class BlocksCoutClient(object):

    request_maker = None

    def __init__(self, request_maker=RequestMaker()):
        self.request_maker = request_maker

    def load_transactions(self, address, start_block, end_block=None):
        """
        Loads transactions for specific address

        :param address:
        :param start_block:
        :param end_block:
        :return:
        """
        payload = {
            'module': 'account',
            'action': 'txlist',
            'address': address,
            'startblock': start_block,
        }
        if end_block:
            payload['endblock'] = end_block

        return self.request_maker.get(payload)

