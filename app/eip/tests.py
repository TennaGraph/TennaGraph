# Stdlib imports
from datetime import date

# Pip imports
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

# Project imports
from ethereum_client.models import VotingDetailsLog

# App imports
from github_client.services import GitHubEIP
from github_client.utils import parse_eip_details
from .models import EIP
from .tasks import fetch_eips_from_official_repo


class EIPsUnitTestCase(APITestCase):

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
        eips_list = self.gh.eips_list()

        self.assertTrue(isinstance(eips_list, list))
        self.assertGreater(len(eips_list), 0)

        content_file = eips_list[0]

        # print("CONTENT_FILE html_url: {}".format(content_file.html_url))
        # print("CONTENT_FILE git_url: {}".format(content_file.git_url))
        # print("CONTENT_FILE download_url: {}".format(content_file.download_url))
        # print("CONTENT_FILE name: {}".format(content_file.name))
        # print("CONTENT_FILE url: {}".format(content_file.url))
        # print("CONTENT_FILE content: {}".format(content_file.content))

        self.assertIsNotNone(content_file)

    def test_should_parse_eip_details(self):
        content = "--- \n" \
                  "eip: 1 \n" \
                  "title: EIP Purpose and Guidelines \n" \
                  "status: Active \n" \
                  "type: Meta \n" \
                  "author: Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, and others \n" \
                  "created: 2015-10-27\n" \
                  "--- \n"

        eip, title, status, eip_type, category, authors, created_raw, created, content = parse_eip_details(content)

        self.assertIsNone(category)
        self.assertEqual(eip, "1")
        self.assertEqual(title, "EIP Purpose and Guidelines")
        self.assertEqual(status, EIP.ACTIVE)
        self.assertEqual(eip_type, EIP.META)
        self.assertEqual(authors, "Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, and others")
        self.assertEqual(created_raw, "2015-10-27")
        self.assertTrue(isinstance(created, date))


    def test_should_parse_eip_details_status_final(self):
        content = "--- \n" \
                  "eip: 1 \n" \
                  "title: EIP Purpose and Guidelines \n" \
                  "status: Final \n" \
                  "type: Meta \n" \
                  "author: Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, and others \n" \
                  "created: 2015-10-27\n" \
                  "--- \n"

        eip, title, status, eip_type, category, authors, created_raw, created, content = parse_eip_details(content)

        self.assertIsNone(category)
        self.assertEqual(eip, "1")
        self.assertEqual(title, "EIP Purpose and Guidelines")
        self.assertEqual(status, EIP.FINAL)
        self.assertEqual(eip_type, EIP.META)
        self.assertEqual(authors, "Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, and others")
        self.assertEqual(created_raw, "2015-10-27")
        self.assertTrue(isinstance(created, date))


    def test_should_parse_eip_details_standards_track(self):
        content = "--- \n" \
                  "eip: 1 \n" \
                  "title: EIP Purpose and Guidelines \n" \
                  "status: Active \n" \
                  "type: Standards Track \n" \
                  "author: Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, and others \n" \
                  "created: 2015-10-27, 2017-02-01 \n" \
                  "--- \n"

        eip, title, status, eip_type, category, authors, created_raw, created, content = parse_eip_details(content)

        self.assertIsNone(category)
        self.assertEqual(eip, "1")
        self.assertEqual(title, "EIP Purpose and Guidelines")
        self.assertEqual(status, EIP.ACTIVE)
        self.assertEqual(eip_type, EIP.STANDARDS_TRACK)
        self.assertEqual(authors, "Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, and others")
        self.assertEqual(created_raw, '2015-10-27, 2017-02-01')

        print("eip {}, title {}, status {}, eip_type {}, category {}, authors {}, created {}".format(eip, title, status, eip_type, category, authors, created))


    def test_should_parse_eip_details_with_other_category(self):
        content = "--- \n" \
                  "eip: 1 \n" \
                  "title: EIP Purpose and Guidelines \n" \
                  "status: draft \n" \
                  "type: Something wrong \n" \
                  "author: Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, and others \n" \
                  "created: 2015-10-27, 2017-02-01 \n" \
                  "--- \n"

        eip, title, status, eip_type, category, authors, created_raw, created, content = parse_eip_details(content)

        self.assertIsNone(category)
        self.assertEqual(eip, "1")
        self.assertEqual(title, "EIP Purpose and Guidelines")
        self.assertEqual(status, EIP.DRAFT)
        self.assertEqual(eip_type, EIP.OTHER)
        self.assertEqual(authors, "Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, and others")
        self.assertEqual(created_raw, "2015-10-27, 2017-02-01")

    def test_should_load_and_store_first_eip(self):
        eips_list = self.gh.eips_list()
        content_file = eips_list[0]
        self.assertEqual(EIP.objects.count(), 0)

        eip = self.gh.load_eip(content_file)

        self.assertEqual(EIP.objects.count(), 0)
        eip.save()

        self.assertEqual(EIP.objects.count(), 1)
        self.assertIsNotNone(eip.file_sha)
        self.assertIsNone(eip.eip_category)
        self.assertEqual(eip.eip_num, "1")
        self.assertEqual(eip.eip_title, "EIP Purpose and Guidelines")
        self.assertEqual(eip.eip_status, EIP.ACTIVE)
        self.assertEqual(eip.eip_type, EIP.META)
        self.assertEqual(eip.eip_authors, "Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, and others")
        self.assertNotEqual(eip.eip_created, None)

    def test_sould_fetch_eips_from_official_repo(self):
        self.assertEqual(EIP.objects.count(), 0)

        fetch_eips_from_official_repo()

        self.assertGreater(EIP.objects.count(), 0)


