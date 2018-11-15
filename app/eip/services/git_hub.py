# Stdlib imports
import base64

# Django imports
from django.conf import settings

# Pip imports
from github import Github

# App imports
from ..models import EIP
from ..utils import parse_eip_details


class GitHubEIP:

    gh = None

    def __init__(self):
        self.gh = Github(settings.GITHUB_USERNAME, settings.GITHUB_PASSWORD)

    def repo(self):
        return self.gh.get_repo("ethereum/EIPs")

    def content_of_dir(self, path=""):
        return self.repo().get_contents(path)

    def eips_list(self):
        return self.content_of_dir('/EIPS')

    def load_eip(self, content_eip_file):
        b64_content = content_eip_file.content

        file_name = content_eip_file.name
        file_download_url = content_eip_file.download_url
        file_sha = content_eip_file.sha
        file_content = base64.b64decode(b64_content).decode('utf-8')

        eip, title, status, eip_type, category, authors, created = parse_eip_details(file_content)

        eip_dict = {
            'eip_num':      eip,
            'eip_title':    title,
            'eip_status':   status,
            'eip_type':     eip_type,
            'eip_category': category,
            'eip_authors':  authors,
            'eip_created':  created,

            'file_name':            file_name,
            'file_download_url':    file_download_url,
            'file_content':         file_content,
            'file_sha':             file_sha,
        }

        return EIP(**eip_dict)





