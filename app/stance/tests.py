# Pip imports
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

# App imports
from .models import Stance



class StancesClientAPITestCase(APITestCase):

    def test_should_return_empty_list_of_stances(self):
        url = reverse("stance:stance")
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_should_return_list_of_stances(self):
        stance_dict = {
            'author': '@author',
            'post_url': 'https://google.com',
            'choice': Stance.YAY,
        }
        Stance.objects.create(**stance_dict)

        url = reverse("stance:stance")
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        stance_response = response.data[0]

        self.assertEqual(stance_response['author'],         stance_dict['author'])
        self.assertEqual(stance_response['post_url'],       stance_dict['post_url'])
        self.assertEqual(stance_response['choice']['key'],  stance_dict['choice'])
        self.assertEqual(stance_response['status']['key'],  'PENDING')


    def test_should_retrieve_the_stance(self):
        stance_dict = {
            'author': '@author',
            'post_url': 'https://google.com',
            'choice': Stance.YAY,
        }
        stance = Stance.objects.create(**stance_dict)

        url = reverse("stance:stance_retrieve", kwargs={'pk': stance.id})

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, dict))

        stance_response = response.data

        self.assertEqual(stance_response['author'],         stance_dict['author'])
        self.assertEqual(stance_response['post_url'],       stance_dict['post_url'])
        self.assertEqual(stance_response['choice']['key'],  stance_dict['choice'])
        self.assertEqual(stance_response['status']['key'],  'PENDING')

    def test_should_create_new_stance(self):
        stance_dict = {
            'author': '@author',
            'post_url': 'https://google.com',
            'choice': Stance.YAY,
        }

        url = reverse("stance:stance")

        response = self.client.post(url, data=stance_dict, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(isinstance(response.data, dict))

        stance_response = response.data

        self.assertEqual(stance_response['author'],         stance_dict['author'])
        self.assertEqual(stance_response['post_url'],       stance_dict['post_url'])
        self.assertEqual(stance_response['choice']['key'],  stance_dict['choice'])
        self.assertEqual(stance_response['status']['key'],  'PENDING')
