"""tennagraph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    path('', include('django_prometheus.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Change simple admin link to another without word admin
    path('admin/', admin.site.urls),

    path('system/', include('system.urls', namespace='system')),
    path('eip/', include('eip.urls', namespace='eip')),
    path('stance/', include('stance.urls', namespace='stance')),
    path('influencer/', include('influencer.urls', namespace='influencer')),
    path('ethereum/', include('ethereum_client.urls', namespace='ethereum_client')),
]

