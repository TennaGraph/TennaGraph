# Stdlib imports
import logging
from datetime import timedelta

# Django imports
from django.utils import timezone
from django.db import transaction

# Pip imports
from celery import task
from github.GithubException import GithubException

# App imports
from .models import Stance

# Project imports
from twitter_client.utils import weather_is_twitter_link
from twitter_client.utils import get_twitter_status_id
from twitter_client.services import TwitterClient
from github_client.services import GitHubDB


logger = logging.getLogger(__name__)


@task()
def check_availability_proofs_of_stances():
    """
    :return:
    """

    # Returns all TWITTER Stances which were checked more than one day ago
    yesterday = timezone.now() - timedelta(days=1)
    stances = Stance.objects.filter(proof_type=Stance.TWITTER).exclude(proof_last_check__gt=yesterday).all()

    if len(stances) == 0:
        return

    tw = TwitterClient()
    gh = GitHubDB()

    for stance in stances:
        operation = 'update'
        try:
            with transaction.atomic():
                # check weather the proof link was changed through admin panel to incorrect link
                is_twitter_link = weather_is_twitter_link(stance.proof_url)
                if not is_twitter_link:
                    stance.proof_type = Stance.OTHER

                # if the stance is not exists => remove it
                elif not tw.is_status_exists(get_twitter_status_id(stance.proof_url)):
                    operation = 'delete'

                    # delete stance on git hub
                    if gh.is_model_exists(stance):
                        gh.delete(stance)

                    stance.delete()
                    continue

                stance.proof_last_check = timezone.now()
                stance.save()

                # update stance on git hub
                if gh.is_model_exists(stance):
                    gh.update(stance)
                else:
                    gh.create(stance)

        except GithubException as ex:
            logger.error("Can't {} Stance with id '{}', cause the error occurred: '{}'".format(operation, stance.id,
                                                                                               ex.data.get('message')))

        except Exception as ex:
            logger.error("Can't {} Stance with id '{}', cause the error occurred: '{}'".format(operation, stance.id, ex))
