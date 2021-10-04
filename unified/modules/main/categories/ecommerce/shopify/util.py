from datetime import datetime, timezone
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from unified.core.auth import Auth
import requests
import json

def get_access_token(headers):
    
    # Rest api Instance
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url": headers['token_url']
    }
    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))['access_token']


def rest(method, url, domain, access_token, body=None):
    BASE_URL = f"https://{domain}.myshopify.com/{url}"
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }
    return requests.request(method, BASE_URL, headers=headers, json=body)