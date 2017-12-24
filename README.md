# Bittrex_LineBot

## これは何か
LINEメッセージからBittrexの取引を行うためのソースコードです。


## 動作環境
- aws Lamda(python 2.7)
    - 必要権限:  AWSLambdaFullAccessのみ
- API gatewayよりアクセスを想定

## 導入
1. パッケージを任意のフォルダに展開
2. `pip install -r requirements.txt -t <展開したフォルダのフルパス>`
3. configフォルダ内の2ファイルを編集
4. zipに圧縮しLambdaへアップロードする
5. API gateway越しに叩く