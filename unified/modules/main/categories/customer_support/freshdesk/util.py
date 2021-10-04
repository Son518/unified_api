import json
import base64
import requests
from freshdesk.api import API


def get_freshdesk_client(headers):
    """
    returns freshdesk api client
    """
    client = API(f"{headers['domain']}.freshdesk.com",
                 headers["api_key"], version=2)
    return client


def rest(method, category, headers, payload):
    """
    returns result of rest calls
    """

    # :X is deafault value used for making basic key
    api_key = (headers["api_key"])+":X"
    api_bytes = api_key.encode('ascii')
    basic_apikey = (base64.b64encode(api_bytes)).decode("utf-8")

    # adding domain to base url
    domain = headers["domain"]
    base_url = f"https://{domain}.freshdesk.com/api/v2/discussions"

    # actual url builds here
    if category[0] == "forums":
        url = base_url+f"/categories/{category[1]}/forums"
    elif category[0] == "topics":
        url = base_url+f"/forums/{category[1]}/topics"
    elif category == "categories":
        url = base_url+"/categories"

    # required headers are prepared here
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {basic_apikey}'
    }
    response = requests.request(
        method, url, headers=headers, data=json.dumps(payload))
    return response
