from . import util
from unified.core.actions import Actions
import json
import requests
import logging


class WufooActions(Actions):

    def create_entry(self, context, payload):
        """ Create entry of the form
        
            Note: File upload requires paid account
        """
                
        payload_type = type(payload)
        logging.info(f'Payload type {payload_type}')
        logging.info(f'Payload -- {payload}')
        logging.info(f'Context -- {context}')

        domain = context["headers"]["domain"]
        form_id = payload.get("form_id")          
        field_json = self.get_fields_data(domain, form_id, context)
        data = {}
        if payload.get("first_name")!= None:
            data[field_json["First"]] = payload["first_name"]

        if payload.get("last_name")!= None:
            data[field_json["Last"]] = payload["last_name"]
        
        if payload.get("email")!= None:
            data[field_json["Email"]] = payload["email"]

        if payload.get("phone_number")!= None:
            data[field_json["Phone Number"]] = payload["phone_number"]

        response = util.rest("POST", f'https://{domain}.wufoo.com/api/v3/forms/{form_id}/entries.json', context, data)
        return json.loads(response.text)

    def create_entry_legacy(self, context, payload):
        """ Create legacy entry form"""

        payload_type = type(payload)
        logging.info(f'Payload type {payload_type}')
        logging.info(f'Payload -- {payload}')
        logging.info(f'Context -- {context}')
        return self.create_entry(context, payload)

    def get_fields_data(self, domain, form_id, context):
        """ Get field data"""

        fields_data = util.rest("GET", f'https://{domain}.wufoo.com/api/v3/forms/{form_id}/fields.json', context)
        fields_data = json.loads(fields_data.text)
        fields = fields_data["Fields"]
        field_obj = {}
        for field in fields:
            field_obj[field["Title"]] = field["ID"]
            if "SubFields" in field:
                for sub_field in field["SubFields"]:
                    field_obj[sub_field["Label"]] = sub_field["ID"]
        return field_obj