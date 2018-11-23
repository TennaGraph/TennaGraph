# Django imports
from django.db import models

class SystemSettings(models.Model):
    is_maintenance = models.BooleanField(default=False)
    support_email = models.EmailField(default="test@gmail.com")

    last_update_influencers = models.DateTimeField(null=True, blank=True)
