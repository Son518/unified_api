from datetime import datetime, timezone
import requests
# import base64
from http.client import HTTPSConnection
from base64 import b64encode


def rest(method, url, context, body=None):
    ''' returns response from request'''

    api_key = context.get("headers").get("api_key")
    
    headers = {
        "Authorization": f"Basic {api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response = requests.request(method, url, headers=headers, data=body)
    return response


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
