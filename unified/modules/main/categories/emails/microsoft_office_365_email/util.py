from unified.core.auth import Auth
import requests
from datetime import datetime, timezone
import json


def get_access_token(headers):
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers.get('refresh_token'),
        "refresh_url": headers['token_url']
    }
    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))['access_token']


def rest(method, url, access_token, body=None):

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=body)


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
