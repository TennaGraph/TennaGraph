from system.models import SystemSettings

# SITE SETTINGS
def create_system_settings():
    # Workaround to avoid SystemSettings undefined
    from system.models import SystemSettings

    seed_info = {
        'contract_vot_manager_address': '0xb662F0418fB5c501D9fbe437640C3856aCc14f56'
    }

    SystemSettings.objects.create(**seed_info)
    print("Site settings seed created")



if SystemSettings.objects.count() == 0:
    create_system_settings()
else:
    print("Site settings already exists")