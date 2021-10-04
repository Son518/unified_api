from datetime import datetime, timezone
import requests
import json



def rest(method, url, token, body=None):
    base_url = "https://api.surveymonkey.com/v3"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    return requests.request(method, f"{base_url}{url}", headers=headers, json=body)