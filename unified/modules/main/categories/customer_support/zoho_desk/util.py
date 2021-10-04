from unified.core.auth import Auth
import requests
import json
from datetime import datetime, timezone


def get_access_token(context):
    """ Returns new access token """

    headers = context['headers']
    auth_info = {
        "client_id": headers["client_id"],
        "client_secret": headers["client_secret"],
        "token": headers["token"],
        "refresh_url": headers["refresh_url"],
    }
    token = Auth().get_oauth2_token(auth_info)

    return (json.loads(token))['access_token']


def rest(method, url, access_token, org_id, body=None, files=None):
    """ Send REST request and returns response  """

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Zoho-oauthtoken {access_token}"
    }

    if org_id:
        headers['orgId'] = org_id

    if files:
        del headers['Content-Type']
        response = requests.post(url, files=files, headers=headers)
        return response

    response = requests.request(method, url, headers=headers, json=body, files=files)

    return response

def epoch_to_format(epoch, format='%Y-%m-%dT%H:%M:%SZ'):
    """ Convert  epoch to given format """

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def get_url():
    """ Utility function for getting url """

    return "https://desk.zoho.in/api/v1/"
