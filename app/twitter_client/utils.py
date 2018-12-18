# Stdlib imports
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


def weather_is_twitter_link(link):
    """
    Example: https://twitter.com/bomalkevych/status/1074683558084706305

    returns weather link is Twitter link to status
    :param link: (str)
    :return: (Boolean)
    """

    if not 'twitter.com/' in link or not '/status/' in link:
        return False

    path = urlparse.urlparse(link).path
    parts = path.split('/')
    parts = list(filter(lambda x: x != '', parts))

    try:
        int(parts[-1])
    except Exception:
        return False

    if not 'status' in parts[-2]:
        return False

    return True


def get_twitter_status_id(link):
    """
    Parse Twitter status url and returns it
    :param link:
    :return: (str)
    """
    assert weather_is_twitter_link(link), 'It is not twitter URL'

    path = urlparse.urlparse(link).path
    parts = path.split('/')
    parts = list(filter(lambda x: x != '', parts))

    return parts[-1]

