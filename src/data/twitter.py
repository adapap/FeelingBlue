import csv
import tweepy
from util import *

API = tokens['twitter']['API']
API_SECRET = tokens['twitter']['API_SECRET']

auth = tweepy.AppAuthHandler(API, API_SECRET)
api = tweepy.API(auth)

def fetch_tweets(limit):
    data = []
    for tweet in tweepy.Cursor(api.search, tweet_mode='extended', q='jetblue -filter:retweets AND -filter:replies', lang='en', include_entities='false').items(25 if limit else 500):
        text = clean_text(tweet.full_text)
        data.append(text)
    with open('tweets.csv', encoding='utf-8') as f:
        tweets = csv.reader(f, delimiter=',')
        for tweet in tweets:
            text = tweet[10]
            if 'jetblue' not in text.lower():
                continue
            data.append(clean_text(text))
    return data