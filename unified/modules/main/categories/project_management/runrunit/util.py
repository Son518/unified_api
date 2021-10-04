import json
import os.path
import inspect
from unified.core.auth import Auth
import requests


def rest(method, url, headers, body=None):
    """ Send REST request and returns response  """

    headers = {
        "Accept": "application/json, */*",
        "content-type": "application/json; charset=utf-8",
        "App-Key": headers["app_key"],
        "User-Token": headers["user_token"]
    }

    BASE_URL = f"https://runrun.it/api/v1.0/{url}"
    
    response = requests.request(method, BASE_URL, headers=headers, json=body)
    return response
