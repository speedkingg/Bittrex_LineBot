# -*- coding: utf-8 -*-

from define.key_word_define import KeyWordDefine # キーワード定義情報一覧
from utils.reply import reply #受け取ったメッセージを処理し、LINEでリプライを行うクラス

reply = reply()

# lineメッセージを受け取って起動する
def lambda_handler(event, context):

    # debug
    print(event)
    print(event['body-json']['events'][0]['replyToken'])
    print(event['body-json']['events'][0]['message']['text'].encode('utf-8'))

    # lineイベントの取り出し
    line_event = event['body-json']['events'][0]

    # lineメッセージを返す用のトークン取得
    reply_token = line_event['replyToken']

    # 送られてきたlineメッセージ取り出し
    line_message = line_event['message']['text'].encode('utf-8')

    # [ヘルプ]のキーワードとマッチした場合
    for word in KeyWordDefine.HELP:
        if line_message.find(word) != -1:
            reply.match_keyword_help(reply_token)
            exit()

    # [所有している通貨一覧を取得する]のキーワードとマッチした場合
    for word in KeyWordDefine.WALLET:
        if line_message.find(word) != -1:
            reply.match_keyword_wallet(reply_token)
            exit()

    # [買い]のキーワードとマッチした場合
    for word in KeyWordDefine.ORDER_BUY:
        if line_message.find(word) != -1:
            reply.match_keyword_buy(reply_token, line_message)
            exit()

    # [売り]のキーワードとマッチした場合
    for word in KeyWordDefine.ORDER_SELL:
        if line_message.find(word) != -1:
            reply.match_keyword_sell(reply_token, line_message)
            exit()

    # [注文一覧]のキーワードとマッチした場合
    for word in KeyWordDefine.ORDERS_LIST:
        if line_message.find(word) != -1:
            reply.match_keyword_orders_list(reply_token)
            exit()

    # [キャンセル]のキーワードとマッチした場合
    for word in KeyWordDefine.ORDER_CANCEL:
        if line_message.find(word) != -1:
           reply.match_keyword_cancel(reply_token, line_message)
           exit()
