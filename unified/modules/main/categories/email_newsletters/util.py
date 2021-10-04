from unified.core.auth import Auth
from datetime import datetime, timezone
from mailerlite import MailerLiteApi
import requests
import json


def rest(method, url, api_key, body=None):

    headers = {
        "X-MailerLite-ApiKey": f"{api_key}",
        "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=body)


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)