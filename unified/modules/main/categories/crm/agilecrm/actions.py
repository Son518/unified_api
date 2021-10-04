from agilecrm.client import Client
from unified.core.actions import Actions
from crm.agilecrm.entities.agilecrm_contact import AgilecrmContact
from crm.agilecrm.entities.agilecrm_deal import AgilecrmDeal
from crm.agilecrm.entities.agilecrm_task import AgilecrmTask
from crm.agilecrm.util import agilecrm_authentication
from crm.agilecrm.entities.agilecrm_event import AgilecrmEvent
from crm.agilecrm.entities.agilecrm_tag import AgilecrmTag
from crm.agilecrm import util
import json


class AgilecrmActions(Actions):

    def create_contact(self, context, contact_entity):
        ''' creates new contact'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        contact_schema = AgilecrmContact(**contact_entity)

        # address for creating contact is taking string format of dictionary took separetly dumped with json
        address={
                "address":contact_schema.mailing_street,
                "city":contact_schema.mailing_city,
                "state":contact_schema.mailing_state,
                "zip":contact_schema.mailing_zip,
                "country":contact_schema.mailing_country
                }
        contact_data = {
            "star_value": contact_schema.star_value,
            "lead_score": contact_schema.lead_score,
            "tags": contact_schema.tags,
            "properties": [
                {
                    "type": "SYSTEM",
                    "name": "first_name",
                    "value": contact_schema.first_name
                },
                {
                    "type": "SYSTEM",
                    "name": "last_name",
                    "value": contact_schema.last_name
                },
                {
                    "type": "SYSTEM",
                    "name": "company",
                    "value": contact_schema.company
                },
                {
                    "type": "SYSTEM",
                    "name": "title",
                    "value": contact_schema.title
                },
                {
                    "type": "SYSTEM",
                    "name": "email",
                    "subtype": "work",
                    "value": contact_schema.email
                },
                {
                    "type": "SYSTEM",
                    "name": "address",
                    "value": json.dumps(address)
                },
                {
                    "type": "CUSTOM",
                    "name": "phone",
                    "value": contact_schema.phone
                },
                {
                    "type": "CUSTOM",
                    "name": "website",
                    "value": contact_schema.business_website
                }
            ]
        }
        response = agilecrm_client.create_contact(contact_data)
        return response

    def create_deal(self, context, deal_entity):
        ''' creates new deal'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        deal_schema = AgilecrmDeal(**deal_entity)
        deal_data = {
            "name": deal_schema.name,
            "expected_value": deal_schema.value,
            "probability": deal_schema.probability,
            "close_date": deal_schema.end_date,
            "milestone": deal_schema.milestone,
            "contact_ids":
                [deal_schema.owner],
            "custom_data": [
                {
                    "name": "Group Size",
                    "value": deal_schema.value
                }
            ]
        }
        response = agilecrm_client.create_deal(deal_data)
        return response

    def create_note(self, context, note_entity):
        ''' creates new note'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        note_schema = AgilecrmContact(**note_entity)
        note_data = {
            "subject": note_schema.subject,
            "description": note_schema.description,
            "contact_ids": [
                note_schema.contact_id
            ]
        }

        response = agilecrm_client.create_contact_note(note_data)
        return response

    def update_contact(self, context, contact_entity):
        ''' updates contact'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        contact_schema = AgilecrmContact(**contact_entity)

        # address for creating contact is taking string format of dictionary took separetly dumped with json
        address={
                "address":contact_schema.mailing_street,
                "city":contact_schema.mailing_city,
                "state":contact_schema.mailing_state,
                "zip":contact_schema.mailing_zip,
                "country":contact_schema.mailing_country
                }
        contact_data = {
            "id": contact_schema.contact_id,
            "properties": [
                {
                    "type": "SYSTEM",
                    "name": "first_name",
                    "value": contact_schema.first_name
                },
                {
                    "type": "SYSTEM",
                    "name": "last_name",
                    "value": contact_schema.last_name
                },
                {
                    "type": "SYSTEM",
                    "name": "company",
                    "value": contact_schema.company
                },
                {
                    "type": "SYSTEM",
                    "name": "title",
                    "value": contact_schema.title
                },
                {
                    "type": "SYSTEM",
                    "name": "email",
                    "subtype": "work",
                    "value": contact_schema.email
                },
                {
                    "type": "SYSTEM",
                    "name": "address",
                    "value":json.dumps(address)
                },
                {
                    "type": "CUSTOM",
                    "name": "phone",
                    "value": contact_schema.business_phone
                },
                {
                    "type": "CUSTOM",
                    "name": "website",
                    "value": contact_schema.business_website
                }
            ]

        }

        response = agilecrm_client.update_contact(contact_data)
        return response

    def create_organization(self, context, contact_entity):
        ''' creates new organization'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        contact_schema = AgilecrmContact(**contact_entity)

        # address for creating contact is taking string format of dictionary took separetly dumped with json
        address={
                "address":contact_schema.mailing_street,
                "city":contact_schema.mailing_city,
                "state":contact_schema.mailing_state,
                "zip":contact_schema.mailing_zip,
                "country":contact_schema.mailing_country
                }
        company_data = {
            "type": contact_schema.company,
            "tags": contact_schema.tags,
            "properties": [
                {
                    "type": "CUSTOM",
                    "name": "Company Type",
                    "value": contact_schema.company_type
                },
                {
                    "type": "SYSTEM",
                    "name": "name",
                    "value": contact_schema.company_name
                },
                {
                    "type": "SYSTEM",
                    "name": "url",
                    "value": contact_schema.company_url
                },
                {
                    "name": "email",
                    "value": contact_schema.email,
                    "subtype": ""
                },
                {
                    "name": "phone",
                    "value": contact_schema.business_phone,
                    "subtype": ""
                },
                {
                    "name": "website",
                    "value": contact_schema.business_website,
                    "subtype": "LINKEDIN"
                },
                {
                    "name": "address",
                    "value": json.dumps(address),
                    "subtype": "office"
                }
                
            ]
        }
        response = agilecrm_client.create_contact(company_data)
        return response

    def create_task(self, context, task_entity):
        ''' creates new task'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        task_schema = AgilecrmTask(**task_entity)
        task_data = {
            "subject": task_schema.subject,
            "progress": task_schema.progress,
            "is_complete": task_schema.is_complete,
            "priority_type": task_schema.priority,
            "type": task_schema.task_type,
            "status": task_schema.status,
            "due": task_schema.end_date,
            "properties": [
                {
                    "name": "email",
                    "value": task_schema.email,
                    "subtype": ""
                }
            ]

        }
        response = agilecrm_client.create_task(task_data)
        return response

    def create_event(self, context, event_entity):
        ''' creates new event'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        event_schema = AgilecrmEvent(**event_entity)
        event_data = {
            "event_name": event_schema.event_name,
            "priority_type": event_schema.priority,
            "start": event_schema.start_date_time,
            "end": event_schema.end_date_time
        }
        response = agilecrm_client.create_event(event_data)
        return response

    def add_tag_to_contact(self, context, tag_entity):
        ''' adds tag to contact'''

        # add_tag_to_contact done using api calls as sdk support not given for this action
        domain = context["headers"]["domain"]
        url = f"https://{domain}.agilecrm.com/dev/api/contacts/email/tags/add"
        tag_schema = AgilecrmTag(**tag_entity)

        tag_data = {"email": tag_schema.contact_email,
                    "tags": tag_schema.tags}
        response = util.rest(
            url, context["headers"], "POST", tag_data, "application/json")
        return (response)
