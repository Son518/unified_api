from unified.core.auth import Auth
import requests
from datetime import datetime, timezone
import json

def get_access_token(headers):
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url": headers['refresh_url']
    }
    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))['access_token']

def rest(method,endpoint,access_token,body=None):

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    base_url = f"https://api.pinterest.com/v5/{endpoint}"
    response = requests.request(method, base_url, headers=headers, json=body)
    return response