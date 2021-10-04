from basecampy3 import Basecamp3
from unified.core.auth import Auth
from datetime import datetime, timezone
import requests
import json

def basecamp3_client(headers):
    # SDK instance
    bc3 = Basecamp3(
        client_id=headers['client_id'],
        client_secret=headers['client_secret'],
        redirect_uri="https://plugins.500apps.com/oauth-authorized",
        refresh_token=headers['refresh_token'],  # header 'refresh_token' required, per (python repo) plugins
        conf={}
    )

    return bc3

def get_access_token(headers):
    # Rest api Instance
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url": "https://launchpad.37signals.com/authorization/token?type=refresh"
    }
    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))['access_token']

def rest(method, url, body=None, access_token=None):

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=body)

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
