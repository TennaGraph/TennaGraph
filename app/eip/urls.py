from django.urls import path

from . import views

app_name = 'eip'

urlpatterns = [
    path('', views.EIPsAPIView.as_view(), name='eip'),
    path('<str:eip_num>/', views.EIPAPIView.as_view(), name='eip_retrieve')
]
