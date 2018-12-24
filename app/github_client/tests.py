# Stdlib imports
from decimal import Decimal

# Pip imports
from rest_framework.test import APITestCase

# Project imports
from stance.models import Stance
from eip.models import EIP
from influencer.models import Influencer

# App imports
from .services import GitHubDB



class GitHubClientTestCase(APITestCase):

    gh = None

    def setUp(self):
        self.gh = GitHubDB()

        eip_dict = {
            'eip_num': '12',
            'eip_title': 'Title of EIP',
            'eip_status': EIP.ACTIVE,
            'eip_type': EIP.INFORMATIONAL,
            'eip_category': EIP.ERC,
            'eip_authors': 'Authors here',
            'eip_created': '1994-12-23',

            'file_name': 'File name here',
            'file_download_url': 'https://google.com.ua/',
            'file_content': 'Here markdown text from md file',
            'file_sha': '0xjsfidsfseuiui34893hbsfo2i2ifeg',
        }
        eip2_dict = {
            'eip_num': '8',
            'eip_title': 'Title of EIP 2',
            'eip_status': EIP.ACTIVE,
            'eip_type': EIP.INFORMATIONAL,
            'eip_category': EIP.ERC,
            'eip_authors': 'Authors here 2',
            'eip_created': '1994-02-06',

            'file_name': 'File name here 2',
            'file_download_url': 'https://google.com.ua/2/',
            'file_content': 'Here markdown text from md file 2',
            'file_sha': '0xjsfidsfseuiui34893hbsfo2i2ifeg2',
        }
        self.eip = EIP.objects.create(**eip_dict)
        self.eip2 = EIP.objects.create(**eip2_dict)


        influencer = {
            'twitter_id':       '12345',
            'score':            Decimal('123.452435400000000000'),
            'name':             'The best influencer on myself =)',
            'screen_name':      'malkevych',
            'friends_count':    124987,
            'followers_count':  3456,
        }
        self.influencer = Influencer.objects.create(**influencer)


        stance_dict = {
            'author': 'malkevych',
            'proof_url': 'https://google.com',
            'choice': Stance.YAY,
            'eip': self.eip
        }
        self.stance_dict = stance_dict

        # Clear repo before run tests
        self.gh.delete_repo_content()

    def test_should_not_model_exists_on_repo(self):
        stance = Stance.objects.create(**self.stance_dict)

        is_exists = self.gh.is_model_exists(stance)

        self.assertFalse(is_exists)

    def test_should_create_right_stance_file_path(self):
        stance = Stance.objects.create(**self.stance_dict)

        file_path = self.gh.get_file_path(stance)

        self.assertEqual(file_path, 'stances/1.json')

    def test_should_write_stance_to_repo_as_file(self):
        stance = Stance.objects.create(**self.stance_dict)

        self.gh.create(stance)

        is_exists = self.gh.is_model_exists(stance)
        self.assertTrue(is_exists)

    def test_should_update_stance_to_repo_as_file(self):
        stance = Stance.objects.create(**self.stance_dict)

        self.gh.create(stance)
        json = self.gh.get_json_content(stance)
        json_from_repo = self.gh.get_json_content_from_repo(stance)
        self.assertEqual(json, json_from_repo)

        stance.status = Stance.APPROVED
        stance.save()

        self.gh.update(stance)

        json_updated = self.gh.get_json_content(stance)
        json_from_repo_updated = self.gh.get_json_content_from_repo(stance)

        self.assertEqual(json_updated, json_from_repo_updated)
        self.assertNotEqual(json, json_updated)





