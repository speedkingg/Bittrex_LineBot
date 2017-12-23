# -*- coding: utf-8 -*-

from bittrex import Bittrex  # Bittrexで取引するためのAPI

class bittrex_public:

    def __init__(self):
        self.bittrex_public = Bittrex(None, None)  # 公開情報を扱うBittrexオブジェクト

    # 取引可能通貨サマリ一覧をList型で返す
    def get_coin_summery_list(self):
        coin_summery_list = []
        response = self.bittrex_public.get_markets()

        for item in response['result']:
            coin_summery = str(item['MarketCurrencyLong'])
            coin_summery_list.append(coin_summery)

        return coin_summery_list

    # 通貨の最小取引単位取得
    def get_min_trade_size(self,market):
        response = self.bittrex_public.get_markets()
        for item in response['result']:
            if item['MarketCurrency'] == market:
                return item['MinTradeSize']

        return False

    # 通貨の終値取得
    def get_last_price(self,market):
        response = self.bittrex_public.get_marketsummary(market)
        return response['result'][0]['Last']