from unified.core.auth import Auth
from datetime import datetime, timezone
import requests
import json

def get_url(site_id, endpoint):
    # return f'https://{domain}.atlassian.net/rest/servicedeskapi/{endpoint}'
    
    return f'https://api.atlassian.com/ex/jira/{site_id}/rest/servicedeskapi/{endpoint}'


def get_access_token(headers):
    # Rest api Instance
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url": headers['refresh_url']
    }

    token = Auth().get_oauth2_token(auth_info)
    
    return json.loads(token)['access_token']


def rest(method, url, access_token, body=None):

    headers = {
        "Authorization": f"Bearer {access_token}",
        # "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=body)
