# Stdlib imports
import base64
import json

# Django imports
from django.conf import settings
from django.utils import timezone

# Pip imports
from github import Github
from github.GithubException import UnknownObjectException
from github import InputGitAuthor

# App imports



class GitHubDB:

    gh = None

    branch = settings.GITHUB_DB_BRANCH

    def __init__(self):
        self.gh = Github(settings.GITHUB_USERNAME, settings.GITHUB_PASSWORD)

    def repo(self):
        return self.gh.get_repo(settings.GITHUB_DB_REPO)

    def is_model_exists(self, model):
        """
        Returns weather the model is already stored in the github repo
        :param model:
        :return:
        """
        file_path = self.get_file_path(model)
        try:
            self.repo().get_contents(file_path, ref=self.branch)
            return True

        except UnknownObjectException as ex:
            if ex.status == 404:
                return False
            raise


    def create(self, model, author="Moderator"):
        """
        see details https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html?highlight=create_file

        :param model:
        :param author: The author of the commit
        :return:
        """
        file_path = self.get_file_path(model)
        json_content = self.get_json_content(model)

        self.repo().create_file(path=file_path,
                                message="Create new model ({})".format(type(model)),
                                content=json_content,
                                branch=self.branch,
                                author=self.construct_author(author))

    def update(self, model, author="Moderator"):
        """
        see details https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html?highlight=update_file

        :param model:
        :param author: The author of the commit
        :return:
        """
        file_path = self.get_file_path(model)
        json_content = self.get_json_content(model)
        contents = self.repo().get_contents(file_path, ref=self.branch)

        if base64.b64decode(contents.content).decode('utf-8') == json_content:
            return

        # repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")
        self.repo().update_file(path=file_path,
                                message="Updated model ({})".format(type(model)),
                                content=json_content,
                                sha=contents.sha,
                                branch=self.branch,
                                author=self.construct_author(author))

    def delete(self, model, author="Moderator"):
        """
        see details https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html?highlight=delete_file

        :param model:
        :param author: The author of the commit
        :return:
        """
        file_path = self.get_file_path(model)

        contents = self.repo().get_contents(file_path, ref=self.branch)

        self.repo().delete_file(path=contents.path,
                                message="Create new model ({})".format(type(model)),
                                sha=contents.sha,
                                branch=self.branch,
                                author=self.construct_author(author))

    def delete_repo_content(self, author="Moderator"):
        """
        Removes all files from test github repo. It is dangerous function, use only for TESTING purpose

        :param author: The author of the commit
        :return:
        """
        contents = self.repo().get_contents("", ref=self.branch)

        while len(contents) >= 1:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(self.repo().get_contents(file_content.path, ref=self.branch))
            else:
                self.repo().delete_file(path=file_content.path,
                                        message="Delete repo content ({})".format(type(file_content.path)),
                                        sha=file_content.sha,
                                        branch=self.branch,
                                        author=self.construct_author(author))

    def retrive_from_github(self, default_eip_num):
        import json
        from stance.models import Stance
        from influencer.models import Influencer
        from eip.models import EIP

        contents = self.repo().get_contents("", ref=self.branch)

        while len(contents) >= 1:
            print("LENGTH: {}".format(len(contents)))

            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(self.repo().get_contents(file_content.path, ref=self.branch))
            else:
                content = json.loads(base64.b64decode(file_content.content).decode('utf-8'))

                id_obj = content.get("id")
                author = content.get("author")
                author_from_social = content.get("author_from_social")
                proof_url = content.get("proof_url")
                choice = content.get("choice").get("key")
                status = content.get("status").get("key")
                influencer = content.get("influencer")
                created_at = content.get("created_at")

                eip_num = content.get("eip_num", default_eip_num)

                params = {
                    "id": id_obj,
                    "author": author,
                    "proof_url": proof_url,
                    "choice": choice,
                    "status": status,
                    "created_at": created_at,
                    "eip": EIP.objects.get(eip_num=eip_num)
                }

                if influencer:
                    try:
                        params["influencer"] = Influencer.objects.get(screen_name=influencer.get("screen_name"))
                    except Influencer.DoesNotExist:
                        print("Influencer no more exists: {}".format(params))

                if author_from_social:
                    params["author_from_social"] = author_from_social

                Stance.objects.create(**params)


    """
    Utils / Helpers
    """

    def get_file_path(self, model):
        """
        Generates path to file for specific model. Must implement abstract GitHubCompatible
        :param model:
        :return:
        """
        options = model.git_options()
        return '{}/{}.json'.format(options.get('folder'), model.id)

    def get_json_content(self, model):
        Serializer = model.git_options().get('serializer')
        return json.dumps(Serializer(instance=model).data)

    def get_json_content_from_repo(self, model):
        """

        :param model:
        :return:
        """
        file_path = self.get_file_path(model)
        contents = self.repo().get_contents(file_path, ref=self.branch)

        return base64.b64decode(contents.content).decode('utf-8')

    def construct_author(self, name, email='unknown@example.com', date=str(timezone.now())):
        return InputGitAuthor(name, email, date)







