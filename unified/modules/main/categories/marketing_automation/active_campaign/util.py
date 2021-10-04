import urllib.parse
import requests
from datetime import datetime, timezone
from activecampaign.client import Client


def get_client(context):
    api_key = context['headers']['api_key']
    domain = context['headers']['domain'] # is it right - domain in headers?

    return Client(f'https://{domain}.api-us1.com', api_key)


def rest(method, endpoint, context, data):

    api_token = context['headers']['api_key']
    domain = context['headers']['domain'] # is it right - domain in headers?

    headers = {
        "Api-Token": f"{api_token}",
        "Content-Type": "application/json"
    }
    url = f'https://{domain}.api-us1.com/api/3/{endpoint}'

    resp = requests.request(method, url, headers=headers, json=data)  ## json=
    return resp

def custom_field(field_id, field_name, field_value, field_currency=None):
    field = {
        "customFieldId": field_id,
        "fieldValue": field_value,
    }

    ## where does field_name go?

    if field_currency:
        field["fieldCurrency"] = field_currency

    return field


def get_custom_field_value(dct, cust_field):
    """Get value of custom field from 'fields' using reverse lookup

    Args:
        dct (dict): dictionary containing custom field
        cust_field (str): field name for reverse lookup

    Returns:
        str: value found. None, if not found
    """

    for num in dct['fields']:
        if dct['fields'][num]['key'].lower() == cust_field.lower():
            return dct['fields'][num]['value']

    return None


def utl_to_values(url_values):
    return urllib.parse.parse_qsl(url_values, keep_blank_values=True)


def extract_multi_dict(orig_dct):
    dup_dct = {**orig_dct}

    result_dct = {}
    while dup_dct:
        for orig_key, value in orig_dct.items():
            if (ob := orig_key.rfind('[')) > -1 and (cb := orig_key.rfind(']')) > -1:
                keyprefix = orig_key[:ob]
                subkey = orig_key[ob + 1:-1]

                if keyprefix not in result_dct:
                    result_dct[keyprefix] = {}
                
                result_dct[keyprefix][subkey] = dup_dct[orig_key]

                if keyprefix.rfind('[') == -1 or keyprefix.rfind(']') == -1:
                    del dup_dct[orig_key]
            else:
                result_dct[orig_key] = value
                del dup_dct[orig_key]

        if not dup_dct:
            return result_dct
        
        orig_dct = {**result_dct}
        dup_dct = {**result_dct}
        result_dct = {}


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)