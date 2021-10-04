import dataclasses
import json
import requests
from datetime import datetime, timezone

def rest(method, endpoint, api_key, body=None):

    headers = {
                "authorization": f"{api_key}",
                "Content-Type": "application/json"
            }
    base_url = f"https://api.livestorm.co/v1/{endpoint}" 
    response = requests.request(method,base_url,headers=headers,json=body)
    return response 