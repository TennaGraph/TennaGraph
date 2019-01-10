from django.urls import path

from . import views

app_name = 'ethereum_client'

urlpatterns = [
    path('gas-voting/<str:proposal_id>/', views.gas_voting_view, name='gas_voting')
]
