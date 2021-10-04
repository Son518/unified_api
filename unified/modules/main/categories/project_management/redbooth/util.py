import json
import os.path
import inspect
from unified.core.auth import Auth
import requests


def get_authentication(headers):
    """ Returns new access token """

    if headers.get("access_token") is not None:
        return headers.get("access_token")
    
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
    BASE_URL = f"https://redbooth.com/api/3/{url}"
    response = requests.request(method, BASE_URL, headers=headers, json=body)
    return response