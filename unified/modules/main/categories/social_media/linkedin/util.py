import json
import requests
from core.auth import Auth

def get_access_token(headers):

    auth_info = {
        "client_id":headers["client_id"],
        "client_secret":headers["client_secret"],
        "token":headers["token"],
        "refresh_url":headers["token_url"]
    }
    token = Auth().get_oauth2_token(auth_info)
    return json.loads(token)['access_token']

def rest(method,url,access_token,data={}):

    headers = {
        "Authorization" :f"Bearer {access_token}",
        "ContentType" :"application/json"
    }
    response = requests.request(method,url,headers=headers,json=data)
    return response