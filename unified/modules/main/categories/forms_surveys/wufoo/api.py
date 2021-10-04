import json
import requests
from . import util
import logging


class WufooAPI():

    def entry_by_id(self, context, params):
        """ Get form submission"""
        
        logging.info(f'params -- {params}')
        logging.info(f'Context -- {context}')
        
        domain = context["headers"]["domain"]
        identifier = params.get("form_hash")
        entry_id = params.get("entry_id")
        response = util.rest("GET", f'https://{domain}.wufoo.com/api/v3/forms/{identifier}/entries.json?Filter1=EntryId+Is_equal_to+{entry_id}', context)
        return json.loads(response.text)

    def profile(self, context, params):
        """Get profile details"""

        domain = context["headers"]["domain"]
        response_data = util.rest("GET", f'https://{domain}.wufoo.com/api/v3/users.json', context)
        response = json.loads(response_data.text)
        response = response["Users"][0]
        if response_data.ok:
            data = {
                "id": response["Hash"],
                "name": response["User"],
                "email": response["Email"]
            }
            return data
        return response
    
    def verify(self, context, params):
        """Verify the app"""

        return self.profile(context, params)