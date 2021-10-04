from unified.core.auth import Auth
import requests
from datetime import datetime, timezone
import json

def get_access_token(headers):
    # Rest api Instance
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url": headers['refresh_url']
    }
    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))['access_token']

def rest(method,endpoint,access_token, body=None):

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type":"application/xhtml+xml"
    }
    base_url=f"https://graph.microsoft.com/v1.0/me/onenote/{endpoint}"
    if method=="GET":
        headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type":"application/json"
                }
        response = requests.request(method, endpoint, headers=headers)  
    elif method=="PATCH":
        response = requests.request(method, base_url, headers=headers, json=body)
    else:
        response = requests.request(method, base_url, headers=headers, data=body)
    return response