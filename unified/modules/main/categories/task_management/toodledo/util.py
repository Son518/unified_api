from datetime import datetime, timezone
import requests
import json
from unified.core.auth import Auth

def get_access_token(headers):
    ''' returns access token '''

    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url":headers["refresh_url"]
    }
    headers = {
            'Content-Type': 'application/json'
    }
    token = Auth().get_oauth2_token(auth_info)
    print(token)    
    return json.loads(token)["access_token"]

def rest(method,endpoint,access_token,data={}):
    headers = {
            "Authorization":f"Bearer {access_token}"
        }

    base_url=f"http://api.toodledo.com/3/"
    url=f"{base_url}{endpoint}"
    response = requests.request(method,url,headers=headers,data=data)
    return response

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)