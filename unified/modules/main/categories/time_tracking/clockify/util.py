import json
import requests
from datetime import datetime, timezone

def rest(method,endpoint,data,api_key,workspace_id,user_id=None,id=None,name=None):
    ''' clockify api rest call '''
    headers = {
        'Content-Type': "application/json",
        'X-Api-Key': api_key
    }
    base_url=f"https://api.clockify.me/api/v1/workspaces/{workspace_id}"
    if endpoint == "projects" and  method == "POST":
        url=f"{base_url}/projects"
    elif endpoint == "client" and method == "POST":
        url=f"{base_url}/clients"
    elif endpoint == "tag" and method == "POST":
        url=f"{base_url}/tags"
    elif endpoint == "time" and method == "POST":
        url=f"{base_url}/time-entries"
    elif endpoint == "task" and method == "POST":
        url=f"{base_url}/projects/{id}/tasks"
    elif endpoint == "stop" and method == "POST":
        url=f"{base_url}/user/{user_id}/time-entries"
    elif endpoint == "projects" and method == "GET":
        url=f"{base_url}/projects?name={name}"
    elif endpoint == "task" and method == "GET":
        url=f"{base_url}/projects/{id}/tasks?name={name}"
    elif endpoint == "client" and method == "GET":
        url=f"{base_url}/clients?name={name}"
    elif endpoint == "tag" and method == "GET":
        url=f"{base_url}/tags?name={name}"
    elif endpoint == "time" and method == "GET":
        url=f"{base_url}/user/{user_id}/time-entries"

    response = requests.request(method,url,headers=headers,json=data)
    return response