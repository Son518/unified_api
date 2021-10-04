import json
import requests
from datetime import datetime, timezone
from unified.core.auth import Auth


def get_access_token(headers):
    ''' returns access token '''

    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url": headers['refresh_url']
    }
    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))['access_token']


def rest(method,endpoint,data,access_token,organization_id,id=None):

  headers={
    "Authorization":f"Zoho-oauthtoken {access_token}",
    "Content-Type": "application/x-www-form-urlencoded"
    }
  base_url="https://books.zoho.in/api/v3/" 
  if endpoint in ['customers', 'items', 'invoices', 'estimates'] and method == 'POST':
    url = f"{base_url}{endpoint}?organization_id={organization_id}"
  elif endpoint == 'invoices' and method == 'GET':
    url = f"{base_url}{endpoint}/{id}?organization_id={organization_id}"
    print(url)
  


  data = f'JSONString={json.dumps(data)}'
  response = requests.request(method,url,headers=headers,data=data)
  return response


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)