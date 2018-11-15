from django.urls import path

from . import views

app_name = 'eip'

urlpatterns = [
    path('', views.EIPAPIView.as_view(), name='eip'),
]
