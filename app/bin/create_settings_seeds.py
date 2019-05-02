from system.models import SystemSettings
from stance.models import Stance

#CREATE SITE SETTINGS
def create_system_settings():
    # Workaround to avoid SystemSettings undefined
    import os
    from system.models import SystemSettings

    voting_address = os.environ.get('VOTING_MANAGER_CONTRACT_ADDRESS')

    seed_info = {
        'contract_vot_manager_address': voting_address
    }

    SystemSettings.objects.create(**seed_info)
    print("Site settings seed created")


def update_system_settings():
    # Workaround to avoid SystemSettings undefined
    import os
    from system.models import SystemSettings

    voting_address = os.environ.get('VOTING_MANAGER_CONTRACT_ADDRESS')
    settings = SystemSettings.objects.first()

    settings.contract_vot_manager_address = voting_address
    settings.save()

    print("Site settings updated")


if SystemSettings.objects.count() == 0:
    create_system_settings()
else:
    update_system_settings()


# def import_stances_from_git_hub():
#     from github_client.services import GitHubDB
#     gh = GitHubDB()
#     gh.retrive_from_github(default_eip_num=1057)
#
#
# if Stance.objects.count() == 0:
#     import_stances_from_git_hub()
