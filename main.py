##youtube 「Pythonでtwitterのbotを作ろう」いまにゅじゃないので書き方違うかも
#pip install tweepyしておく
#ryota_twibot のPJで実装
import tweepy
import glob
import time
import numpy as np

#permissionの設定で readとwriteの権限追加しておくこと→設定しなおしたらトークン再発行する必要あり
#keyの設定
CK = 'i9dTHPkL04WWeN9yGX1FCN5As'  #API key    以前はconsumer key
CS = 'M3GjMZezm0g8kH4mgehGPGBKoalCYfr00XmED9YMK7iAsE1xfG' #API key secret
AT = '3618847218-QzZHriHC0LoMXJHzRlDwhjewyPuXvIHQ5FtYduq'  #access token
AS = 'lbS4fSHaIwy81MMG1TUyhnIXU8Hi6UTkmiLcIZE8oRwUy' #access token secret

#twitter オブジェクト
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

#画像ファイルのパスを取得
files = glob.glob("images/*")


    
#メッセージ
message = "#photography"
#ランダムに画像を抽出
file = np.random.choice(files)

#ツイートする
api.update_with_media(status = message, filename = file)

print(message,file)


