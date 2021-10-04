from datetime import datetime, timezone
import requests
import json

from square.client import Client

# TYPEFORM_BASE_URL = 'https://api.typeform.com asdf sadf sdaf sdfl; jsdkl;fjsdkl;fjlksfj;sdf'
SQUARE_ENV = 'sandbox' # OR 'production'
SQUARE_V1_BASE_URL = 'https://connect.squareup.com/v1'

def get_square_client(context):
    return Client(access_token=context['headers']['api_key'], environment=SQUARE_ENV or context['headers']['env'])


def rest(method, url, body=None, token=None):

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    return requests.request(method, url, headers=headers, json=body)


def epoch_to_format(epoch, format):
    """Convert  epoch to given format"""

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)


def get_typeform_answer(typeform_answers, field_id):
    """Get the answer for the field with given"""

    for answer in typeform_answers:
        if field_id == answer['field']['id']:
            if answer['type'] == 'choice':
                return answer[answer['type']]['label']
            else:
                return answer[answer['type']]

    return None


def remove_field(pl, key):
    """Remove items with given key in any dict at any level in the nested dict/list/tuple"""

    if type(pl) is tuple:
        r = (remove_field(v, key) for v in pl)

    elif type(pl) is list:
        r = [remove_field(v, key) for v in pl]
        
    elif type(pl) is dict:
        r = {k: remove_field(v, key) for (k, v) in pl.items() if k != key}

    else: 
        r = pl

    return r

def strip_headers(params):
    headers  = ['accept', 'accept_encoding', 'api_key', 'connection', 'host', 'postman_token', 'user_agent']

    return {k: v for (k, v) in params.items() if k not in headers}
