# Django imports
from django.contrib import admin

# App imports
from .models import Stance


@admin.register(Stance)
class TransferSettingsAdmin(admin.ModelAdmin):
    list_display = ('author',)
