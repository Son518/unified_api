from unified.core.auth import Auth
from datetime import datetime, timezone
import requests
import json


def get_access_token(headers):
    """ Returns new access token """

    auth_info = {
        "client_id": headers["client_id"],
        "client_secret": headers["client_secret"],
        "token": headers["refresh_token"],
        "refresh_url": headers["token_url"],
    }
    client = Auth().get_oauth2_requests(auth_info)
    return client


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)


def rest(method, url, client, body=None):
    """ Send REST request and returns response  """

    headers = {
        "content-type": "application/json"
       }
    base_url = f'https://api.capsulecrm.com/api/v2/{url}'
    
    response = client.request(method, base_url, headers=headers, json=body)

    return response
