from marketing_automation.entities.object import Object
import requests
import json

class OntraportApi():

    url = "https://api.ontraport.com/1/"

    def contact(self, context, params):
        """Retrieve contact by id"""

        # Set headers
        headers = {
            "Api-Key": context.get('headers').get('api_key'),
            "Api-Appid": context.get('headers').get('app_id')
        }

        response = requests.request("GET", f'{self.url}Contact?id={params.get("id")}', headers= headers).text
        return json.loads(response)


    def objects(self, context, params):
        """Retrieve all objects"""

        # Set headers
        headers = {
            "Api-Key": context.get('headers').get('api_key'),
            "Api-Appid": context.get('headers').get('app_id')
        }

        params = {
            "objectID": params.get("objectID", 0),
            "sortDir": params.get("sortDir", "desc")
        }

        response = requests.request("GET", f'{self.url}objects', headers= headers, params=params).text
        return json.loads(response)


    def objects_by_tag_name(self, context, params):
        """List objects with certian tag"""

        # Set headers
        headers = {
            "Api-Key": context.get('headers').get('api_key'),
            "Api-Appid": context.get('headers').get('app_id')
        }

        params = {
            "objectID": params.get("objectID", 0),
            "tag_id": params.get("tag_id", 1),
            "listFields": params.get("listFields", None),
        }

        response = requests.request("GET", f'{self.url}objects/tag', headers= headers, params=params).text
        return json.loads(response)

    def verify(self, context, params):
        """Verify the app"""

        # Set headers
        headers = {
            "Api-Key": context.get('headers').get('api_key'),
            "Api-Appid": context.get('headers').get('app_id')
        }

        response = requests.request("GET", f'{self.url}CreditCards?range=1', headers= headers).text
        return json.loads(response)