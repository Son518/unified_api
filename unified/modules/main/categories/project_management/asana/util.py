import asana
import json
from unified.core.auth import Auth
from flask import Response, request
from datetime import datetime, timezone

def get_asana_client(asana_headers):
    auth_info = {
        "client_id": asana_headers['client_id'],
        "client_secret": asana_headers['client_secret'],
        "token": asana_headers.get('refresh_token'),
        "refresh_url": asana_headers.get('token_url') or asana_headers.get('refresh_url')
    }
    token = Auth().get_oauth2_token(auth_info)
    # Invoking asana client for specific access token
    return asana.Client.access_token((json.loads(token))['access_token'])

def check_handshake():
    try:
        if request.headers.get('X-Hook-Secret'):
            result = {
                'X-Hook-Secret': request.headers.get('X-Hook-Secret')
            }
            return Response(headers=result)
    except Exception as err:
        pass # supress error - for test_suite, or probably log it.        
    return None

def epoch_to_format(format,epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
