import websocket
import json
from configparser import ConfigParser
import urls

# Temporary variables
server_name = "localhost"
event_code = "test1"


def create_config_file():
    """Creates a configuration file when one does not exist"""


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
        "ws://" + server_name + urls.event_stream_url(event_code),
        on_message=on_message,
        on_error=on_error,
        on_close=on_close)
    ws_test.run_forever()
# End websocket code


if __name__ == "__main__":
    websocket_test()
