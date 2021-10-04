import urllib.parse
import requests
from datetime import datetime, timezone
from activecampaign.client import Client


def rest(method, endpoint, context, data=None):

    access_token = context['headers']['access_token']
    account_id = context['headers']['account_id']

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Harvest-Account-Id": f"{account_id}",
        "Content-Type": "application/json"
    }
    url = f'https://api.harvestapp.com/v2/{endpoint}'

    resp = requests.request(method, url, headers=headers, json=data)
    return resp