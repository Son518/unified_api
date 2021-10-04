import requests
import base64
from datetime import datetime

def get_basic_token(headers):
    '''return basic acces token'''
    api_key = (headers["api_key"]+":"+headers["api_secret"])
    api_bytes = api_key.encode('ascii')
    access_token = (base64.b64encode(api_bytes)).decode("utf-8")
    return access_token


def epoch_to_format(epoch):
    
    """converts epoch to isoformat"""
    return datetime.utcfromtimestamp(int(epoch)).isoformat()


def rest(method, url, access_token, body=None):
    headers = {
        "Authorization": f"Basic {access_token}",
        "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=body)