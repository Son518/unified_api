import json
import os.path
import inspect
from unified.core.auth import Auth
import requests
# from datetime import datetime, timezone


def get_authentication(headers):
    """ Returns new access token """

    auth_info = {
        "client_id": headers["client_id"],
        "client_secret": headers["client_secret"],
        "token": headers["refresh_token"],
        "refresh_url": headers["token_url"],
    }
    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))['access_token']

def rest(method, url, access_token, body=None):
    """ Send REST request and returns response  """

    headers = {
        "Accept": "application/json, */*",
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {access_token}"
    }
    BASE_URL = f"https://tasks.googleapis.com/tasks/v1/{url}"

    response = requests.request(method, BASE_URL, headers=headers, json=body)
    return response

def epoch_to_format(format,epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
