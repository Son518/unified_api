import json
import requests
from datetime import datetime, timezone

def rest(method,endpoint,data,api_key,id=None):
    ''' postmark api rest call '''
    headers = {
        'Content-Type': "application/json",
        'Authorization': f"Bearer {api_key}"
    }

    if endpoint == "projects" and  method == "POST":
        url="https://api.todoist.com/rest/v1/projects"
    elif endpoint == "task" and method == "POST":
        url="https://api.todoist.com/rest/v1/tasks"
    elif endpoint == "close" and method == "POST":
        url=f"https://api.todoist.com/rest/v1/tasks/{id}/close"
    elif endpoint == "tasks" and method == "POST":
        url=f"https://api.todoist.com/rest/v1/tasks/{id}"
    elif endpoint == "comments" and method == "POST":
        url="https://api.todoist.com/rest/v1/comments"
    response = requests.request(method,url,headers=headers,json=data)
    return response

def epoch_to_format(format,epoch):
    '''Convert  epoch to given format''' 
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
