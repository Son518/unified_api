import json
from requests.models import Response
from unified.core.actions import Actions
from customer_support.drift import util
from customer_support.drift.entities.drift_contact import DriftContact

class DriftActions(Actions):
    
    def create_contact(self,context,contact_payload):
        """
        creates a contact 
        context holds the headers 
        contact_payloads holds the request.body  
        """
        contact_entity = DriftContact(**contact_payload)
        data={
            "attributes": {
                            "email": contact_entity.email_address,
                            "start_date": contact_entity.start_date,
                            "LastActive": contact_entity.last_active,
                            "name": contact_entity.name,    
                            "firstname": contact_entity.first_name, 
                            "lastname": contact_entity.last_name,
                            "LastContacted": contact_entity.last_contacted,
                            "country": contact_entity.country,
                            "state": contact_entity.state,
                            "city": contact_entity.city,
                            "PostalCode": contact_entity.pin_code,
                            "alias": contact_entity.alias,
                            "phone": contact_entity.phone,
                            "employmentTitle": contact_entity.employment_title,
                            "employmentRole": contact_entity.employment_role,
                            "employment_seniority": contact_entity.employment_seniority,
                        }
                    }
        response = util.rest("POST","contact",data,context["headers"]["access_token"])
        return json.loads(response)

    def update_contact(self,context,contact_payload):
        """
        updates a contact 
        context holds the headers 
        contact_payloads holds the request.body  
        """
        contact_entity = DriftContact(**contact_payload)
        update_obj={
                    "attributes":
                                {
                                "email": contact_entity.email_address,
                                "start_date": contact_entity.start_date,
                                "LastActive": contact_entity.last_active,
                                "name": contact_entity.name,    
                                "firstname": contact_entity.first_name, 
                                "lastname": contact_entity.last_name,
                                "LastContacted": contact_entity.last_contacted,
                                "country": contact_entity.country,
                                "state": contact_entity.state,
                                "city": contact_entity.city,
                                "PostalCode": contact_entity.pin_code,
                                "alias": contact_entity.alias,
                                "phone": contact_entity.phone,
                                "employmentTitle": contact_entity.employment_title,
                                "employmentRole": contact_entity.employment_role,
                                "employment_seniority": contact_entity.employment_seniority,
                                }
                            }
        response = util.rest("PATCH","update_contact",update_obj,context["headers"]["access_token"],contact_entity.contact_id)
        return json.loads(response)