from unified.core.auth import Auth
import requests
import json
from datetime import datetime, timezone


def get_auth(context):
    """ Returns basic auth info """

    headers = context['headers']
    auth_info = {
        "type": "basic",
        "basic": {
            "user": headers['api_key'],
            "password": "X"
        }
    }
    auth = Auth().get_auth(auth_info)

    return auth


def rest(method, path, context, body=None):
    """ Send REST request and returns response  """

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json; charset=utf-8",
    }
    domain = context['headers']['domain']
    auth = get_auth(context)
    url = get_url(domain, path)

    response = requests.request(method, url, headers=headers, json=body, auth=auth)

    if response.status_code >= 400:
        raise Exception("Error: ", response.text)

    return json.loads(response.text)

def epoch_to_format(epoch, format='%Y-%m-%dT%H:%M:%SZ'):
    """ Convert  epoch to given format """

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def get_url(domain, path):
    """ Utility function for getting url """

    return f"https://{domain}.freshservice.com/api/v2/{path}"