class EIPsClientAPITestCase(APITestCase):

    def test_should_return_empty_list_of_eips(self):
        url = reverse("eip:eip")
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_should_return_list_of_eips(self):
        voting_details_log = {
            "proposal_id": 12,
            "is_voting_open": True,
            "block_number": 900000,
        }
        VotingDetailsLog.objects.create(**voting_details_log)

        eip_dict = {
            'eip_num': '12',
            'eip_title': 'Title of EIP',
            'eip_status': EIP.ACTIVE,
            'eip_type': EIP.INFORMATIONAL,
            'eip_category': EIP.ERC,
            'eip_authors': 'Authors here',
            'eip_created': '2015-10-27',

            'file_name': 'File name here',
            'file_download_url': 'https://google.com.ua/',
            'file_content': 'Here markdown text from md file',
            'file_sha': '0xjsfidsfseuiui34893hbsfo2i2ifeg',
        }
        EIP.objects.create(**eip_dict)

        url = reverse("eip:eip")
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        eip_response = response.data[0]

        self.assertEqual(eip_response['eip_num'],               eip_dict['eip_num'])
        self.assertEqual(eip_response['eip_title'],             eip_dict['eip_title'])
        self.assertEqual(eip_response['eip_status']['key'],     eip_dict['eip_status'])
        self.assertEqual(eip_response['eip_type']['key'],       eip_dict['eip_type'])
        self.assertEqual(eip_response['eip_category']['key'],   eip_dict['eip_category'])
        self.assertEqual(eip_response['eip_authors'],           eip_dict['eip_authors'])
        self.assertEqual(eip_response['eip_created'],           eip_dict['eip_created'])
        self.assertEqual(eip_response['file_name'],             eip_dict['file_name'])
        self.assertEqual(eip_response['file_download_url'],     eip_dict['file_download_url'])
        self.assertEqual(eip_response['file_content'],          eip_dict['file_content'])
        self.assertEqual(eip_response['file_sha'],              eip_dict['file_sha'])

        # Voting details log
        self.assertEqual(eip_response['voting_details']['proposal_id'], voting_details_log['proposal_id'])
        self.assertEqual(eip_response['voting_details']['is_voting_open'], voting_details_log['is_voting_open'])
        self.assertEqual(eip_response['voting_details']['block_number'], voting_details_log['block_number'])
        self.assertIsNotNone(eip_response['voting_details']['created_at'])
        self.assertIsNotNone(eip_response['voting_details']['updated_at'])

    def test_should_retrieve_the_eip(self):
        eip_dict = {
            'eip_num': '12',
            'eip_title': 'Title of EIP',
            'eip_status': EIP.ACTIVE,
            'eip_type': EIP.INFORMATIONAL,
            'eip_category': EIP.ERC,
            'eip_authors': 'Authors here',
            'eip_created': '2015-10-27',
            'eip_created_raw': '2015-10-27',

            'file_name': 'File name here',
            'file_download_url': 'https://google.com.ua/',
            'file_content': 'Here markdown text from md file',
            'file_sha': '0xjsfidsfseuiui34893hbsfo2i2ifeg',
        }
        eip = EIP.objects.create(**eip_dict)

        url = reverse("eip:eip_retrieve", kwargs={'pk': eip.id})

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, dict))

        eip_response = response.data

        print("::::::::::: eip_response {}".format(eip_response))

        self.assertEqual(eip_response['eip_num'],               eip_dict['eip_num'])
        self.assertEqual(eip_response['eip_title'],             eip_dict['eip_title'])
        self.assertEqual(eip_response['eip_status']['key'],     eip_dict['eip_status'])
        self.assertEqual(eip_response['eip_type']['key'],       eip_dict['eip_type'])
        self.assertEqual(eip_response['eip_category']['key'],   eip_dict['eip_category'])
        self.assertEqual(eip_response['eip_authors'],           eip_dict['eip_authors'])
        self.assertEqual(eip_response['eip_created_raw'],       eip_dict['eip_created'])
        self.assertEqual(eip_response['file_name'],             eip_dict['file_name'])
        self.assertEqual(eip_response['file_download_url'],     eip_dict['file_download_url'])
        self.assertEqual(eip_response['file_content'],          eip_dict['file_content'])
        self.assertEqual(eip_response['file_sha'],              eip_dict['file_sha'])
