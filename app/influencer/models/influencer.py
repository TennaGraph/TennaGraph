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
    following_count     = models.IntegerField()
    followers_count     = models.IntegerField()
    image_url           = models.URLField(null=True, blank=True)


    def __str__(self):
        return "{}, {}, score: {}".format(self.name, self.screen_name, self.score)

    @classmethod
    def create(cls, influencer_raw):
        influencer = cls(twitter_id=influencer_raw['id'],
                         score=influencer_raw['score'],
                         name=influencer_raw['name'],
                         screen_name=influencer_raw['screenName'],
                         image_url=influencer_raw['imageUrl'],
                         following_count=influencer_raw['following'],
                         followers_count=influencer_raw['followers'])
        return influencer

    def update_with_influencer(self, influencer):
        self.score              = influencer.score
        self.name               = influencer.name
        self.screen_name        = influencer.screen_name
        self.imageUrl           = influencer.imageUrl
        self.following_count    = influencer.following_count
        self.followers_count    = influencer.followers_count

        return self


