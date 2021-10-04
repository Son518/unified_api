import json
from unified.core.auth import Auth
from datetime import datetime, timezone


def get_xero_client(headers):

    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers.get('refresh_token'),
        "refresh_url": headers.get('redirect_url') or headers.get('token_url')
    }
    token = Auth().get_oauth2_token(auth_info)
    
    # TODO: Need to update refresh token every time in DB. Otherwise it will be expaire with in 30min
    return json.loads(token).get("access_token")
    

def epoch_to_format(format,epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)