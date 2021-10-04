import json
import base64
import requests

from flask import Response, request
from datetime import datetime, timezone

def get_toggl_request(method: str, url: str, toggl_headers, body=None, params=None):
    API_URL = "https://api.track.toggl.com/api/v8"
    auth_data = toggl_headers['api_key']+":"+"api_token"
    encoded_data = base64.b64encode(auth_data.encode("utf-8"))
    encoded_str = str(encoded_data, "utf-8")

    toggl_headers = {'Authorization' : 'Basic '+encoded_str,
                         "Content-Type" : "application/json",
               }
    final_url = API_URL + url
    return requests.request(method, final_url, headers=toggl_headers, json=body, params=params)

def epoch_to_format(format,epoch):
    '''Convert epoch to given format'''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
