import json
import requests
from datetime import datetime, timezone
from agilecrm.client import Client
from datetime import datetime, timezone


def agilecrm_authentication(headers):
    ''' returns agilecrm client'''

    agilecrm_client = Client(headers["api_key"], headers["email"], headers["domain"])

    return agilecrm_client


def rest(url, headers, method, data, contenttype):
    ''' agilecrm api rest call '''

    EMAIL = headers["email"]
    APIKEY = headers["api_key"]
    headers = {
        'Accept': 'application/json',
        'content-type': contenttype,
    }

    if method == "GET":

        response = requests.request("GET",url, headers=headers, auth=(EMAIL, APIKEY))
        return response.text

    elif method == "POST":

        response = requests.request("POST",url, data=json.dumps(data), headers=headers, auth=(EMAIL, APIKEY))
        return response.text

    elif method == "PUT":
        response = requests.request("PUT",url, data=json.dumps(data), headers=headers, auth=(EMAIL, APIKEY))
        return response.text

    elif method == "DELETE":
        response = requests.request("DELETE",url, headers=headers, auth=(EMAIL, APIKEY))
        return response



    return "Wrong method provided"


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)


def property_conversion(properties):
    '''converts list of values into required fields'''

    return {item['name']: item.get('value') for item in properties}
