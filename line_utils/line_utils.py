# -*- coding: utf-8 -*-

import json
from linebot.api import LineBotApi
from linebot.models import TextSendMessage


# 設定ファイル読み込み--------------
line_keys_json = open('config/line_keys.json', 'r')
line_keys = json.load(line_keys_json)

channel_access_token = line_keys["channel_access_token"]  # シークレットキー読み込み
# -------------------------------


class line_utils:
    def __init__(self):
        # Line返信用オブジェクト作成
        self.line_bot_api = LineBotApi(channel_access_token)

    def line_reply(self,reply_token, reply_message):
        self.line_bot_api.reply_message(reply_token, messages=TextSendMessage(reply_message))


