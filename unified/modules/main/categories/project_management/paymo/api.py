import json
from project_management.paymo import util
import requests


class PaymoApi:

    def profile(self, context, params):
        '''Details of authenticated user'''
        access_token = util.get_basic_token(context["headers"])
        response = util.rest(
            "GET", "https://app.paymoapp.com/api/clients", access_token).text
        response = json.loads(response)['clients'][0]
        profile = {
            'id': response.get('id'),
            'email': response.get('email'),
            'name': response.get('name')
        }
        return profile

    def verify(self, context, params):

        access_token = util.get_basic_token(context["headers"])
        response = util.rest(
            "GET", "https://app.paymoapp.com/api/clients", access_token).text
        return json.loads(response)
