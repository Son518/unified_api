from onepagecrm import OnePageCRMAPI
from unified.core.actions import Actions
from crm.onepagecrm.entities.onepagecrm_contact import OnepagecrmContact


class OnepagecrmActions(Actions):

    def create_contact(self, context, contact_entity):
        ''' creates new contact'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contact_schema = OnepagecrmContact(**contact_entity)
        contact_data = {
                        'first_name': contact_schema.first_name,
                        'last_name': contact_schema.last_name,
                        'job_title': contact_schema.job_title,
                        'company_name': contact_schema.company,
                        "address_list": [{
                                        "address": contact_schema.address,
                                        "city": contact_schema.city,
                                        "country_code": contact_schema.country,
                                        "state": contact_schema.state,
                                        "type": "work",
                                        "zip_code": contact_schema.zip
                                        }],
                        "emails": [{
                                    "type": "work",
                                    "value": contact_schema.email
                                    }],
                        "urls": [{
                                    "type": "website",
                                    "value": contact_schema.website
                                }],
                        "tags": [contact_schema.tags]
                        }

        contact = client.post('contacts', contact_data)['contact']
        contact["contact_id"] = contact["id"]

        return contact

    def update_contact(self, context, contact_entity):
        ''' updates existing contact'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contact_schema = OnepagecrmContact(**contact_entity)
        contact_data = {'first_name': contact_schema.first_name,
                        'last_name': contact_schema.last_name,
                        'job_title': contact_schema.job_title,
                        'company_name': contact_schema.company,
                        "address_list": [{
                                        "address": contact_schema.address,
                                        "city": contact_schema.city,
                                        "country_code": contact_schema.country,
                                        "state": contact_schema.state,
                                        "type": "work",
                                        "zip_code": contact_schema.zip
                                        }],
                        "emails": [{
                                    "type": "work",
                                    "value": contact_schema.email
                                   }],
                        "urls": [{
                                    "type": "website",
                                    "value": contact_schema.website
                                }],
                        "tags": [contact_schema.tags]
                        }
        contact = client.put('contacts', contact_schema.contact_id, contact_data)

        return contact

    def create_note(self, context, contact_entity):
        ''' create note to contact'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contact_schema = OnepagecrmContact(**contact_entity)
        contact_data = {
                        'text': contact_schema.text,
                        'contact_id': contact_schema.contact_id
                        }
        contact = client.post('notes', contact_data)

        return contact

    def update_note(self, context, contact_entity):
        ''' updates existing note'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contact_schema = OnepagecrmContact(**contact_entity)
        contact_data = {
                        'text': contact_schema.text,
                        'contact_id': contact_schema.contact_id
                        }
        contact = client.put('notes', contact_schema.note_id, contact_data)

        return contact
