# Stdlib imports
import pytz

# Django imports
from django.utils.timezone import datetime as datetime_z


def utcfromtimestamp(t):
    utc = pytz.utc
    return datetime_z.utcfromtimestamp(t).replace(tzinfo=utc)