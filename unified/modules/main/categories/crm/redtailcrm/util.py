import requests
import json
import base64
from datetime import datetime, timezone


def get_basic_token(headers):
    ''' return basic api key'''

    api_key = headers["apikey"]+":"+headers["username"]+":"+headers["password"]
    api_bytes = api_key.encode('ascii')
    access_token = (base64.b64encode(api_bytes)).decode("utf-8")
    
    return access_token


def rest(method, url, body, access_token):
    ''' does rest api call and return response'''

    headers = {
        "Authorization": f"Basic {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.request(
        method, url, headers=headers, data=json.dumps(body))

    return response


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
