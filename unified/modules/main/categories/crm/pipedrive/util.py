import json
import requests
from datetime import datetime, timezone
from pipedrive.client import Client
from datetime import datetime, timezone


def pipedrive_authentication(headers):
    ''' returns pipedrive client'''

    client = Client(domain=f'https://{headers["domain"]}.pipedrive.com/')
    client.set_api_token(f'{headers["api_token"]}')
    return client


def rest(url, api_token, method, data, contenttype):
    ''' Pipedrive api rest call '''

    headers = {
        'Content-Type': 'application/json'
        }
    params = {
        "api_token": api_token
        }

    if method == "GET":
        response = requests.request("GET", f'{url}?api_token={api_token}')
        return response.text

    elif method == "POST":
        response = requests.request("POST", f'{url}', params=params, headers=headers, json=data)
        return response.text

    elif method == "PUT":
        response = requests.request("PUT", f'{url}?api_token={api_token}', json=data)
        return response.text

    elif method == "DELETE":
        response = requests.request("DELETE", f'{url}?api_token={api_token}', headers=headers)
        return response

    return "Wrong method provided"


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)


def property_conversion(properties):
    '''converts list of values into required fields'''

    return {item['name']: item.get('value') for item in properties}
