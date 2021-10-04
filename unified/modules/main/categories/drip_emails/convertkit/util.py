from datetime import datetime, timezone
import requests
# import base64
from http.client import HTTPSConnection
from base64 import b64encode


def rest(method, url, context, body=None):
    ''' returns response from request'''

    BASE_URL = f"https://api.convertkit.com/v3/{url}"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.request(method, BASE_URL, headers=headers, json=body)
    
    return response