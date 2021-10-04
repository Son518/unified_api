import requests
import json


class GetResponseApi():

    url = f"https://api.getresponse.com/v3/"

    def contact(self, context, params):
        """ Retrieve contact by id"""

        headers = {
            "X-Auth-Token" : f'api-key {context["headers"]["api_key"]}',
            "Content-Type" : "application/json"
        }
        response = requests.request("GET", f"{self.url}contacts/{params.get('contact_id')}", headers=headers).text
        return response

    def list(self, context, params):
        """ Retrieve List or campaign by id"""

        headers = {
            "X-Auth-Token" : f'api-key {context["headers"]["api_key"]}',
            "Content-Type" : "application/json"
        }
        response = requests.request("GET", f"{self.url}campaigns/{params.get('list_id')}", headers=headers).text
        return response

    def profile(self, context, params):
        """ Get profile details"""

        headers = {
            "X-Auth-Token" : f'api-key {context["headers"]["api_key"]}',
            "Content-Type" : "application/json"
        }
        response_data = requests.request("GET", f"{self.url}accounts", headers=headers)
        response = json.loads(response_data.text)
        if response_data.ok:
            data = {
                "id": response["accountId"],
                "name": response["firstName"]+" "+response["lastName"],
                "email": response["email"]
            }
            return data
        return response

    def verify(self, context, params):
        """Verify the app"""

        return self.profile(context, params)