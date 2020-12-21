import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

#create img folder
img_folder_path = "./img"
try:
    os.mkdir(img_folder_path)
except OSError:
    print ("Creation of the directory %s failed" % img_folder_path)

machine = TocMachine(
    states=["user", "start", "index", "search", "USA_index", "index_search", "index_chart"],
    transitions=[
        {"trigger": "advance","source": "user","dest": "start","conditions": "is_going_to_start"},
        {"trigger": "advance","source": "start","dest": "index","conditions": "is_going_to_index"},
        {"trigger": "advance","source": "index","dest": "start","conditions": "is_going_to_start"},
        {"trigger": "advance","source": "index","dest": "USA_index","conditions": "is_going_to_USA_index"},
        {"trigger": "advance","source": "USA_index","dest": "index_search","conditions": "is_going_to_index_search"},
        {"trigger": "advance","source": "index","dest": "index_search","conditions": "is_going_to_index_search"},
        {"trigger": "advance","source": "index_search","dest": "index_chart","conditions": "is_going_to_index_chart"},
        {"trigger": "advance","source": "index_search","dest": "index","conditions": "is_going_to_index"},
        {"trigger": "advance","source": "index_chart","dest": "index_search","conditions": "is_going_to_index_search"},
        {"trigger": "advance","source": "index_chart","dest": "start","conditions": "is_going_to_start"},



        {
            "trigger": "advance",
            "source": "start",
            "dest": "search",
            "conditions": "is_going_to_search",
        },
        {"trigger": "go_back", "source": ["state1", "state2"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        
        response = machine.advance(event)
        print(machine.state)
        if response == False:
            send_text_message(event.reply_token, "請依照指示與按鈕來操作!")

    return "OK"

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)