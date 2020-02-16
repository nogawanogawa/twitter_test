import requests
from requests_oauthlib import OAuth1Session
import json

#取得したkeyを以下で定義する
API_key = ''
API_secret_key = ''
access_token  =''
access_token_secret = ''

# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#パラメータの定義
params = {'screen_name':'nogawanogawa',
          'exclude_replies':True,
          'include_rts':False,
          'count':200}

#APIの認証
twitter = OAuth1Session(API_key, API_secret_key, access_token, access_token_secret)

f_out = open('tweets.txt','w')

for j in range(100):
    res = twitter.get(url, params = params)

    if res.status_code == 200:

        # API残り
        limit = res.headers['x-rate-limit-remaining']
        print ("API remain: " + limit)
        if limit == 1:
            sleep(60*15)

        n = 0
        timeline = json.loads(res.text)
        # 各ツイートの本文を表示
        for i in range(len(timeline)):
            if i != len(timeline)-1:
                f_out.write(timeline[i]['text'] + '\n')
            else:
                f_out.write(timeline[i]['text'] + '\n')
                # 一番最後のツイートIDをパラメータmax_idに追加
                params['max_id'] = timeline[i]['id']-1

f_out.close()
