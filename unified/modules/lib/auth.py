from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import requests
import jwt
import base64
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
import json
from unified.default_settings import PROJECT_JWT_SECRET,DB_CONFIG
from flask_httpauth import HTTPTokenAuth

proj_auth = HTTPTokenAuth(scheme='Bearer')


class Auth():
    """docstring for auth"""

    # def __init__(self):
    #     super(auth, self).__init__()

    def token_saver(self, token=None):
        logger.info("token to be saved", token)

    def get_auth(self, auth):
        type = auth['type']

        if type == 'basic':
            logger.info("Doing basic ", auth)
            user = auth['basic']['user']
            password = auth['basic']['password']
            return HTTPBasicAuth(user, password)

        if type == 'digest':
            logger.info("Doing digest ", auth)
            user = auth['basic']['user']
            password = auth['basic']['password']
            return HTTPDigestAuth(user, password)

        if type == "oauth1":
            logger.info("OAuth1 ", auth)
            api_key = auth['oauth1']['api_key']
            api_secret = auth['oauth1']['api_secret']
            oauth_token = auth['oauth1']['oauth_token']
            oauth_token_secret = auth['oauth1']['oauth_token_secret']
            return OAuth1(api_key, api_secret, oauth_token, oauth_token_secret)

        return None

    def get_headers(self, auth, content_type, url):
        type = auth['type']
        logger.info(type, url,auth)

        if "salesforce.com" in url:
            header = json.loads(self.get_oauth2_salesforce(auth))
            return {
                "Authorization": f"Bearer {header['access_token']}", 
                "Content-Type": "application/json"
            }
			
        if auth['type'] == "bearer":
            logger.info("Bearer", auth)
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
        logger.info("OAuth2", auth)
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

def verify_token(token):

    # Setup 500apps login
    if not token:
        return False

    from lib.DB import DB
    db = DB(DB_CONFIG)

    project = db.public_get_select(DB_CONFIG['database'], 'projects',
                                   '*', f"api_key='{token}'")
    if project is None or len(project) == 0:
        return False

    logger.info("Token")
    logger.info(token)

    return project

@proj_auth.verify_token
def verify_project_token(token):

    if not token:
        return False

    payload = jwt.decode(token, base64.b64decode(PROJECT_JWT_SECRET), algorithms=["HS256"])
    email = payload.get("email", None)
    domain_id = payload.get("tenant_id", None)
    user_id = payload.get("user_id", None)
    project_id = payload.get("project_id", None)

    # 0 (zero) is passed for project_id in plugins call
    if not (email and domain_id and user_id) and project_id is None:
        return False

    return {
        "email": email,
        "domain_id": domain_id,
        "user_id": user_id,
        "project_id": project_id,
        "token": token,
    }

