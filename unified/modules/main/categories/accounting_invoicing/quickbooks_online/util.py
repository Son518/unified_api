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

    token = Auth().get_oauth2_token(auth_info)
    print(token)
    return (json.loads(token))['access_token']
    
def rest(method, url, access_token, body=None):
    """ Send REST request and returns response  """
    BASE_URL = f"https://quickbooks.api.intuit.com/{url}"

    if 'send' in BASE_URL:
        payload = {}
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.request("POST", BASE_URL, headers=headers, data=payload)
    else:    
        headers = {
            "Accept": "application/json, */*",
            "content-type": "application/json; charset=utf-8",
            "OData-MaxVersion": "4.0",
            "OData-Version": "4.0",
            "Authorization": f"Bearer {access_token}",
        }
        response = requests.request(method, BASE_URL, headers=headers, json=body)
    return response

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
