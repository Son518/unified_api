from unified.core.auth import Auth
import requests
import json
from datetime import datetime, timezone


def get_access_token(headers):
    """ Returns new access token """

    auth_info = {
        "client_id": headers["client_id"],
        "client_secret": headers["client_secret"],
        "token": headers["refresh_token"],
        "refresh_url": headers["token_url"],
    }
    token = Auth().get_oauth2_token(auth_info)

    return (json.loads(token))['access_token']


def rest(method, url, access_token, body=None):
    """ Send REST request and returns response  """

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {access_token}",
    }

    response = requests.request(method, url, headers=headers, json=body)

    return response


def epoch_to_format(format, epoch):
    """ Convert  epoch to given format """

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc)\
        .strftime(format)


def get_url(context):
    """ Utility function for getting url """
    
    url = "https://gmail.googleapis.com/gmail/v1/users/"
    if context.get('headers').get('user_email'):
        return f"{url}{context['headers']['user_email']}/"
    else:
        return f"{url}me/"
