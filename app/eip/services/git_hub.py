# Django imports
from django.conf import settings

# Pip imports
from github import Github


class GitHubEIP:

    gh = None

    def __init__(self):
        self.gh = Github(settings.GITHUB_USERNAME, settings.GITHUB_PASSWORD)

    def repo(self):
        return self.gh.get_repo("ethereum/EIPs")

    def content_of_dir(self, path=""):
        return self.repo().get_contents(path)

    def eips_content(self):
        return self.content_of_dir('/EIPS')


