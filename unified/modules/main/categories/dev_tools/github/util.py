import json
import requests


def rest(method, url, access_token, body=None):
    """ Send REST request and returns response  """

    headers = {
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"token {access_token}"
    }
    BASE_URL = f"https://api.github.com/{url}"

    print(method, BASE_URL, headers, body)

    response = requests.request(method, BASE_URL, headers=headers, json=body)
    return response
