from datetime import datetime, timezone
import requests
import base64


def get_basic_token(headers):
    '''return basic acces token'''
    api_key = (headers["api_key"])+":{$$.env.password}"
    api_bytes = api_key.encode('ascii')
    access_token = (base64.b64encode(api_bytes)).decode("utf-8")
    return access_token


def rest(method, url, body, access_token):
    ''' returns response from request'''
    headers = {
        "Authorization": f"Basic {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.request(method, url, headers=headers, data=body)

    return response


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
