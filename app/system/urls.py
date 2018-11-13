from django.urls import path

from . import views

app_name = 'system'

urlpatterns = [
    path('settings/', views.SystemSettingsAPIView.as_view(), name='settings'),
]
