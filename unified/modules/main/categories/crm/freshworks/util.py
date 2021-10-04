from unified.core.auth import Auth
from datetime import datetime, timezone
import requests
import json


def rest(method, url, body, context):

    api_key = context["api_key"]
    headers = {
        "Authorization": f"Token token={api_key}",
        "Content-Type": "application/json"
    }

    response = requests.request(method, url, headers=headers, data=body)
    return response


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
