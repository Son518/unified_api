from datetime import datetime, timezone
import requests
import base64
from core.auth import Auth


def get_basic_token(headers):
    '''return basic acces token'''

    api_key = (headers["api_key"])+":X"
    api_bytes = api_key.encode('ascii')
    access_token = (base64.b64encode(api_bytes)).decode("utf-8")
    return access_token

def rest(method, url,access_token,body=None):
    ''' returns response from request'''
    headers = {
        "Authorization": f"Basic {access_token}",
        "Content-Type": "application/json"
    }
    
    response = requests.request(method, url, headers=headers, json=body)
    return response


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
