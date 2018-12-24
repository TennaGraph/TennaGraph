# Django imports
from django.db import models
from abc import abstractmethod


class GitHubCompatible(models.Model):

    class Meta:
        abstract = True

    @abstractmethod
    def git_options(self):
        """
        In inherited method we must return fields below

        :return: {
            'folder': 'name_of_folder',
            'serializer': 'django_rest_framework_serializer'
        }
        """
        pass