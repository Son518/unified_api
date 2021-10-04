from unified.core.auth import Auth
import requests
import json

def get_access_token(headers):
    """ Returns new access token """

    auth_info = {
        "client_id": headers["client_id"],
        "client_secret": headers["client_secret"],
        "token": headers["refresh_token"],
        "refresh_url": headers["refresh_url"],
    }

    token = Auth().get_oauth2_token(auth_info)

    return (json.loads(token))['access_token']


def rest(method, url, access_token, body=None):
    """ Send REST request and returns response  """

    headers = {
        "Accept": "application/json",
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.request(method, url, headers=headers, json=body)

    return response
