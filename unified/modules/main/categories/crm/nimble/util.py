import json
import requests
from datetime import datetime, timezone

def rest(method, endpoint, data, api_key):
    ''' nimble api rest call '''
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Authorization':f"Bearer {api_key}" 
    }

    if endpoint == "contact" and method == "POST":
        url="https://api.nimble.com/api/v1/contact"
        response = requests.request("POST",url, headers=headers, json=(data))
        return response.text
    elif endpoint == "task" and method == "POST":
        url="https://api.nimble.com/api/v1/activities/task"
        response = requests.request("POST",url, headers=headers, json=(data))
        return response.text

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)