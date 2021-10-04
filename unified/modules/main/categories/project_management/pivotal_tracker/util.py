import dataclasses
import json
import requests
from datetime import datetime, timezone

def rest(method, endpoint, api_key, body={}, id=None):

    headers = {
                "X-TrackerToken":f"{api_key}",
                "Content-Type": "application/json"
            }
    base_url = f"https://www.pivotaltracker.com/services/v5/{endpoint}"
    response = requests.request(method,base_url,headers=headers,json=body)
    return response