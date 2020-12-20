import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage,FlexSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_flex_message(reply_token, text, message):
    line_bot_api = LineBotApi(channel_access_token)
    message_to_reply = FlexSendMessage(text, message)
    line_bot_api.reply_message(reply_token, message_to_reply)

    return "OK"