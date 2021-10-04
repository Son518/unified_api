from datetime import datetime, timezone
from unified.core.auth import Auth
import json
import requests

def convert_epoch(date,format):
    if not(date is None or "-" in date):
        date = epoch_to_format(format, date)
        return date
def dateformat_to_epoch(date):
    if date is not None:
        date = date.split("-")
        return datetime(int(date[0]),int(date[1]),int(date[2])).timestamp()
    
def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def get_access_token(headers):
    """ Returns new access token """

    auth_info = {
        "client_id": headers["client_id"],
        "client_secret": headers["client_secret"],
        "token": headers["refresh_token"],
        "refresh_url": headers["refresh_url"],
    }

    token = Auth().get_oauth2_token(auth_info)

    return (json.loads(token))['access_token']

def google_profile(context, params):
        '''Details of authenticated user for google apps'''

        access_token = get_access_token(context["headers"])
        url = "https://www.googleapis.com/oauth2/v1/userinfo"
        headers ={
            "Authorization" : f"Bearer {access_token}",
            "Content-Type" : "application/json"
        }
        response_data = requests.request("GET", url, headers=headers)
        response = response_data.json()
        profile = {
            'id':response['id'],
            'email':response['email'],
            'name':response['name']
        }
        return profile