import json
import requests

def rest(method,endpoint, data, server_token):
    ''' postmark api rest call '''
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'X-Postmark-Server-Token': server_token
    }

    if endpoint == "email" and  method == "POST":
        url="https://api.postmarkapp.com/email"
        response = requests.request("POST",url, headers=headers, json=(data))
        return response.text

    elif endpoint=="template" and method == "POST":
        url="https://api.postmarkapp.com/email/withTemplate"
        response = requests.request("POST",url, headers=headers, json=(data))
        return response.text

    elif endpoint=="bounce" and method == "POST":
         url="https://api.postmarkapp.com/bounces?type=HardBounce&inactive=true&count=50&offset=0"
         response = requests.request("POST",url, headers=headers, json=(data))
         return response.text
