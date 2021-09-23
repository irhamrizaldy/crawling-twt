import tweepy
import csv
access_token="1439979991261802501-NGHrh9DxPYVq0UDfW50VB5VRoiEMX6"
access_token_secret="4d4PFhmVeCJMKPv4ULJEqpi5dKzn6dpjFC1CSegus86cA"
consumer_key="RvQVtnf2IOiOpJC1sRErHLkco"
consumer_key_secret="8LbwTnshEjRQq0WToQxVCqUIx0Yh8wJUb5oNnKgJSuZeM34z7P"
auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
api = tweepy.API(auth)
# Open/create a file to append data to
csvFile = open('dataset_search.csv', 'w', encoding='utf-8')
#Use csv writer
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search, q='coding -filter:retweets', tweet_mode='extended',lang="id", since='2021-09-12', until='2021-09-22').items(100):
    text = tweet.full_text
    user = tweet.user.name
    created = tweet.created_at
    csvWriter.writerow([created, text.encode('utf-8'), user])
csvWriter = csv.writer(csvFile)
csvFile.close()