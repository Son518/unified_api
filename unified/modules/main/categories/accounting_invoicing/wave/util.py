import json
import requests

from flask import Response, request
from datetime import datetime, timezone

def get_wave_request(method: str, wave_headers, body=None, variables=None):
    API_URL = "https://gql.waveapps.com/graphql/public"


    wave_headers = {'Authorization' : 'Bearer '+wave_headers['full_access_token'],
                    "Content-Type" : "application/json",
               }
    data = {"query": body, "variables": variables}

    return requests.request(method, API_URL, headers=wave_headers, json=data)

def epoch_to_format(format,epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
