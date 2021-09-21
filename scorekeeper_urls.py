# API URLs
event_get_all_url = "/api/v1/events/"


def event_get_url(code): return "/api/v1/events/" + code + "/"


def event_awards_url(code): return "/api/v2/events/" + code + "/awards/"


def event_full_details_url(code): return "/api/v2/events/" + code + "/full/"


def event_stream_url(code): return "/api/v2/stream/?code=" + code
