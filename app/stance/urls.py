from django.urls import path

from . import views

app_name = 'stance'

urlpatterns = [
    path('', views.StancesAPIView.as_view(), name='stance'),
    path('<str:pk>/', views.StanceAPIView.as_view(), name='stance_retrieve')
]
