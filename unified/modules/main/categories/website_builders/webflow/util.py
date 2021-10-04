from unified.core.auth import Auth
import requests
from datetime import datetime, timezone
import json

def rest(method, endpoint, access_token, body=None):

    headers = {
                'Authorization': f'Bearer {access_token}',
                'accept-version': '1.0.0',
                'Content-Type': 'application/json'
            }
    base_url = f"https://api.webflow.com/{endpoint}"
    response = requests.request(method, base_url, headers=headers, json=body)
    return response
