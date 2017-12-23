# -*- coding: utf-8 -*-

import json  # jsonを使用するため
from pprint import pprint  # 表示用(jsonをきれいに表示してくれる)
from bittrex import Bittrex  # Bittrexで取引するためのAPI

# 設定ファイル読み込み--------------
bittrex_keys_json = open('config/bittrex_keys.json', 'r')
bittrex_keys = json.load(bittrex_keys_json)

KEY = bittrex_keys["key"]  # アクセスキー読み込み
SECRET = bittrex_keys["secret"]  # シークレットキー読み込み
# -------------------------------

class bittrex_private:
    def __init__(self):
        # self.bittrex_public = Bittrex(None, None)  # 公開情報を扱うBittrexオブジェクト
        self.bittrex_private = Bittrex(KEY, SECRET)  # 個人の情報を扱うBittrexオブジェクト

    # トレード履歴を取得
    def get_order_history(self):
        response = self.bittrex_private.get_order_history()
        pprint(response)
        return response

    # 買い注文を出す
    # marketに通貨ペア、quantityに注文する量、rateに価格を指定
    def buy_alt_coin(self, market, quantity, rate):
        response = self.bittrex_private.buy_limit(market=market, quantity=quantity, rate=rate)
        # 成功なら注文id、失敗ならfalseを返す
        if response['success'] is False:
            print(response)
            return False
        else:
            return response['result']['uuid']

    # 売り注文を出す
    # marketに通貨ペア、quantityに注文する量、rateに価格を指定
    def sell_alt_coin(self, market, quantity, rate):
        response = self.bittrex_private.sell_limit(market=market, quantity=quantity, rate=rate)
        # 成功なら注文id、失敗ならfalseを返す
        if response['success'] is False:
            print(response)
            return False
        else:
            return response['result']['uuid']

    # 注文をキャンセルする
    def order_cancel(self, uuid):
        response = self.bittrex_private.cancel(uuid=uuid)
        # 成功ならtrue、失敗ならfalseを返す
        print(response)
        return response['success']

    # 注文一覧を取得する
    def get_orders(self):
        order_list = []
        response = self.bittrex_private.get_open_orders()
        if response['success'] is False:
            print(response)
            return False
        else:
            # 注文が１件もない場合
            if len(response['result']) == 0:
                return None

            for item in response['result']:
                # 通貨の種類と量、注文IDを抜き出す
                balance = {}
                balance['market'] = item['Exchange']
                balance['quantity'] = item['Quantity']
                balance['uuid'] = item['OrderUuid']
                order_list.append(balance)

        return order_list

    # 所有している通貨をList型で返す
    def get_balances(self):
        balance_list = []
        response = self.bittrex_private.get_balances()
        if response['success'] is False:
            print(response)
            return False
        else:
            for item in response['result']:
                # 利用可能な通貨量が0の場合はスキップする
                if item['Available'] == 0:
                    continue
                # 通貨の種類と量を抜き出す
                balance = {}
                balance['currency'] = item['Currency']
                balance['available'] = item['Available']
                balance_list.append(balance)

        return balance_list














