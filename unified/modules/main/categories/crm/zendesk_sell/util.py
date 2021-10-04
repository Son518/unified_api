import requests
import json
import base64
from datetime import datetime,timezone


def rest(method, url, body, access_token):
    ''' returns response from request'''
    headers = {
        "Authorization": f"Bearer {access_token}",
        'Accept': 'application/json',
        "Content-Type": "application/json"
    }

    response = requests.request(method, url, headers=headers, data=json.dumps(body),verify=True)

    return response

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def date_format_to_epoch(date):
    ''' convert date format to epoch'''

    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").timestamp()
     

