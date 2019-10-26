import json
import twitter
import reddit
import reviews

def fetch_data(limit=False):
    data = {}
    print('Twitter...')
    data['twitter'] = twitter.fetch_tweets(limit)
    print(len(data['twitter']), 'tweets found')
    print('Reddit...')
    data['reddit'] = reddit.fetch_posts(limit)
    print(len(data['reddit']), 'posts found')
    print('Reviews...')
    data['reviews'] = reviews.fetch_data(limit)
    print(len(data['reviews']), 'reviews found')
    with open('input.json', 'w') as f:
        json.dump(data, f)

fetch_data(limit=False)