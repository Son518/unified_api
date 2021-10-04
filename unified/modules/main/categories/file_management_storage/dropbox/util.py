from unified.core.auth import Auth
import requests
from datetime import datetime, timezone
from flask import request,Response
import json

def check_handshake():
    try:
        if request.args.get('challenge'):
            resp = Response(request.args.get('challenge'))
            resp.headers['Content-Type'] = 'text/plain'
            print(resp)
            return resp
    except Exception as err:
        print('in except')
        pass # supress error - for test_suite, or probably log it.        
    return None

def get_access_token(headers):
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers.get('refresh_token'),
        "refresh_url": headers['token_url']
    }
    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))['access_token']


def rest(method, url, access_token=None, body=None):
    
    base_url = f"https://api.dropboxapi.com/2/{url}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
        }
    return requests.request(method, base_url, headers=headers, json=body)


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
