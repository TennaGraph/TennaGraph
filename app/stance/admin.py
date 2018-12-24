# Django imports
from django.contrib import admin
from django.db import transaction

# Project imports
from github_client.services import GitHubDB

# App imports
from .models import Stance


@admin.register(Stance)
class StanceAdmin(admin.ModelAdmin):
    list_display = ('author',)
    list_filter = ('status', 'choice')


    @transaction.atomic()
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        gh = GitHubDB()
        if change and gh.is_model_exists(obj):
            gh.update(obj)
        else:
            gh.create(obj)

    def delete_model(self, request, obj):
        gh = GitHubDB()
        if gh.is_model_exists(obj):
            gh.delete(obj)

        super().delete_model(request, obj)
