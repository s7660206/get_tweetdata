#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 必要なモジュールのimport
import datetime
import pandas as pd
import tweepy

# 各種ツイッターのキーをセット　consumer_key, consumer_secret, access_key, access_secret
consumer_key = "*******************************"
consumer_secret = "*******************************"
access_key = "*******************************"
access_secret = "*******************************"

# 認証のためのAPIキーをセット
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)  # API利用制限にかかった場合、解除まで待機する

"""
メインの実行部分
ツイートデータの取得からデータの出力まで
"""

# ツイートデータの取得 日付の指定は 2020-7-30のみでもOK,
# 日本時間で取得したい場合は2020-7-30_00:00:00_JSTのように指定
# JSTをつけないと時間がUTCになる UTCは協定世界時間-> JST＋9:00(日本時間よりも9時間進んでいる)

# ツイートデータを番号順に出力

# ツイートデータをDataframeにする

# ツイートデータのCSVへの出力

# ツイートを収集する関数

"""
ツイート情報を特定のキーワードで、期間を指定して収集
取得できるデータは1週間以内のデータだけ
リツイート数＋いいね数の合計でツイートを絞り込める
"""

# 検索キーワードの設定、 リツイートは除く
searchkey = "Python"
# ツイートデータ取得部分
# tweepy.CursorのAPIのキーワードサーチを使用(api.search)
# qがキーワード, sinceがいつから, untilがいつまで, tweet_modeでつぶやきの省略ありなし, langで言語, .items(数)と書いてツイート数を指定
tweets = tweepy.Cursor(
    api.search,
    q=searchkey,
    exclude_replies=True,
    since="2019-11-10",
    until="2019-11-30",
    tweet_mode="extended",
    lang="ja",
).items(100)
print(tweets)

# ツイートのtweet_data = []  # ツイートデータを入れる空のリストを用意
tweet_data = []
for tweet in tweets:
    if tweet.favorite_count + tweet.retweet_count >= 50:  # いいねとリツイートの合計がrlcuont以上の条件
        tweet_data.append(
            [
                tweet.user.name,
                tweet.user.screen_name,
                tweet.retweet_count,
                tweet.favorite_count,
                tweet.created_at.strftime("%Y-%m-%d-%H:%M:%S_JST"),
                tweet.full_text("\n", ""),
            ]
        )
# ツイートデータを入れる空のリストを用意

# いいねとリツイートの合計がrlcuont以上の条件

# 空のリストにユーザーネーム、スクリーンネーム、RT数、いいね数、日付などを入れる


"""
ツイートのリストを順番をつけて出力する関数の作成
"""
i = 1
for tweet in tweet_data:
    print(f'{i}番目の呟き{tweet}')
    i += 1

"""
ツイートデータからDataFrameを作成する
"""

# データを入れる空のリストを用意(ユーザー名、ユーザーid、RT数、いいね数、日付け、ツイート本文)

# ツイートデータからユーザー名、ユーザーid、RT数、いいね数、日付け、ツイート本文のそれぞれをデータごとにまとめたリストを作る

# 先ほど作ったデータごとにまとめたリストからDataframeの作成
