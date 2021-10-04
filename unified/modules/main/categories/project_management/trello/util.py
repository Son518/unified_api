import json
from datetime import datetime, timezone
import requests
from requests_oauthlib import OAuth1


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def rest(method, url, headers, body=None):
    auth_1 = OAuth1(headers['client_id'], headers['client_secret'],
                    headers['token'], headers['token_secret'])
    return requests.request(method, url, auth=auth_1, json=body)
