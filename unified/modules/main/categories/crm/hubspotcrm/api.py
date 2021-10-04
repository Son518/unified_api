import json
import requests
from crm.hubspotcrm import util
from crm.hubspotcrm.entities.hubspotcrm_contact import HubspotcrmContact


class HubspotcrmApi():

    def contacts(self, context, params):
        ''' returns list of contacts '''

        # context holds headers from request
        # params holds param values from request
        api_client = util.hubspot_client(context["headers"])
        contacts = api_client.crm.contacts.get_all()
        contact_value = []
        for contact in contacts:
            contact = contact.to_dict()
            contact_obj = HubspotcrmContact(contact_id=contact.get("id") ,
                                            email=contact.get("properties").get("email") ,
                                            first_name=contact["properties"].get("firstname"),
                                            last_name=contact["properties"].get("lastname"),

                                            # updated_at is datetime.datetime(YYYY,MM,DD,HH,MM,SS)
                                            updated_date=contact.get("updated_at").strftime(
                                                '%Y-%m-%dT%H-%M-%SZ'),

                                            # created_at is datetime.datetime(YYYY,MM,DD,HH,MM,SS) 
                                            created_date=contact.get("created_at").strftime(
                                                '%Y-%m-%dT%H-%M-%SZ') 
                                            )
            contact_value.append(contact_obj.__dict__)
        
        return json.dumps(contact_value)

    def contact(self, context, params):
        ''' returns a single contact  '''

        # context holds headers from request
        # params holds param values from request
        api_client = util.hubspot_client(context["headers"])
        contact = api_client.crm.contacts.basic_api.get_by_id(
            params["contact_id"])
        contact = contact.to_dict()
        contact_obj = HubspotcrmContact(contact_id=contact.get("id") ,
                                            email=contact.get("properties").get("email") ,
                                            first_name=contact["properties"].get("firstname"),
                                            last_name=contact["properties"].get("lastname"),

                                            # updated_at is datetime.datetime(YYYY,MM,DD,HH,MM,SS)
                                            updated_date=contact.get("updated_at").strftime(
                                                '%Y-%m-%dT%H-%M-%SZ'),

                                            # created_at is datetime.datetime(YYYY,MM,DD,HH,MM,SS) 
                                            created_date=contact.get("created_at").strftime(
                                                '%Y-%m-%dT%H-%M-%SZ') 
                                            )

        return contact_obj.__dict__
    
    def profile(self,context,params):
        """
        get call to show user authenticated information
        """
        url = "https://api.hubapi.com/crm/v3/owners/"
        querystring = {"limit":"100","archived":"false","hapikey":context["headers"]["api_key"]}
        headers = {'accept': 'application/json'}
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        profile = {
            'id':response['results'][0]['id'],
            'email':response['results'][0]['email'],
            'name':response['results'][0]['firstName']
        }
        return profile
    
    def verify(self,context,params):
        """
        get call to verify user authenticated information
        """
        api_client = util.hubspot_client(context["headers"])
        contact = api_client.crm.contacts.get_all()[0]
        return contact.to_dict()