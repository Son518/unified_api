import json
import requests
from helpscout import Client


def helpscout_client(headers):
    """ 
    return sdk client 
    """
    client = Client(headers["app_id"], headers["app_secret"])
    return client


def help_scout_token(headers):
    """
    returns access_token based on POST call
    """
    url = "https://api.helpscout.net/v2/oauth2/token"
    payload = f"grant_type=client_credentials&client_id={headers['app_id']}&client_secret={headers['app_secret']}"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request(
        "POST", url, headers=headers, data=payload).text
    return json.loads(response)["access_token"]


def rest(method, endpoint, data, access_token, id=None):
    """
    rest api calls done here based on method
    """
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }
    base_url = "https://api.helpscout.net/v2/"

    if endpoint == "conversations":
        url = base_url + endpoint
    elif endpoint == "notes":
        url = base_url+"conversations/"+str(id)+"/"+endpoint
    elif endpoint == "customers":
        url = base_url + endpoint
    elif endpoint == "reply":
        url = base_url+"conversations/"+str(id)+"/"+endpoint
    else:
        url = base_url
    response = requests.request(
        method, url, headers=headers, data=json.dumps(data))
    return response
