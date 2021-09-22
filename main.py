import json
import time

import websocket

import settings
import atem
import tricaster
import scorekeeper_urls

# TODO:
#  Rate Limiting

MATCH_LENGTH = 159

# Global variables
hostname = ""
event_code = ""

match_state = "none"
match_start_time = 0
match_number_current = 0
match_name_current = "none"
current_field = 1

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
    global match_start_time
    global match_state
    global match_number_current
    global match_name_current
    global current_field

    update_type = json.loads(message)["updateType"]
    match_number = json.loads(message)["payload"]["number"]
    short_name = json.loads(message)["payload"]["shortName"]
    field_number = json.loads(message)["payload"]["field"]

    if update_type == "MATCH_START":
        match_start_time = int(time.time())
        match_state = "started"
        match_number_current = match_number
        match_name_current = short_name
        current_field = field_number


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


def main_loop():
    global match_state

    if match_state == "started":
        # Check to see if the match time has elapsed
        if int(time.time()) > (match_start_time + MATCH_LENGTH):
            # TODO
            pass


if __name__ == "__main__":
    if not settings.check_section('scorekeeper'):
        initialize_sections()
    load_config()

    # websocket_test()
