import websocket
import json

# Temporary variables
server_name = "localhost"
event_code = "test1"

# API URLs
event_get_all_url = "/api/v1/events/"


def event_get_url(code): return "/api/v1/events/" + code + "/"


def event_awards_url(code): return "/api/v2/events/" + code + "/awards/"


def event_full_details_url(code): return "/api/v2/events/" + code + "/full/"


def event_stream_url(code): return "/api/v2/stream/?code=" + code
# End API URLs


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
        "ws://" + server_name + event_stream_url(event_code),
        on_message=on_message,
        on_error=on_error,
        on_close=on_close)
    ws_test.run_forever()


if __name__ == "__main__":
    websocket_test()
