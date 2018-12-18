# Stdlib
import logging

# Django imports
from django.conf import settings

# Pip imports
import twitter

logger = logging.getLogger(__name__)


class TwitterClient:

    api = None

    def __init__(self):
        self.api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
                                      consumer_secret=settings.TWITTER_CONSUMER_SECRET_KEY,
                                      access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
                                      access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET_KEY)

    def verification(self):
        return self.api.VerifyCredentials()

    def load_status(self, status_id):
        return self.api.GetStatus(status_id)

    def is_status_exists(self, status_id):
        """
        Returns True if status exists
        Returns False if status doesn't exist
        Returns None if An error was occurred

        :param status_id:
        :return: True / False / None
        """
        try:
            self.load_status(status_id)
            return True
        except twitter.error.TwitterError as ex:
            status_code = ex.message[0].get('code')
            if status_code == 144:
                return False

            logger.error("Can't load twit, TwitterError occurred: {}".format(ex))

        except Exception as ex:
            logger.error("Can't load twit, en error occurred: {}".format(ex))

        return None
