# Stdlib imports
import pytz
import datetime

# Django imports
from django.utils.timezone import datetime as datetime_z


def utcfromtimestamp(t):
    utc = pytz.utc
    return datetime_z.utcfromtimestamp(t).replace(tzinfo=utc)

def utc_from_nem_timestamp(nem_stamp):
    utc = pytz.utc
    nem_epoch = datetime.datetime(2015, 3, 29, 0, 6, 25, 0, utc)
    return nem_epoch + datetime.timedelta(seconds=nem_stamp)