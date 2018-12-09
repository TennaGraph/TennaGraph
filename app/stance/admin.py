# Django imports
from django.contrib import admin

# App imports
from .models import Stance


@admin.register(Stance)
class StanceAdmin(admin.ModelAdmin):
    list_display = ('author',)
    list_filter = ('status', 'choice')