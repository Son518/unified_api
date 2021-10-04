import requests


def rest(method, url, api_key, body=None):

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    return requests.request(method, url, headers=headers, json=body)
