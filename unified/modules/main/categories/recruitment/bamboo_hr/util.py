import json
import base64
import requests

from flask import Response, request
from datetime import datetime, timezone

def get_bamboo_request(method: str, url: str, bamboo_headers, body=None, params=None, files=None):

    API_URL = "https://{api_key}:x@api.bamboohr.com/api/gateway.php/{domain}/v1".format(api_key=bamboo_headers["api_key"],
        domain=bamboo_headers["domain"])
    auth_str = bamboo_headers["username"]+":"+bamboo_headers["password"]
    encoded_str = base64.b64encode(auth_str.encode("utf-8"))
    encoded_auth = str(encoded_str, "utf-8")

    bamboo_headers = {'Authorization' : encoded_auth,
                     "Accept" : "application/json"
               }
    final_url = API_URL + url
    if files:
        return requests.request(method, final_url, headers=bamboo_headers, data=body, files=files)
    else: return requests.request(method, final_url, headers=bamboo_headers, json=body, params=params)

def epoch_to_format(format,epoch):
    '''Convert epoch to given format'''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

def create_employee_payload(task_schema):
    task_data = {
        "firstName": task_schema.first_name,
        "lastName": task_schema.last_name,
        "dateOfBirth": task_schema.date_of_birth,
        "address1": task_schema.address1,
        "address2": task_schema.address2,
        "city": task_schema.city,
        "state": task_schema.state,
        "zipcode": task_schema.zip_code,
        "country": task_schema.country,
        "hireDate": task_schema.hire_date,
        "bestEmail": task_schema.work_email
    }
    return task_data

def date_to_epoch(date):
    if not(date is None or "-" in date):
        format = "%Y-%m-%d"
        date = epoch_to_format(format, date)
        return date
