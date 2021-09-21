import json
import os
from configparser import ConfigParser

import websocket

import scorekeeper_urls

config = ConfigParser()

# Global variables
hostname = ""
event_code = ""


def write_config():
    config.write(open('config.ini', 'w'))


def initialize_sections():
    """Initilize the config file with default values"""

    config.set('scorekeeper', 'hostname', 'localhost')
    config.set('scorekeeper', 'event_code', 'none')

    write_config()


def create_config_file():
    """Creates a configuration file when one does not exist and
    initializes it with default values.
    """

    config.add_section('scorekeeper')

    # TODO Move these to modules
    # config.add_section('atem')
    # config.add_section('tricaster')
    # config.add_section('obs')
    # config.add_section('xsplit')

    write_config()
    initialize_sections()


def load_config():
    global hostname
    global event_code

    config.read('config.ini')

    hostname = config.get('scorekeeper', 'hostname')
    event_code = config.get('scorekeeper', 'event_code')


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
    if not os.path.exists('config.ini'):
        create_config_file()
    else:
        config.read('config.ini')
        if not config.has_section('scorekeeper'):
            initialize_sections()
        load_config()

    websocket_test()
