"""
Module containing functions to generate API URLs

All functions require a hostname, some also require the event code
"""

import settings

settings.load_config()
use_ssl = settings.get_value('scorekeeper', 'use_ssl')


def reload_config():
    settings.load_config()


def http_url_start(hostname):
    """Add http:// and a trailing backslash to the server name"""

    return "http://" + hostname + "/"


def https_url_start(hostname):
    """Add https:// and a trailing backslash to the server name"""
    # TODO: SSL support

    return "https://" + hostname + "/"


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

    return http_url_start(hostname) + "/api/v1/events/"


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

    return http_url_start(hostname) + "/api/v1/events/" + code + "/"


def event_awards_url(hostname, code):
    return http_url_start(hostname) + "/api/v2/events/" + code + "/awards/"


def event_full_details_url(hostname, code):
    return http_url_start(hostname) + "/api/v2/events/" + code + "/full/"


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
