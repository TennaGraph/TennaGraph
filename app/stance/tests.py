# Pip imports
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

# Project imports
from eip.models import EIP

# App imports
from .models import Stance



class StancesClientAPITestCase(APITestCase):

    eip = None

    def setUp(self):
        eip_dict = {
            'eip_num': '12',
            'eip_title': 'Title of EIP',
            'eip_status': EIP.ACTIVE,
            'eip_type': EIP.INFORMATIONAL,
            'eip_category': EIP.ERC,
            'eip_authors': 'Authors here',
            'eip_created': '12.33.2344',

            'file_name': 'File name here',
            'file_download_url': 'https://google.com.ua/',
            'file_content': 'Here markdown text from md file',
            'file_sha': '0xjsfidsfseuiui34893hbsfo2i2ifeg',
        }
        self.eip = EIP.objects.create(**eip_dict)

    def test_should_return_empty_list_of_stances(self):
        url = reverse("stance:stance")
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_should_return_list_of_stances(self):
        stance_dict = {
            'author': '@author',
            'proof_url': 'https://google.com',
            'choice': Stance.YAY,
            'eip': self.eip
        }
        Stance.objects.create(**stance_dict)

        url = reverse("stance:stance")
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        stance_response = response.data[0]

        self.assertEqual(stance_response['author'],         stance_dict['author'])
        self.assertEqual(stance_response['proof_url'],       stance_dict['proof_url'])
        self.assertEqual(stance_response['choice']['key'],  stance_dict['choice'])
        self.assertEqual(stance_response['status']['key'],  'PENDING')


    def test_should_retrieve_the_stance(self):
        stance_dict = {
            'author': '@author',
            'proof_url': 'https://google.com',
            'choice': Stance.YAY,
            'eip': self.eip
        }
        stance = Stance.objects.create(**stance_dict)

        url = reverse("stance:stance_retrieve", kwargs={'pk': stance.id})

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, dict))

        stance_response = response.data

        self.assertEqual(stance_response['author'],         stance_dict['author'])
        self.assertEqual(stance_response['proof_url'],      stance_dict['proof_url'])
        self.assertEqual(stance_response['choice']['key'],  stance_dict['choice'])
        self.assertEqual(stance_response['status']['key'],  'PENDING')

    def test_should_create_new_stance(self):
        stance_dict = {
            'author': '@author',
            'proof_url': 'https://google.com',
            'choice': Stance.YAY,
            'eip_id': self.eip.id,
        }

        url = reverse("stance:stance")
        response = self.client.post(url, data=stance_dict, format='json')

        print("RESPONSE: {}".format(response.data))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(isinstance(response.data, dict))

        stance_response = response.data

        self.assertEqual(stance_response['author'],         stance_dict['author'])
        self.assertEqual(stance_response['proof_url'],      stance_dict['proof_url'])
        self.assertEqual(stance_response['choice']['key'],  stance_dict['choice'])
        self.assertEqual(stance_response['status']['key'],  'PENDING')
