from unified.core.auth import Auth
import requests
import json
from datetime import datetime, timezone


def get_access_token(headers, type="bot"):
    """ Returns new access token """

    token_t = type + "_token"

    return headers[token_t]


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

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def get_url():
    """ Utility function for getting url """

    return f"https://slack.com/api/"
