from __future__ import absolute_import, unicode_literals
import os
import logging
from celery import Celery
import logstash
from celery.signals import after_setup_task_logger
from celery.signals import after_setup_logger
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tennagraph.settings')

LOGSTASH_ENABLED = getattr(settings, 'LOGSTASH_ENABLED', None)
LOGSTASH_HOST = getattr(settings, 'LOGSTASH_HOST', None)
LOGSTASH_PORT = getattr(settings, 'LOGSTASH_PORT', None)


def initialize_logstash(logger=None, loglevel=logging.INFO, **kwargs):
    handler = logstash.TCPLogstashHandler(LOGSTASH_HOST, LOGSTASH_PORT, tags=['celery'], message_type='celery',
                                          version=1)
    handler.setLevel(loglevel)
    logger.addHandler(handler)
    return logger


if LOGSTASH_ENABLED:
    after_setup_task_logger.connect(initialize_logstash)
    after_setup_logger.connect(initialize_logstash)

app = Celery('signals')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(['eip', 'influencer', 'stance'])


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
