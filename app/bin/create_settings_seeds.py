# SITE SETTINGS
def create_system_settings():
    # Workaround to avoid SystemSettings undefined
    from system.models import SystemSettings

    SystemSettings.objects.create()
    print("Site settings seed created")


def create_system_settings_if_needed():
    from system.models import SystemSettings

    if SystemSettings.objects.count() == 0:
        create_system_settings()
    else:
        print("Site settings already exists")


create_system_settings_if_needed()