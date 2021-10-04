import json
from project_management.runrunit import util


class RunrunitApi:

    def profile(self, context, params):

        headers = context["headers"]

        response = json.loads(util.rest("GET", "users", headers).text)[0]

        profile = {
            'id': response.get('id'),
            'email': response.get('email') or None,
            'name': response.get('name') or None
        }
        return profile

    def verify(self, context, params):

        headers = context["headers"]

        response = util.rest("GET", "users", headers).text

        return response
