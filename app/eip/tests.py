# Pip imports
from rest_framework.test import APITestCase

# App imports
from .services import GitHubEIP



class EIPsClientAPITestCase(APITestCase):

    gh = None


    def setUp(self):
        self.gh = GitHubEIP()

    def test_load_eips_repo(self):
        repo = self.gh.repo()
        print("REPO name: {}".format(repo.name))
        print("REPO archived: {}".format(repo.archived))
        print("REPO git_url: {}".format(repo.git_url))
        print("REPO url: {}".format(repo.url))
        print("REPO blobs_url: {}".format(repo.blobs_url))
        print("REPO contents_url: {}".format(repo.contents_url))

        self.assertFalse(repo.archived, "Repo suppose to be unsupported")

    def test_should_root_consist_folders(self):
        contents = self.gh.content_of_dir()

        EIPS_folder_exist = False
        assets_folder_exist = False

        for content_file in contents:
            if content_file.name == "EIPS":
                EIPS_folder_exist = True

            if content_file.name == "assets":
                assets_folder_exist = True

        self.assertTrue(EIPS_folder_exist, "No folder with all EIPs")
        self.assertTrue(assets_folder_exist, "No folder with all assets")

    def test_should_exist_eips_in_eip_folder(self):
        eips_content = self.gh.eips_content()

        self.assertTrue(isinstance(eips_content, list))
        self.assertGreater(len(eips_content), 0)




