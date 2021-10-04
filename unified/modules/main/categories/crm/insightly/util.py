import json
import base64
import requests

from flask import Response, request
from datetime import datetime, timezone

def get_insightly_request(method: str, url: str, insightly_headers, body=None):
    API_URL = "https://api.na1.insightly.com/v3.1"
    encoded_bytes = base64.b64encode(insightly_headers['api_key'].encode("utf-8"))
    encoded_key = str(encoded_bytes, "utf-8")

    #Do I need to increment the dictionary wit the Authorization data or is the authorization is already included in headers?
    insightly_headers = {'Authorization' : 'Basic '+encoded_key,
                         "Content-Type" : "application/json",
               }
    final_url = API_URL + url
    return requests.request(method, final_url, headers=insightly_headers, json=body)

def epoch_to_format(format,epoch):
    '''Convert epoch to given format'''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def date_format_to_epoch(date):
    '''Convert date format to epoch'''

    return datetime.strptime(date, "%Y-%m-%d %H:%M:%S").timestamp() * 1000
