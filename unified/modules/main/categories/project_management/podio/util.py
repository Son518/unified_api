import json
import requests
from datetime import datetime, timezone
from pypodio2 import api

def podio_oauth(headers):
    ''' return podio oauth cleint'''

    client_id = headers["client_id"]
    client_secret=headers["client_secret"]
    username = headers["username"]
    password = headers["password"]
    podio_oauth_session = api.OAuthClient(client_id, client_secret, username, password)

    return podio_oauth_session

def get_access_token(podio_headers):
    '''return access_token'''

    url = f"https://podio.com/oauth/token?grant_type=password&username={podio_headers['username']}&password={podio_headers['password']}&client_id={podio_headers['client_id']}&redirect_uri={podio_headers['redirect_uri']}&client_secret={podio_headers['client_secret']}"
    headers = {
    'Cookie': '_podio_session=UVB4YlJOOWdDSkF6WkFZdFpPZ1BuUlhsQ2YvNWZOTDMvb0dIWjduUEEwcG96WVpxUTF1U1pFcGo4RzZwZENvZlB6bUg2eDlWZHVSbGczNDZYQ1hxSkJma0hhYVhLeUZUeE5VRkxlQjBKZjlTcGdySjdVSEpKVkZ0aWR4T28yVE1vRkp5VXFyWnpjbUdyWDRCVHB5WUtTY0U0cHlGa3d5ampleURiQUI3c1l4dW5BbzBLVnVGSkRXelA1U3VUMk84MHhwT3pYcjRPZFg1ckVrbmhiWmtSSGs4ZkFSYVZCUGYwWVFVNDNhZGhWMUdsSEhTc2NKMHFmK281ZGMrL1lmY2lDM1BOdzV4ZFZOLzhzRk8yZGdPekhNcHJFN1VycFRGM2JuZGh5cXArU2dpRm1Vek1OaC9qZnptNzY4ejFwSjNRWDFiMDcrREVjSnk5ODF6cVA1YlpRPT0tLTByZ3J3VU9jSXl5TXE2dFYrZkFSMEE9PQ%3D%3D--1f2e5b67d68e75deacbfd8351f541e11873b30d4'
    }

    response = json.loads(requests.request("POST", url, headers=headers, data={}).text)
    
    return response["access_token"]


def rest(method, url, body, access_token):
    ''' returns response from request'''

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.request(method, url, headers=headers, data=body)

    return response

def epoch_to_format(format,epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)


