# Django imports
from django.contrib import admin

# App imports
from .models import Influencer


@admin.register(Influencer)
class InfluencerAdmin(admin.ModelAdmin):
    list_display = ('name',)
