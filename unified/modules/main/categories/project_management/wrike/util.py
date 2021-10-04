from unified.core.auth import Auth
from datetime import datetime, timezone
import requests
import json


def get_access_token(headers):
    ''' returns access token '''

    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url": headers.get('refresh_url') or headers.get('token_url')
    }

    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))['access_token']


def rest(method, url, body=None, access_token=None):
    ''' returns rest calls result'''

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=body)


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
