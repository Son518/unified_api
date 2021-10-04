import json
import os.path
import inspect
from unified.core.auth import Auth
from flask import Response, request
from datetime import datetime, timezone
from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def get_authentication(headers):
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "refresh_token": headers.get('refresh_token'),
        "token_url": headers.get('token_url')
    }
    creds = Credentials.from_authorized_user_info(auth_info, scopes= ["https://www.googleapis.com/auth/calendar"])
    return creds

def epoch_to_format(format,epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
