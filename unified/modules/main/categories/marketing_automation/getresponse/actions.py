from requests.models import Response
import requests
from unified.core.actions import Actions
from marketing_automation.getresponse.entities.getresponse_contact import GetresponseContact
from marketing_automation.getresponse.entities.getresponse_newsletter import GetresponseNewsletter
from getresponse.client import GetResponse
from marketing_automation.getresponse import util
import json
import requests


class GetresponseActions(Actions):

    url = f"https://api.getresponse.com/v3/"

    def create_contact(self, context, payload):
        """ Create a contact"""

        contact = GetresponseContact(**payload)
        data = {
            	"name": contact.name,
            	"campaign": {
            		"campaignId": contact.list_id
            	},
            	"email": contact.email
            }
        if contact.tags is not None:
            data["tags"] = [{"tagId": contact.tags}]
            
        getresponse = util.getresponse_authentication(context["headers"])
        contact = getresponse.create_contact(data)
        
        return json.dumps(contact)

    def create_newsletter(self, context, payload):
        """ Create a news letter"""

        newsletter_data= GetresponseNewsletter(**payload)

        # sendOn must take current time or above
        data = {
            "content":{
                "html": newsletter_data.content_html,
                "plain": newsletter_data.content_plain
            },
            "flags":[
                newsletter_data.flags
            ],
            "name": newsletter_data.name,
            "subject": newsletter_data.subject,
            "type": newsletter_data.type,
            "fromField":{
                "fromFieldId": newsletter_data.from_field
            },
            "campaign":{
                "campaignId": newsletter_data.list_id
            },
            "sendSettings":{
                "selectedCampaigns":[newsletter_data.list_id]
            },
            "sendOn":newsletter_data.send_on
        }

        headers = {
            "X-Auth-Token" : f'api-key {context["headers"]["api_key"]}',
            "Content-Type" : "application/json"
        }
        response = requests.request("POST", f'{self.url}newsletters', json= data, headers= headers).text
        return response

    def remove_contact(self, context, payload):
        """ Remove contact"""

        getresponse = util.getresponse_authentication(context["headers"])
        contact = GetresponseContact(**payload)
        contact = getresponse.delete_contact(contact.contact_id)
        return json.dumps(contact)

    def update_contact(self, context, payload):
        """ Update contact"""

        contact= GetresponseContact(**payload)

        data = {}
        if contact.name is not None:
            data["name"] = contact.name
        if contact.campaignId is not None:
            data["campaign"]= {"campaignId":contact.campaignId}
        if contact.comment is not None:
            data["note"] = contact.comment
        if contact.tags is not None:
            data["tags"] = {"tagId":contact.tags}
            
        headers = {
            "X-Auth-Token" : f'api-key {context["headers"]["api_key"]}',
            "Content-Type" : "application/json"
        }
        response = requests.request("POST", f'{self.url}contacts/{contact.contact_id}', json= data, headers= headers).text
        return response          