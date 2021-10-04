import requests
from datetime import datetime, timezone


def rest(method, endpoint, context, data=None):
    
    api_key = context['headers']['api_key']

    headers = {
        "API-Key": f"{api_key}",
        "Content-Type": "application/json"
    }
    url = f'https://api.oncehub.com/v2/{endpoint}'

    resp = requests.request(method, url, headers=headers, json=data)  
    return resp