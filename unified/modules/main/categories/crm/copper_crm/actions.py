from crm.copper_crm import util
from unified.core.actions import Actions
from crm.entities.deal import Deal
from crm.copper_crm.entities.copper_contact import CoppercrmContact
from crm.copper_crm.entities.copper_lead import CoppercrmLead
from crm.copper_crm.entities.copper_account import CoppercrmAccount
from crm.copper_crm.entities.copper_task import CoppercrmTask
from crm.copper_crm.entities.copper_activity import CoppercrmActivity
from crm.copper_crm.entities.copper_deal import CoppercrmDeal
import json


class CoppercrmAction:
    def create_contact(self, context, payload):
        '''Creates a new Person.'''

        headers = context['headers']
        contact = CoppercrmContact(**payload)

        url = 'people'
        contact = {
            "name": f'{contact.first_name} {contact.last_name}',
            "emails": [
                {
                    "email": contact.email,
                    "category": "work"
                }
            ],
            "address": {
                "street": contact.mailing_street,
                "city": contact.mailing_city,
                "state": contact.mailing_state,
                "postal_code": contact.mailing_zip,
                "country": contact.mailing_country
            },
            "phone_numbers": [
                {
                    "number": contact.business_phone,
                    "category": "mobile"
                }
            ]
        }

        response = util.rest("POST", url, headers, contact)
        response = json.loads(response.text)
        response["contact_id"] = response.get("id")

        return response

    def create_task(self, context, payload):
        '''Creates a new Task.'''

        headers = context['headers']
        task = CoppercrmTask(**payload)
        url = 'tasks'
        task = {
            "name": task.name,
            "related_resource": {
                "id": task.project_id,
                "type": "project"
            },
            "assignee_id": task.owner_id,
            "due_date": task.due_date,
            "status": task.status,
            "details": task.description,
        }
        response = util.rest("POST", url, headers, task)

        return json.loads(response.text)

    def update_contact(self, context, payload):
        '''updates a Task.'''

        headers = context['headers']
        contact = CoppercrmContact(**payload)
        url = f'people/{contact.contact_id}'
        contact = {
            "name": f'{contact.first_name} {contact.last_name}',
            "emails": [
                {
                    "email": contact.email,
                    "category": "work"
                }
            ],
            "address": {
                "street": contact.mailing_stree,
                "city": contact.mailing_city,
                "state": contact.mailing_state,
                "postal_code": contact.mailing_zip,
                "country": contact.mailing_country
            },
            "phone_numbers": [
                {
                    "number": contact.business_phone,
                    "category": "mobile"
                }
            ]
        }

        response = util.rest("PUT", url, headers, contact)

        return json.loads(response.text)

    def create_lead(self, context, payload):
        '''Creates a new Lead.'''

        headers = context['headers']
        lead = CoppercrmLead(**payload)
        url = 'leads'
        lead_body = {
            "name": f'{lead.first_name} {lead.last_name}',
            "emails": [
                {
                    "email": lead.email,
                    "category": "work"
                }
            ],
            "address": {
                "street": lead.street,
                "city": lead.city,
                "state": lead.state,
                "country": lead.country_id
            },
            "phone_numbers": [
                {
                    "number": lead.phone,
                    "category": "mobile"
                }
            ]
        }

        response = util.rest("POST", url, headers, lead_body)
        response = json.loads(response.text)
        response["id"] = response.get("id")
        return response

    def update_lead(self, context, payload):
        '''Updates an Lead based off a match criteria..'''
        headers = context['headers']
        lead = CoppercrmLead(**payload)
        url = f'leads/{lead.lead_id}'
        lead_body = {
            "name": f'{lead.first_name} {lead.last_name}',
            "emails": [
                {
                    "email": lead.email,
                    "category": "work"
                }
            ],
            "address": {
                "street": lead.street,
                "city": lead.city,
                "state": lead.state,
                "country": lead.country_id
            },
            "phone_numbers": [
                {
                    "number": lead.phone,
                    "category": "mobile"
                }
            ]
        }

        response = util.rest("PUT", url, headers, lead_body)

        return json.loads(response.text)

    def create_organization(self, context, payload):
        '''Creates a new Opportunity.'''

        headers = context['headers']
        organization = CoppercrmAccount(**payload)
        url = 'companies'

        organization_body = {
            "name": organization.name,
            "address": {
                "street": organization.mailing_street,
                "city": organization.mailing_city,
                "state": organization.mailing_state,
                "postal_code": organization.mailing_zip,
                "country": organization.mailing_country
            },
            "email_domain": organization.email_domain,
            "details": organization.description,
            "phone_numbers": [
                {
                    "number": organization.phone,
                    "category": "work"
                }
            ]
        }

        response = util.rest("POST", url, headers, organization_body)
        return response.text, response.status_code

    def create_account(self, context, payload):
        """ Create account"""

        return self.create_organization(context, payload)

    def create_company(self, context, payload):
        """ Create company"""

        return self.create_organization(context, payload)

    def update_organization(self, context, payload):
        '''Updates a Company depending on the match criteria.'''

        headers = context['headers']
        organization = CoppercrmAccount(**payload)
        url = f'companies/{organization.account_id}'

        organization_body = {
            "name": organization.name,
            "address": {
                "street": organization.mailing_street,
                "city": organization.mailing_city,
                "state": organization.mailing_state,
                "postal_code": organization.mailing_zip,
                "country": organization.mailing_country
            },
            "email_domain": organization.email_domain,
            "details": organization.description,
            "phone_numbers": [
                {
                    "number": organization.phone,
                    "category": "work"
                }
            ]
        }

        response = util.rest("PUT", url, headers, organization_body)
        return response.text, response.status_code

    def update_account(self, context, payload):
        """ Upload Account"""

        return self.update_organization(context, payload)

    def update_company(self, context, payload):
        """ Upload Company"""

        return self.update_organization(context, payload)

    def create_deal(self, context, payload):
        '''Creates a new Opportunity.'''

        headers = context['headers']
        deal = CoppercrmDeal(**payload)
        url = 'opportunities'
        deal_body = {
            "name": deal.name,
            "primary_contact_id": deal.contact_id,
            "close_date": deal.close_date,
            "monetary_value": deal.value,
            "monetary_unit": deal.currency_id,
            "details": deal.description,
            # "assignee_id": deal.owner_id
        }
        response = util.rest("POST", url, headers, deal_body)
        return response.text, response.status_code

    def create_opportunity(self, context, payload):
        """ Create Opportunity"""

        return self.create_deal(context, payload)

    def update_deal(self, context, payload):
        '''Updates an Opportunity based off of a match criteria.'''

        headers = context['headers']
        deal = CoppercrmDeal(**payload)
        url = f'opportunities/{deal.deal_id}'
        deal_body = {
            "name": deal.name,
            "primary_contact_id": deal.contact_id,
            "close_date": deal.close_date,
            "monetary_value": deal.value,
            "monetary_unit": deal.currency_id,
            "details": deal.description,
            "assignee_id": deal.owner_id,
        }
        response = util.rest("PUT", url, headers, deal_body)

        return response.text, response.status_code

    def update_opportunity(self, context, payload):
        """ Update Opportunity"""

        return self.update_deal(context, payload)

    def create_activity(self, context, payload):
        '''Logs a new Activity on a Person, Company, Opportunity, or Lead.'''

        headers = context['headers']
        activity = CoppercrmActivity(**payload)
        url = "activities"
        activity_body = {
            "parent": {
                "type": activity.parent_type,
                "id": activity.parent_id
            },
            "type": {
                "category": activity.category_type,
                "id": activity.category_id
            },
            "details": activity.description
        }
        response = util.rest("POST", url, headers, activity_body)
        return response.text, response.status_code
