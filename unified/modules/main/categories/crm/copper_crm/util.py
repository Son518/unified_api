from datetime import datetime, timezone
import requests
import json
from datetime import datetime, timezone


def rest(method, url, headers, body=None):
    headers = {
        "X-PW-AccessToken": headers['api_key'],
        "X-PW-Application": "developer_api",
        "X-PW-UserEmail": headers['email'],
        "Content-Type": "application/json"
    }
    base_url = f"https://api.prosperworks.com/developer_api/v1/{url}"
    
    return requests.request(method, base_url, headers=headers, json=body)

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
