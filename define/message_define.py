# -*- coding: utf-8 -*-

class MessageDefine:
    def __init__(self):
        pass

    # line_reply_key_word

    TRADE_ID = "取引ID"

    # line_reply_message

    # ヘルプメッセージ
    HELP_MESSAGE = "メッセージフォーマットだよ\n\n"\
                    + "[所有しているコイン一覧]\nkey_word: 所有、もってるやつ\n\n"\
                    + "[買い注文]\nformat: 買い <通貨略称> <btc量>\n\n"\
                    + "[売り注文]\nformat: 売り <通貨略称> <alt_coin量>\n\n" \
                    + "[キャンセル]\nformat: キャンセル<注文ID>\n\n" \
                    + "[注文一覧]\nkey_word: 注文一覧、オーダー一覧\n\n" \
                    + "[ヘルプを出す]\nkey_word: へるぷ"

    # 所有しているコイン一覧を返すときのメッセージ
    OWNED_COIN_SUMMARY_MESSAGE = "今所有しているコインの一覧だよ"

    # 処理に失敗した際に返すメッセージ
    FAILED_TRADE_MESSAGE = "取引に失敗しちゃった。。。"

    # コインの購入申請をしたときに返すメッセージ
    APPLY_FOR_PURCHASE_MESSAGE = "指定したコインを購入申請したよ"

    # 取引中の注文がないときに返すメッセージ
    NO_ORDER_MESSAGE = "取引中の注文はないよ"

    #  取引中の注文を返すメッセージ
    ORDER_LIST_MESSAGE = "取引中の注文一覧だよ"

    # 取引をキャンセルしたときに返すメッセージ
    CANCEL_MESSAGE = "取引をキャンセルしたよ"

    # 取引のキャンセルに失敗したときに返すメッセージ
    FAILED_CANCEL_MESSAGE = "取引のキャンセルに失敗しちゃった。。。"
