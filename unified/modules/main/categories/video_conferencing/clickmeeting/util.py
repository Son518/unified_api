import dataclasses
import json
import requests
from datetime import datetime, timezone

def rest(method, endpoint, api_key, body=None):

    headers = {
                "X-API-KEY": f"{api_key}",
                "Content-Type": "application/json"
            }
    base_url = f"https://api.clickmeeting.com/v1/{endpoint}" 
    response = requests.request(method,base_url,headers=headers,data=body)
    return response 