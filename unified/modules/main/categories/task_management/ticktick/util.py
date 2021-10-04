from unified.core.auth import Auth
import requests
from datetime import datetime, timezone
import json

def rest(method,endpoint,access_token,body=None):

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    base_url = f"https://api.ticktick.com/{endpoint}"
    response = requests.request(method, base_url, headers=headers, json=body)
    return response