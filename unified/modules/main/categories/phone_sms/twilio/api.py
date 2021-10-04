import json
from phone_sms.twilio import util
import requests
from twilio.rest import Client

class TwilioApi:

    def verify(self,context,params):

        client = Client(context["headers"]["auth_sid"], context["headers"]["auth_token"])
        accounts = client.api.accounts.list(limit=10)
        for record in accounts:
            return{
                    'name':record.friendly_name,
                    'token':record.auth_token,
                    'id':record.sid
                }
    
    def profile(self, context, params):
        '''  get call to show authenticated user information'''

        client = Client(context["headers"]["auth_sid"], context["headers"]["auth_token"])
        account = client.api.accounts(context["headers"]["auth_sid"]).fetch()
        profile = {
                    'id':account.sid,
                    'name':account.friendly_name
                }
        return profile