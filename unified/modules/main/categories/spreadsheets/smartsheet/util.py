from unified.core.auth import Auth
import requests
import json
from flask import request, jsonify, Response


def get_access_token(headers):
    """ Returns new access token """

    auth_info = {
        "client_id": headers["client_id"],
        "client_secret": headers["client_secret"],
        "token": headers["token"],
        "refresh_url": headers["refresh_url"],
    }

    token = Auth().get_oauth2_token(auth_info)

    return (json.loads(token))['access_token']

def check_handshake():
    try:
        if request.headers.get('smartsheet-hook-challenge'):
            result = {
                'Smartsheet-Hook-Response': request.headers.get('smartsheet-hook-challenge'),
            }
            return Response(headers=result)
            # return jsonify(result)
    except Exception as err:
        pass # supress error - for test_suite, or probably log it.        
    return None


def rest(method, url, access_token, body=None):
    """ Send REST request and returns response  """

    headers = {
        "Accept": "application/json, */*",
        "content-type": "application/json; charset=utf-8",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
        "Authorization": f"Bearer {access_token}",
        "Prefer": "return=representation"
    }
    base_url = f"https://api.smartsheet.com/2.0/{url}"
    response = requests.request(method, base_url, headers=headers, json=body)

    return response
