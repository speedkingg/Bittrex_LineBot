# -*- coding: utf-8 -*-


from line_utils.line_utils import line_utils # lineでメッセージを送る
from bittrex_utils.bittrex_private import bittrex_private  # bittrexの個人情報を扱う
from bittrex_utils.bittrex_public import bittrex_public  # bittrexの公開情報を扱う
from define.common_define import COMMON_DEFINE
from define.message_define import MessageDefine

# lineメッセージを受け取って起動する
class reply():
    def __init__(self):
        self.line_utils = line_utils()
        self.bittrex_private = bittrex_private()
        self.bittrex_public = bittrex_public()


    # フォーマットをメッセージにして返す
    def match_keyword_help(self,reply_token):
        # 定義からメッセージを読み込む
        reply_message = MessageDefine.HELP_MESSAGE

        # lineメッセージを返す
        self.line_utils.line_reply(reply_token, reply_message=reply_message)


    # 所有しているコイン一覧をメッセージにして返す
    def match_keyword_wallet(self,reply_token):
        # 定義からメッセージを読み込む
        reply_message = MessageDefine.OWNED_COIN_SUMMARY_MESSAGE + "\n\n"
        # 所有している通貨リストを取得する
        balance_list = self.bittrex_private.get_balances()

        # 所有しているコイン一覧を1行ずつメッセージに追記する
        for item in balance_list:
            reply_message += str(item['currency']) + ": " + str(item['available']) + "\n"

        # lineメッセージを返す
        self.line_utils.line_reply(reply_token,reply_message=reply_message)


    # 指定したコインを買う
    # line_message = "買い <通貨略称> <btc量>"
    def match_keyword_buy(self,reply_token, line_message):
        # 受け取ったlineメッセージを要素に分解する
        line_message_list = line_message.split()
        market_name = line_message_list[1]
        btc_quantity = line_message_list[2]

        # 通貨ペアをBTCにする
        currency_pair = COMMON_DEFINE.PREFIX_BTC + market_name

        # 最小取引量取得
        min_trade_size = self.bittrex_public.get_min_trade_size(market_name)

        # 終値取得
        alt_last_price = self.bittrex_public.get_last_price(currency_pair)

        #注文量計算
        order_quantity = float(btc_quantity)/alt_last_price

        # 最小取引量に合わせる
        order_quantity = int(order_quantity/min_trade_size)*min_trade_size

        # アルトコインを購入し、取引IDを受け取る
        uuid = self.bittrex_private.buy_alt_coin(market=currency_pair ,
                                                 quantity=order_quantity,
                                                 rate=alt_last_price)
        # メッセージ作成
        # 取引失敗の場合
        if uuid is False:
            reply_message = MessageDefine.FAILED_TRADE_MESSAGE

        # 取引成功でトレードが完了している場合
        elif uuid == "":
            reply_message = MessageDefine.APPLY_FOR_PURCHASE_MESSAGE + "\n\n" \
                            + currency_pair + ": " + str(btc_quantity) + COMMON_DEFINE.CURRENCY_UNIT_BTC

        # 取引成功でトレードが完了していない場合
        else:
            reply_message = MessageDefine.APPLY_FOR_PURCHASE_MESSAGE + "\n\n" \
                            + currency_pair + ": " + str(btc_quantity) + COMMON_DEFINE.CURRENCY_UNIT_BTC\
                            + "\n" + MessageDefine.TRADE_ID + " : " + uuid

        # lineメッセージを返す
        self.line_utils.line_reply(reply_token, reply_message=reply_message)



    # 指定したコインを売る
    # line_message = "売り <通貨略称> <alt_coin量>"
    def match_keyword_sell(self,reply_token, line_message):
        # 受け取ったlineメッセージを要素に分解する
        line_message_list = line_message.split()
        market_name = line_message_list[1]
        alt_quantity = line_message_list[2]

        # 通貨ペアをBTCにする
        currency_pair = COMMON_DEFINE.PREFIX_BTC + market_name

        # 最小取引量取得
        min_trade_size = self.bittrex_public.get_min_trade_size(market_name)

        # 終値取得
        alt_last_price = self.bittrex_public.get_last_price(currency_pair)

        # 最小取引量に合わせる
        order_quantity = int(float(alt_quantity) / min_trade_size) * min_trade_size

        # アルトコインを購入し、取引IDを受け取る
        uuid = self.bittrex_private.sell_alt_coin(market=currency_pair ,
                                                 quantity=order_quantity,
                                                 rate=alt_last_price)
        # メッセージ作成
        # 取引失敗の場合
        if uuid is False:
            reply_message = MessageDefine.FAILED_TRADE_MESSAGE

        # 取引成功でトレードが完了している場合
        elif uuid == "":
            reply_message = MessageDefine.APPLY_FOR_PURCHASE_MESSAGE + "\n\n" \
                            + currency_pair + ": " + str(alt_quantity) + market_name.lower()

        # 取引成功でトレードが完了していない場合
        else:
            reply_message = MessageDefine.APPLY_FOR_PURCHASE_MESSAGE + "\n\n" \
                            + currency_pair + ": " + str(alt_quantity) + market_name.lower()\
                            + "\n" + MessageDefine.TRADE_ID + " : " + uuid

        # lineメッセージを返す
        self.line_utils.line_reply(reply_token, reply_message=reply_message)


    # 取引中の注文一覧をメッセージにして返す
    def match_keyword_orders_list(self,reply_token):
        order_list = self.bittrex_private.get_orders()

        if order_list is None:
            reply_message = MessageDefine.NO_ORDER_MESSAGE

        else:
            reply_message = MessageDefine.ORDER_LIST_MESSAGE + "\n\n"
            # 所有しているコイン一覧を1行ずつメッセージに詰める
            for item in order_list:
                reply_message += str(item['market']) + ": " + str(item['quantity']) + "\n"\
                                 + "取引ID: " + str(item['uuid']) + "\n\n"

        # lineメッセージを返す
        self.line_utils.line_reply(reply_token,reply_message=reply_message)


    # 取引中の注文一覧をメッセージにして返す
    # line_message = "キャンセル <取引ID>"
    def match_keyword_cancel(self, reply_token, line_message):
        line_message_list = line_message.split()
        uuid = line_message_list[1]

        # 注文が存在するか確認
        order_list = self.bittrex_private.get_orders()
        if order_list is None:
            reply_message = MessageDefine.NO_ORDER_MESSAGE
            # lineメッセージを返す
            self.line_utils.line_reply(reply_token, reply_message=reply_message)


        else:
            # 注文をキャンセルする
            response = self.bittrex_private.order_cancel(uuid)
            if response:
                reply_message = MessageDefine.CANCEL_MESSAGE
            else:
                reply_message = MessageDefine.FAILED_CANCEL_MESSAGE

            reply_message += "\n" + MessageDefine.TRADE_ID + " : " + uuid

            # lineメッセージを返す
            self.line_utils.line_reply(reply_token, reply_message=reply_message)
