from system.models import SystemSettings

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