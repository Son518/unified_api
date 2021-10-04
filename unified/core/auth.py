from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
import json


class Auth():
    """docstring for auth"""

    # def __init__(self):
    #     super(auth, self).__init__()

    def token_saver(self, token=None):
        print("token to be saved", token)

    def get_auth(self, auth):
        type = auth['type']

        if type == 'basic':
            print("Doing basic ", auth)
            user = auth['basic']['user']
            password = auth['basic']['password']
            return HTTPBasicAuth(user, password)

        if type == 'digest':
            print("Doing digest ", auth)
            user = auth['basic']['user']
            password = auth['basic']['password']
            return HTTPDigestAuth(user, password)

        if type == "oauth1":
            print("OAuth1 ", auth)
            api_key = auth['oauth1']['api_key']
            api_secret = auth['oauth1']['api_secret']
            oauth_token = auth['oauth1']['oauth_token']
            oauth_token_secret = auth['oauth1']['oauth_token_secret']
            return OAuth1(api_key, api_secret, oauth_token, oauth_token_secret)

        return None

    def get_headers(self, auth, content_type, url):
        type = auth['type']
        print(type, url,auth)

        if "salesforce.com" in url:
            header = json.loads(self.get_oauth2_salesforce(auth))
            return {
                "Authorization": f"Bearer {header['access_token']}", 
                "Content-Type": "application/json"
            }
			
        if auth['type'] == "bearer":
            print("Bearer", auth)
            token = auth['bearer']['token']
            return {'Content-type': content_type, 'Accept': 'text/plain, application/json', 'Authorization': 'Bearer ' + token}

        if auth['type'] == "header":
            header1 = auth['header']['header1']
            header2 = auth['header']['header2']
            value1 = auth['header']['value1']
            value2 = auth['header']['value2']

            if header2:
                return {'Content-type': content_type, 'Accept': 'text/plain, application/json', header1: value1, header2: value2}

            if header1:
                return {'Content-type': content_type, 'Accept': 'text/plain, application/json', header1: value1}

        return {'Content-type': content_type, 'Accept': 'text/plain, application/json'}

    # todo Need to check how to extract token from OAuth2Session
    def get_oauth2_token(self, auth):
        body = f'''client_id={auth["client_id"]}&client_secret={auth["client_secret"]}&grant_type=refresh_token&refresh_token={auth["token"]}'''
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        token_response = requests.post(auth['refresh_url'], headers=headers, data=body)

        return token_response.text

    def get_oauth2_requests(self, auth):
        print("OAuth2", auth)
        client_id = auth['client_id']
        client_secret = auth['client_secret']
        refresh_url = auth['refresh_url']
        token_client = auth['token']
        extra = {
            'client_id': client_id,
            'client_secret': client_secret,
        }
        token = {
            'access_token': 'eswfld123kjhn1v5423',
            'refresh_token': token_client,
            'token_type': 'Bearer',
            'expires_in': '-30'
        }
        client = OAuth2Session(client_id, token=token, auto_refresh_url=refresh_url,
                               auto_refresh_kwargs=extra, token_updater=self.token_saver)
                               
        return client
