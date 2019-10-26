import praw
from util import *

ID = tokens['reddit']['API']
SECRET = tokens['reddit']['API_SECRET']
reddit = praw.Reddit(client_id=ID, client_secret=SECRET, user_agent='webapp:feelingblue:v1.0.0 (by /u/LegendaryB3ast)')

def fetch_posts(limit):
    data = []
    for post in reddit.subreddit('jetblue').top(limit=25 if limit else 500):
        if not post.selftext:
            continue
        text = clean_text(f'{post.title} {post.selftext}')
        data.append(text)
    return data