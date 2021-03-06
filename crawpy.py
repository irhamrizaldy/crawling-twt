# -*- coding: utf-8 -*-
"""crawl-stream.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F4YIOQ_wnEp3rCkty4FQZYYOFvD8aUyu
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import json, time, sys
import csv
import telegram

# API Twitter
consumer_key = 'w1TqY9AwKzDX3OizxCU1pA0v1'
consumer_secret = 'OT569vsiQlUdoVbx1AyZpnFJddc8M7zweCi6RT4EhRqKAaoKcn'
access_token = '1439979991261802501-Ac22VOQPgfLD7SpG0hzbP1OBw0F18J'
access_token_secret = 'l498vnjrA9okLbXUFvd5ey3ZPbNnuCkzxftAUBQtJVsjA'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API Telegram
api_key = '2010624549:AAGv8qDbYJIMuRPG60SwhOPWbCIDgA7nDuk'
user_id = '-1001735202458'

class StdOutListener(StreamListener):
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 0     # buat variabel inisialisasi jumlah tweet

    def on_status(self, status):
        # record = {'TWEET': status.text, 'LINK': 'https://twitter.com/'+str(status.user.screen_name)+'/status/'+str(status.id)}       # simpan hasil response kedalam variabel (contoh: ambil text/tweet dan created_at/tanggal tweet)
        tweet = status.text
        link = 'https://twitter.com/'+str(status.user.screen_name)+'/status/'+str(status.id)
        username = str(status.user.screen_name)
        if (username == 'joktugfess' or username == 'basejokitugas') :
            bot = telegram.Bot(token=api_key)
            record = bot.send_message(chat_id=user_id, text=tweet + " " + link)
            print(record)
          
        self.num_tweets += 1        # setiap satu tweet yang berhasil didapat dihitung dengan menambahkan satu
        # if status.lang == 'in':     # filter tweet yang hanya berbahasa indonesia
        #   if self.num_tweets < 200:  # batasi jumlah tweet yang dicrawling sebanyak 20
        #       return True
        #   else:
        #       return False

    def on_error(self, status_code):
        if status_code == 420:
            print('Error on status', status)
            return False

    def on_limit(self, status):
        print('Limit threshold exceeded', status)

    def on_timeout(self, status):
        print('Stream disconnected; continuing...')


stream = Stream(auth, StdOutListener())
# stream.filter(track=['coding', 'joki web', 'joki website', 'buat web', 'bikin web', 'buat website', 'bikin website', 'joki buat program', 'joki program', 'joki ngoding', 'joki data mining', 'buat flowchart', 'bikin flowchart', 'joki coding', 'tugas coding', 'joki informatika', 'joki pemrograman', 'joki java', 'bantuin java', 'bantuin c++', 'bantuin python', 'tugas python', 'joki python'])   # menggunakan fungsi stream filter untuk mencari kata kunci
# stream.filter(track=['joktug!', 'Joktug!' 'bj!', 'Bj!', 'bJ!', 'BJ!'])   # menggunakan fungsi stream filter untuk mencari kata kunci
stream.filter(track=['koding', 'ngoding', 'coding', 'buat program', 'bikin program', 'joki program', 'flowchart', 'informatika', 'pemrograman', 'pemrograman dasar', 'java', 'python', 'c++', 'c#', 'buat web', 'buat website', 'bikin web', 'bikin website', 'php', 'PHP', 'html', 'HTML'])