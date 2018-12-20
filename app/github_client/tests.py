# Stdlib imports
from datetime import date

# Pip imports
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

# App imports
from .services import GitHubEIP



class GitHubClientTestCase(APITestCase):

    gh = None


    def setUp(self):
        self.gh = GitHubEIP()
