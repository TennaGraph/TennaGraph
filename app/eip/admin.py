# Django imports
from django.contrib import admin

# App imports
from .models import EIP


@admin.register(EIP)
class TransferSettingsAdmin(admin.ModelAdmin):
    list_display = ('file_name',)
