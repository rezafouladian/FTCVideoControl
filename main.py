import json

import websocket

import settings
import atem
import tricaster
import scorekeeper_urls

# TODO:
#  Rate Limiting


# Global variables
hostname = ""
event_code = ""

settings.load_config()


def initialize_sections():
    """Initilize the config file with default values"""

    settings.set_value('scorekeeper', 'hostname', 'localhost')
    settings.set_value('scorekeeper', 'event_code', 'none')
    settings.set_value('scorekeeper', 'use_ssl', 'false')

    settings.write_config()


def load_config():
    global hostname
    global event_code

    hostname = settings.get_value('scorekeeper', 'hostname')
    event_code = settings.get_value('scorekeeper', 'event_code')

    scorekeeper_urls.reload_config()


# Websocket code
def on_message(ws, message):
    update_type = json.loads(message)["updateType"]
    match_number = json.loads(message)["payload"]["number"]
    short_name = json.loads(message)["payload"]["shortName"]
    field_number = json.loads(message)["payload"]["field"]


def on_error(ws, error): print(error)


def on_close(ws): print("Socket Closed")


def websocket_test():
    websocket.enableTrace(True)
    ws_test = websocket.WebSocketApp(
        scorekeeper_urls.event_stream_url(hostname, event_code),
        on_message=on_message,
        on_error=on_error,
        on_close=on_close)
    ws_test.run_forever()
# End websocket code


if __name__ == "__main__":
    if not settings.check_section('scorekeeper'):
        initialize_sections()
    load_config()

    # websocket_test()
