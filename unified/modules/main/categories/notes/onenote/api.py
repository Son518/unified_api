import json
from notes.onenote import util
import requests

class OnenoteApi:

    def profile(self, context, params):
        '''Details of authenticated user'''

        access_token = util.get_access_token(context['headers'])
        url = 'https://graph.microsoft.com/v1.0/me'
        response = json.loads(util.rest("GET",url,access_token).text)
        profile = {
            'id':response['id'],
            'email':response['userPrincipalName'],
            'name':response['displayName']
        }
        return profile