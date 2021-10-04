from unified.core.auth import Auth
from datetime import datetime, timezone
import requests
import json

TYPEFORM_BASE_URL = 'https://api.typeform.com'

def rest(method, url, body=None, token=None):

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    return requests.request(method, url, headers=headers, json=body)


def epoch_to_format(format, epoch):
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
