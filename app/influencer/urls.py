from django.urls import path

from . import views

app_name = 'influencer'

urlpatterns = [
    path('', views.InfluencersAPIView.as_view(), name='influencer'),
]
