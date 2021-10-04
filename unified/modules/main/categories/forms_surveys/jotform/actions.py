import json
import requests
import logging
from unified.core.actions import Actions
from forms_surveys.jotform.entities.jotform_form import JotFormForm


class JotFormActions(Actions):

    def create_form(self, context, payload):
        """ Create a form"""

        api_key = context['headers']['api_key']
        form_data = JotFormForm(**payload)

        payload_type = type(payload)
        logging.info(f'Payload type {payload_type}')
        logging.info(f'Payload -- {payload}')
        logging.info(f'Context -- {context}')

        data = {
            "properties[title]": form_data.form_title
        }

        logging.info(f'Body data - {data}')

        headers= {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        response = requests.request("POST", f"https://api.jotform.com/form?apiKey={api_key}", headers=headers, data=data).text 
        
        logging.info(f'Response -- {response}')
        
        return json.loads(response) 