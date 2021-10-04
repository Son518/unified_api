import json
from datetime import datetime, timezone
import requests
from requests_oauthlib import OAuth1
import twitter


def get_access_token(headers):
    consumer_key = headers['client_id']
    consumer_secret = headers['client_secret']
    access_token = headers['token']
    token_secret = headers['token_secret']
    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=token_secret, cache=None, tweet_mode='extended')
    return api
