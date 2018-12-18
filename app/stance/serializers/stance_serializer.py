# Pip imports
from rest_framework import serializers

# Project imports
from base.utils import ChoiceDisplayField
from influencer.models import Influencer
from influencer.serializers import InfluencerSerializer
from twitter_client.utils import weather_is_twitter_link

# App imports
from ..models import Stance


class StanceSerializer(serializers.ModelSerializer):

    choice = ChoiceDisplayField(Stance.CHOICES)

    status = ChoiceDisplayField(Stance.STATUSES, read_only=True)

    eip_id = serializers.IntegerField(write_only=True)

    influencer = InfluencerSerializer(read_only=True, required=False)

    class Meta:
        model = Stance
        fields = ['id', 'author', 'proof_url', 'choice', 'status', 'eip_id', 'influencer', 'created_at']

    """
    Validators
    """

    def validate_author(self, author):
        return author.replace('@', '')

    def validate(self, attrs):
        author_twitter_username = attrs.get('author')
        proof_url = attrs.get('proof_url', None)
        eip_id = attrs.get('eip_id', None)
        if Stance.objects.filter(eip_id=eip_id, proof_url=proof_url).exists():
            raise serializers.ValidationError("This url already submitted")

        influencers = Influencer.objects.filter(screen_name__icontains=author_twitter_username)
        if influencers.exists():
            attrs['influencer'] = influencers.first()

        if weather_is_twitter_link(attrs['proof_url']):
            attrs['proof_type'] = Stance.TWITTER

        return attrs

