from unified.core.auth import Auth
import json
import requests
from datetime import datetime, timezone


def get_access_token(headers):
    """ Returns new access token """

    auth_info = {
        "client_id": headers["client_id"],
        "client_secret": headers["client_secret"],
        "token": headers["token"],
        "refresh_url": headers["refresh_url"],
    }

    token = Auth().get_oauth2_token(auth_info)

    return (json.loads(token))['access_token']


def rest(method, url, access_token=None, body=None, add_headers=None, c_type=None):
    """ Send REST request and returns response  """

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json; charset=utf-8",
    }

    if c_type:
        headers["Content-Type"] = c_type

    if add_headers:
        headers = {
            **headers,
            **add_headers
        }

    if access_token:
        headers = {
            **headers,
            "Authorization": f"Bearer {access_token}"
        }

    response = requests.request(method, url, headers=headers, json=body)

    return response

def epoch_to_format(format, epoch):
    """ Convert  epoch to given format """

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def get_url():
    """ Utility function for getting url """

    return "https://graph.microsoft.com/v1.0/me/"
