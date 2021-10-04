import json
import requests
from unified.core.auth import Auth


def get_acess_token(headers):
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url": headers['token_url']
    }
    token = Auth().get_oauth2_token(auth_info)

    return json.loads(token)['access_token']


def rest(method, url, body, access_token):
    ''' returns response from request'''
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    if method == "DELETE":
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
    response = requests.request(method, url, headers=headers, data=body)

    return response
