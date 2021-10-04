import json
from requests.models import Response
from crm.nimble.entities.nimble_create_contact import NimbleContact
from crm.nimble.entities.nimble_create_task import NimbleTask
from core.actions import Actions
from crm.nimble import util

class NimbleActions(Actions):

    def create_contact(self, context, contact_payload):
        """ 
        Create contact 
        context holds the headers 
        contact_entity holds the request.body
        """
        contact_entity = NimbleContact(**contact_payload) 
        data = {
               "fields": {
                "parent company": [
                    { 
                        "modifier": "",
                        "value": contact_entity.company_name
                    }
                ],
                "twitter": [
                    {
                        "modifier": "",
                        "value": contact_entity.twitter
                    }
                ],
                "title": [
                    {
                        "modifier": "",
                        "value": contact_entity.title
                    }
                ],
                "last name": [
                    {
                        "modifier": "",
                        "value": contact_entity.last_name
                    }
                ],
                "URL": [
                    {
                        "modifier": "",
                        "value": contact_entity.url_work
                    }
                ],
                "linkedin": [
                    {
                        "modifier": "",
                        "value": contact_entity.linkedin
                    }
                ],
                "facebook": [
                    {
                        "modifier": "",
                        "value": contact_entity.facebook
                    }
                ],
                "first name": [
                    {
                        "modifier": "",
                        "value": contact_entity.first_name
                    }
                ],
                "birthday":[
                        {
                           "value": contact_entity.birthday,
                           "modifier":""
                        }
                    ],
                "address": [
                 {
                    "modifier": "",
                    "value": json.dumps({'city':contact_entity.address_city_home, 'street': contact_entity.address_street_home, 'zip': contact_entity.address_zip_home, 'country': contact_entity.address_country_home})
                   
                 }
                
                ],
                "email": [
                    {
                        "modifier": "",
                        "value": contact_entity.email_personal
                      
                    }
                ],
                "phone": [
                    {
                        "modifier": "",
                        "value": contact_entity.phone_mobile
                    }
                ],
                "description": [
                    {
                        "modifier": "",
                        "value": contact_entity.description_other
                    }
                ],
                "skype id": [
                    {
                        "modifier": "",
                        "value": contact_entity.skype_id
                        }
               ]
            },
                "record_type": "person",
                "tags": contact_entity.tags
           }
        response = util.rest("POST","contact",data,context["headers"]["api_key"])
        return json.dumps(response)
          
    def create_task(self, context, task_payload):
        """ 
        Create task
        context holds the headers 
        task_entity holds the request.body
        """
        task_entity = NimbleTask(**task_payload)
        data = {
                "due_date": task_entity.due_date,
                "notes": task_entity.notes,
                "subject": task_entity.subject
               }
        response = util.rest("POST","task",data,context["headers"]["api_key"])
        return json.dumps(response)