from datetime import datetime, timezone
import requests
import json


def rest(method, endpoint, headers, data={}, id=None):

    if endpoint == "leads" and method == "POST":
        url = f"https://{headers['domain']}.nocrm.io/api/v2/leads"
    elif endpoint == "comments":
        url = f"https://{headers['domain']}.nocrm.io/api/v2/leads/{id}/comments"
    elif (endpoint == "tags" or endpoint == "leads") and method == "PUT":
        url = f"https://{headers['domain']}.nocrm.io/api/v2/leads/{id}"
    elif endpoint == "rows" and method == "POST":
        url = f"https://{headers['domain']}.nocrm.io/api/v2/spreadsheets/{id}/rows"
    elif endpoint == "leads" and method == "GET":
        url = f"https://{headers['domain']}.nocrm.io/api/v2/leads?user_id={data['email']}"
        data = {}
    elif endpoint == "prospects" and method == "GET":
        url = f"https://{headers['domain']}.nocrm.io/api/v2/spreadsheets?title={data['title']}"
        data = {}

    headers = {
        "X-API-KEY": headers["api_key"],
        "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=data)


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)


def date_format_to_epoch(date):
    ''' convert date format to epoch'''
    return date.strftime("%Y-%m-%dT%H:%M:%SZ")
