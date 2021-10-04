from unified.core.actions import Actions
from forms_surveys.surveymonkey import util
from forms_surveys.surveymonkey.entities.surveymonkey_contact import SurveymonkeyContact
from forms_surveys.surveymonkey import util
import json
import requests


class SurveymonkeyActions(Actions):

    def create_contact(self, context, payload):
        """ Create contact"""

        access_token = context["headers"]["access_token"]
        payload_data = SurveymonkeyContact(**payload)

        data = {"first_name": payload_data.first_name, "last_name": payload_data.last_name}

        if payload_data.email is not None:
            data["email"] = payload_data.email

        if payload_data.phone_number is not None:
            data["phone_number"] = payload_data.phone_number
        
        # If contact_list_id is exists need to create contact to that list, else create a contact
        if payload_data.contact_list_id is not None:
            url = f"/contact_lists/{payload_data.contact_list_id}/contacts"
        else:
            url = f"/contacts"

        response = util.rest("POST", url, access_token, data).text
        return json.loads(response)