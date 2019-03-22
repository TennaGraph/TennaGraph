# Django imports
from django.db import transaction

# Pip imports
from rest_framework import serializers
from github.GithubException import GithubException

# Project imports
from base.utils import ChoiceDisplayField
from influencer.models import Influencer
from influencer.serializers import InfluencerSerializer
from twitter_client.utils import weather_is_twitter_link
from github_client.services import GitHubDB
from eip.models import EIP

# App imports
from ..models import Stance


class StanceSerializer(serializers.ModelSerializer):

    choice = ChoiceDisplayField(Stance.CHOICES)

    status = ChoiceDisplayField(Stance.STATUSES, read_only=True)

    eip_num = serializers.IntegerField(write_only=True)

    influencer = InfluencerSerializer(read_only=True, required=False)

    class Meta:
        model = Stance
        fields = ['id', 'author', 'proof_url', 'choice', 'status', 'eip_num', 'influencer', 'created_at']
        write_only_fields = ['eip_num']

    """
    Validators
    """

    @transaction.atomic
    def create(self, validated_data):
        stance = Stance.objects.create(**validated_data)
        gh_db = GitHubDB()

        try:
            gh_db.create(stance, "An user of platform")
        except GithubException as ex:
            raise serializers.ValidationError("{}".format(ex.data.get('message')))

        return stance

    def validate_author(self, author):
        return author.replace('@', '')

    def validate(self, attrs):
        author_twitter_username = attrs.get('author')
        proof_url = attrs.get('proof_url', None)
        eip_num = attrs.pop('eip_num', None)
        if Stance.objects.filter(eip__eip_num=eip_num, proof_url=proof_url).exists():
            raise serializers.ValidationError("This url already submitted")

        influencers = Influencer.objects.filter(screen_name__icontains=author_twitter_username)
        if influencers.exists():
            attrs['influencer'] = influencers.first()

        if weather_is_twitter_link(attrs['proof_url']):
            attrs['proof_type'] = Stance.TWITTER

        try:
            attrs["eip_id"] = EIP.objects.get(eip_num=str(eip_num)).id
        except EIP.DoesNotExist:
            raise serializers.ValidationError("EIP not found")

        return attrs

