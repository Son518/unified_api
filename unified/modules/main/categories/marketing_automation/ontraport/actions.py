import requests
from unified.core.actions import Actions
from marketing_automation.ontraport.entities.ontraport_contact import OntraportContact
import json


class OntraportActions(Actions):
    url = "https://api.ontraport.com/1/"

    def create_contact(self, context, payload):
        """Create a new contact"""

        if context.get('headers').get('api_key') is None or context.get('headers').get('app_id') is None:
            raise Exception("Please provide Api-Key and Api-Appid")
        
        # Set headers
        headers = {
            "Api-Key": context.get('headers').get('api_key'),
            "Api-Appid": context.get('headers').get('app_id'),
            "Content-Type": "application/json"
        }

        response = requests.request("POST", f'{self.url}Contacts', headers=headers, data=payload).text
        response = json.loads(response)
        response = response["data"]
        return response


    # Update Contact
    def update_contact(self, context, payload):
        """Update a contact by Id"""

        if context.get('headers').get('api_key') is None or context.get('headers').get('app_id') is None:
            raise Exception("Please provide Api-Key and Api-Appid")
        
        # Set headers
        headers = {
            "Api-Key": context.get('headers').get('api_key'),
            "Api-Appid": context.get('headers').get('app_id'),
            "Content-Type": "application/json"
        }
        payload["id"] = payload.get("contact_id")
        response = requests.request("PUT", f'{self.url}Contacts', headers=headers, data=payload).text
        response = json.loads(response)
        response = response["data"]["attrs"]
        return response