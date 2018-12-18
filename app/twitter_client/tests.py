# Pip imports
from rest_framework.test import APITestCase
import twitter

# App imports
from .services import TwitterClient
from .utils import weather_is_twitter_link
from .utils import get_twitter_status_id


class TwitterClientAPITestCase(APITestCase):

    twitter = None

    def setUp(self):
        self.twitter = TwitterClient()

    def test_verification(self):
        result = self.twitter.verification()

        self.assertTrue(isinstance(result, twitter.models.User))

    def test_should_load_status(self):
        status_id = "956851653776322565"
        status = self.twitter.load_status(status_id)

        self.assertTrue(isinstance(status, twitter.models.Status))
        # print("Status: {}, tupe {}".format(status, type(status)))

    def test_should_return_status_code_144(self):
        status_id = "1074683558084706305"
        try:
            self.twitter.load_status(status_id)
        except twitter.error.TwitterError as ex:
            status_code = ex.message[0].get('code')
            self.assertEqual(status_code, 144)

    def test_should_status_exists(self):
        status_id = "956851653776322565"

        is_status_exists = self.twitter.is_status_exists(status_id)

        self.assertTrue(is_status_exists)

    def test_should_status_exists(self):
        status_id = "1074683558084706305"

        is_status_exists = self.twitter.is_status_exists(status_id)

        self.assertFalse(is_status_exists)


class TwitterUtilsTestCase(APITestCase):

    def test_should_be_twitter_link(self):
        link = 'https://twitter.com/bomalkevych/status/1074683558084706305'
        is_twitter_link = weather_is_twitter_link(link)

        self.assertTrue(is_twitter_link)

    def test_should_be_twitter_link_2(self):
        link = 'https://twitter.com/bomalkevych/status/1074683558084706305/'
        is_twitter_link = weather_is_twitter_link(link)

        self.assertTrue(is_twitter_link)

    def test_should_not_be_twitter_link(self):
        link = 'https://twitter.com/bomalkevych/post/1074683558084706305/'
        is_twitter_link = weather_is_twitter_link(link)

        self.assertFalse(is_twitter_link)

    def test_should_not_be_twitter_link(self):
        link = 'https://twitter.com/bomalkevych/status/status/'
        is_twitter_link = weather_is_twitter_link(link)

        self.assertFalse(is_twitter_link)

    def test_should_return_status_id_from_twitter_link(self):
        link = 'https://twitter.com/bomalkevych/status/1074683558084706305'
        status_id = get_twitter_status_id(link)

        self.assertEqual(status_id, '1074683558084706305')

    def test_should_return_status_id_from_twitter_link_2(self):
        link = 'http://twitter.com/bomalkevych/status/333/'
        status_id = get_twitter_status_id(link)

        self.assertEqual(status_id, '333')






