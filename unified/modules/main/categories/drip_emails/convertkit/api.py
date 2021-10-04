from drip_emails.entities.profile import Profile
from drip_emails.convertkit import util
import json


class CovertkitApi:
    def verify(self, context, params):
        ''''''
        
        headers = context['headers']
        url = f"account?api_secret={headers['api_secret']}"
        response_secret = util.rest("GET", url, context)
        if response_secret.status_code != 200:
            raise Exception("wrong api Secret")
        else:
            url = f"tags?api_key={headers['api_key']}"
            response = util.rest("GET", url, context)
        if response.status_code != 200:
            raise Exception("wrong api key")
        else:
            return {"response": "okay"}, 200

    def profile(self, context, params):
        '''get user details'''

        headers = context['headers']
        url = f"account?api_secret={headers['api_secret']}"
        response = util.rest("GET", url, context)
        response = json.loads(response.text)
        profile = Profile(
            name=response.get('name'),
            email=response.get('primary_email_address')
        )
        return profile.__dict__
