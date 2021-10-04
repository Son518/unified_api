from datetime import datetime, timezone
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from unified.core.auth import Auth
import requests
import json

def drive_client_instance(headers):
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "refresh_token": headers.get('refresh_token'),
        "token_url": headers.get('token_url')
    }
    creds = Credentials.from_authorized_user_info(auth_info, scopes= ["https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.file"])
    
    # Google Drive Client Instance  
    drive_client = build('drive', 'v3', credentials=creds)
    return drive_client

def epoch_to_format(format,epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

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


def rest(method, url, access_token, body=None):

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=body)