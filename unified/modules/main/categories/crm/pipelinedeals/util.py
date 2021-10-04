import dataclasses
import json
import requests
from datetime import datetime, timezone

def rest(method, endpoint, api_key, body={}, id=None, phone_number=None):

    headers = {
        "Content-Type": "application/json"
    }
    base_url = f"https://api.pipelinecrm.com/api/v3/"    
    if endpoint in ['notes', 'companies', 'deals', 'calendar_entries', 'people'] and method == 'POST':
        url = f"{base_url}{endpoint}?api_key={api_key}"
    elif endpoint in ['companies', 'deals', 'people'] and method == 'PUT':
        url = f"{base_url}{endpoint}/{id}?api_key={api_key}"
    elif endpoint in ['companies', 'deals', 'people'] and method == 'GET':
        url = f"{base_url}{endpoint}/{id}?api_key={api_key}"
    elif endpoint=="people/phone_number" and method=='GET':
        url = f"{base_url}people?person_phone={phone_number}&api_key={api_key}"
    response = requests.request(method,url,headers=headers,json=body)
    return response

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)