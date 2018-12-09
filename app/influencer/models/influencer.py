# Django imports
from django.db import models

# Project imports
from base.models import TimeStampedModel


class Influencer(TimeStampedModel):

    twitter_id          = models.CharField(max_length=20, unique=True)
    score               = models.DecimalField(decimal_places=18, max_digits=30)
    name                = models.CharField(max_length=255)

    # Twitter login
    screen_name         = models.CharField(max_length=100)
    friends_count       = models.IntegerField()
    followers_count     = models.IntegerField()


    def __str__(self):
        return "{}, {}, score: {}".format(self.name, self.screen_name, self.score)

    @classmethod
    def create(cls, influencer_raw):
        influencer = cls(twitter_id=influencer_raw['twitterId'],
                         score=influencer_raw['score'],
                         name=influencer_raw['name'],
                         screen_name=influencer_raw['screenName'],
                         friends_count=influencer_raw['friendsCount'],
                         followers_count=influencer_raw['followersCount'])
        return influencer

    def update_with_influencer(self, influencer):
        self.score              = influencer
        self.name               = influencer
        self.screen_name        = influencer
        self.friends_count      = influencer
        self.followers_count    = influencer

        return self


