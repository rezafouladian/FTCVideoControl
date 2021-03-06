"""
Module containing functions to generate API URLs

All functions require a hostname, some also require the event code
"""

import settings

settings.load_config()
# Temporary fix to prevent errors
if settings.check_section('scorekeeper'):
    use_ssl = settings.get_value('scorekeeper', 'use_ssl')


def reload_config():
    settings.load_config()
    # Temporary fix to prevent errors
    if settings.check_section('scorekeeper'):
        use_ssl = settings.get_value('scorekeeper', 'use_ssl')


def url_start(hostname):
    """Add http:// or https:// and a trailing backslash to the server name"""

    if use_ssl:
        return "https://" + hostname + "/"
    else:
        return "http://" + hostname + "/"


def ws_url_start(hostname):
    """Add ws:// and a trailing backslash to the server name"""

    return "ws://" + hostname + "/"


# API URLs
def event_get_all_url(hostname):
    """A list of all event codes that this instance of the FTCLive
    server knows about.

    {
      "eventCodes": [
        "string"
      ]
    }
    """

    return url_start(hostname) + "/api/v1/events/"


def event_get_url(hostname, code):
    """A detailed description of an event for any given event code.

    Example output:

    {
      "eventCode": "string",
      "division": 0,
      "finals": true,
      "name": "string",
      "start": 0,
      "end": 0,
      "type": "string",
      "status": "string"
    }
    """

    return url_start(hostname) + "/api/v1/events/" + code + "/"


def get_elims(hostname, code):
    """Returns an array of matches that have been played in eliminations."""

    return url_start(hostname) + "/api/v1/events/" + code + "/elim/all/"


def get_quals(hostname, code):
    """The Qualification match list for a given event.

    If matchmaker has not been run when this is requested the match list
    will be empty.
    """

    return url_start(hostname) + "/api/v1/events/" + code + "/matches/"


def get_active_matches(hostname, code):
    """List of matches currently loaded for play."""

    return url_start(hostname) + "/api/v1/events/" + code + "/matches/active/"


def get_qual_info(hostname, code, match):
    """Results for a match that has been played.

    NO_SUCH_MATCH indicates either an invalid match number or
    the match has not been played yet."""

    return url_start(hostname) + "/api/v1/events/" + code + "/matches/" \
        + match + "/"


def event_awards_url(hostname, code):
    return url_start(hostname) + "/api/v2/events/" + code + "/awards/"


def event_full_details_url(hostname, code):
    return url_start(hostname) + "/api/v2/events/" + code + "/full/"


def event_stream_url(hostname, code):
    """Connects a websocket to listen for match events.

    Events come as messages on the socket in near-real-time to when they occur.
    Each event has a timestamp in milliseconds.

    Notable events are MATCH_LOAD, MATCH_START, MATCH_COMMIT, MATCH_POST,
    and MATCH_ABORT.

    Example output:

    {
      "updateTime": "0",
      "updateType": "string",
      "payload": {
        "number": 0,
        "shortName": "string",
        "field": 0
      }
    }
    """

    return ws_url_start(hostname) + "/api/v2/stream/?code=" + code
