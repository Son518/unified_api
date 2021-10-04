import json
import requests
from datetime import datetime, timezone

def rest(method,endpoint,data,access_token,id=None):
    ''' drift api rest call '''
    headers = {
        "Authorization":f"Bearer {access_token}"
    }
    if endpoint == "contact" and  method == "POST":
        url="https://driftapi.com/contacts"
        response = requests.request("POST",url,headers=headers,json=data)
        return response.text
    elif endpoint=="update_contact" and method == "PATCH":
        url="https://driftapi.com/contacts/11851206058065920"
        response = requests.request("PATCH",url,headers=headers,json=data)
        return response.text

    elif endpoint=="anonymous_user_id" and method == "GET":
         url=f"https://driftapi.com/users/{id}"
         response = requests.request("GET",url, headers=headers, json=data)
         return response.text
    
    elif endpoint=="list" and method == "GET":
         url=f"https://driftapi.com/users/list"
         response = requests.request("GET",url, headers=headers, json=data)
         return json.loads(response.text)

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]),tz=timezone.utc).strftime(format)