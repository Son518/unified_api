import json
from unified.core.auth import Auth
from flask import Response, request
from datetime import datetime, timezone
import requests


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)


def rest(method, url, body=None, context=None):
    headers = {
        "Authorization": context['headers']['api_token'],
        "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=body)
