"""
WSGI config for tennagraph project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tennagraph.settings")
GUNICORN_SERVE_STATIC = getattr(settings, 'GUNICORN_SERVE_STATIC', None)
if GUNICORN_SERVE_STATIC:
    application = StaticFilesHandler(get_wsgi_application())
else:
    application = get_wsgi_application()

