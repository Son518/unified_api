from unified.core.auth import Auth
import requests
import json


def rest(method, url, access_token, body=None):
    """ Send REST request and returns response  """

    headers = {
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {access_token}"
    }
    BASE_URL = f"https://api.medium.com/v1/{url}"
    response = requests.request(method, BASE_URL, headers=headers, json=body)
    return response