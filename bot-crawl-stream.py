#!/usr/bin/python3
# coding=utf-8

# Import library yang dibutuhkan
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import csv

# Masukkan Twitter Token API
consumer_key = '6qXA2fmtgpN68yQSy3IzLUPs6'
consumer_secret = '0TEL9W6Eh3Dumx54zAdDWj2lA2i88ookST5jucs0ZOpQmwAb6m'
access_token = '563053721-yCvEBd3vxKWjxqNeJnQ4dRpMw3nEiPX1kfMbny5r'
access_token_secret = 'R99YPN00JTRZF7hNEnH9SkjoDJRn4UhGawdibX0cy1RGq'

# Buat class untuk stream
class StdOutListener(StreamListener):
    def on_status(self, status):
        # filter tweet yang berbahasa indonesia, kemudian masukkan kedalam csv
        if status.lang == "in":
            print(status)
            tweet_text = "'" + status.text.replace('\n', ' ') + "'"
            tweet_text = tweet_text.encode('utf-8')
            csvw.writerow([status.id,
                        status.user.screen_name,
                        status.created_at.strftime('%m/%d/%y'),
                        status.user.followers_count,
                        tweet_text])
            return True

    def on_error(self, status_code):
        # tampilkan pesan jika terdapat error koneksi
        if status_code == 420:
            print(status_code)
            return False


if __name__ == '__main__':

    # Handel twitter autentikasi dan koneksi streaming
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Buat file csv dan filter stream dengan kata kunci
    csvw = csv.writer(open("dataset_stream.csv", "a"))
    csvw.writerow(['twitter_id', 'name', 'created_at', 'followers_count', 'text'])
    stream.filter(track=['Jogja', 'Yogyakarta'])