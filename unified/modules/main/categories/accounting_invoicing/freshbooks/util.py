from datetime import datetime, timezone
import requests
import json

def get_access_token(freshbooks_headers):
    """ Returns new access token """

    auth_info = {
        "client_id": freshbooks_headers["client_id"],
        "client_secret": freshbooks_headers["client_secret"],
        "token": freshbooks_headers["refresh_token"],
        "redirect_uri":freshbooks_headers["redirect_uri"],
        "grant_type":"refresh_token"
    }
    headers = {
            'Content-Type': 'application/json'
            }
    access_token = requests.request("POST",freshbooks_headers["refresh_url"],headers=headers,data=json.dumps(auth_info)).text
    return access_token

def rest(method,url,data,access_token):
    headers = {
        "Authorization":f"Bearer {access_token}"
    }
    if method == "GET":
        response = requests.request(method,url,headers=headers,data=data)
    else :
        response = requests.request(method,url,headers=headers,json=data)
    return response

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)