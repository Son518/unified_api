import json
from unified.core.actions import Actions
from marketing_automation.hubspot import util
from marketing_automation.hubspot.entities.hubspot_deal import HubspotDeal
from marketing_automation.hubspot.entities.hubspot_ticket import HubspotTicket
from marketing_automation.hubspot.entities.hubspot_product import HubspotProduct
from marketing_automation.hubspot.entities.hubspot_company import HubspotCompany
from marketing_automation.hubspot.entities.hubspot_contact import HubspotContact


class HubspotActions(Actions):
    def create_company(self, context, payload):
        '''Creates a new company.'''

        url = f'companies'
        company = HubspotCompany(**payload)
        request_body = self.get_company_body(company)
        response = util.rest("POST", url, context, request_body)
        return json.loads(response.text), response.status_code

    def get_company_body(self, company):
        request_body = {"properties": {
            "city": company.city,
            "domain": company.domain,
            "industry": company.industry,
            "name": company.name,
            "phone": company.phone,
            "state": company.state,
            "description": company.description,
            "numberofemployees": company.number_of_employess,
            "annualrevenue": company.annual_revenue
        }}
        return request_body

    def create_contact(self, context, payload):
        '''Adds a contact'''

        url = f'contacts'
        contact = HubspotContact(**payload)
        request_body = self.get_contact_body(contact)
        response = util.rest("POST", url, context, request_body)
        return json.loads(response.text), response.status_code

    def get_contact_body(self, contact):
        request_body = {
            "properties": {
                "email": contact.email_address,
                "firstname": contact.first_name,
                "lastname": contact.last_name,
                "phone": contact.phone_number,
                "jobtitle": contact.job_title,
                "lifecyclestage": contact.lifecycle_stage,
                "hs_lead_status": contact.lead_status.upper() if contact.lead_status else None
            }
        }
        return request_body

    def replace_lower(self, str):
        return str.replace(" ", "").lower()

    def create_deal(self, context, payload):
        '''Creates a Deal.'''

        url = 'deals'
        deal = HubspotDeal(**payload)
        request_body = self.get_deal_body(deal)
        response = util.rest("POST", url, context, request_body)
        return json.loads(response.text), response.status_code

    def get_deal_body(self, deal):
        request_body = {
            "properties": {
                "amount": deal.ammount,
                "closedate": deal.end_date,
                "dealname": deal.name,
                "hubspot_owner_id": deal.owner_id,
                "pipeline": deal.pipeline,
                "dealtype": self.replace_lower(deal.deal_type) if deal.deal_type else None,
                "hs_priority": self.replace_lower(deal.priority) if deal.priority else None,
            },
            "associations": {
                # vid is contact id
                "associatedVids": [
                    deal.contact_id
                ],
                "associatedCompanyIds": [
                    deal.company_id
                ]
            }
        }
        return request_body

    def create_product(self, context, payload):
        '''Creates a Product in HubSpot.'''

        url = "products"
        product = HubspotProduct(**payload)
        request_body = self.get_product_body(product)
        response = util.rest("POST", url, context, request_body)
        return json.loads(response.text), response.status_code

    def get_product_body(self, product):
        request_body = {
            "properties": {
                "description": product.description,
                "hs_cost_of_goods_sold": product.unit_price,
                "hs_recurring_billing_period": f"P{int(product.term)}M" if product.term else None,
                "hs_sku": product.sku,
                "name": product.product_name,
                "price": product.unit_cost,
                "hs_url": product.url,
                "hs_images": product.image,
                "hs_folder_id": product.folder_id,
            }
        }
        return request_body

    def create_ticket(self, context, payload):
        '''Creates a Ticket in HubSpot.'''

        url = 'tickets'
        ticket = HubspotTicket(**payload)
        request_body = self.get_ticket_body(ticket)
        response = util.rest("POST", url, context, request_body)
        return json.loads(response.text), response.status_code

    def get_ticket_body(self, ticket):
        source = {
            "chat": 1, "email": 2, "form": 3, "phone": 4
        }
        request_body = {
            "properties": {
                "hs_pipeline": 0 if ticket.pipeline == 'support_pipeline' else None,
                "hs_pipeline_stage": source[ticket.source.lower()] if ticket.source else None,
                "hs_ticket_priority": ticket.priority.upper() if ticket.priority else None,
                "hubspot_owner_id": ticket.owner_id,
                "subject": ticket.name,
                "content": ticket.ticket_description,
                "createdate": ticket.create_date
            }, "associations": {
                # vid is contact id
                "associatedVids": [
                    ticket.contact_id
                ],
                "associatedCompanyIds": [
                    ticket.company_id
                ]
            }
        }
        return request_body

    def update_company(self, context, payload):
        '''Update a Company in HubSpot.'''

        company = HubspotCompany(**payload)
        url = f"companies/{company.company_id}"
        request_body = self.get_company_body(company)
        response = util.rest("PATCH", url, context, request_body)
        return json.loads(response.text), response.status_code

    def update_contact(self, context, payload):
        '''Update a Contact in HubSpot.'''

        contact = HubspotContact(**payload)
        url = f'contacts/{contact.contact_id}'
        request_body = self.get_contact_body(contact)
        response = util.rest("PATCH", url, context, request_body)
        return json.loads(response.text), response.status_code

    def update_deal(self, context, payload):
        '''Update a Deal in HubSpot.'''

        deal = HubspotDeal(**payload)
        url = f'deals/{deal.deal_id}'
        request_body = self.get_deal_body(deal)
        response = util.rest("PATCH", url, context, request_body)
        return json.loads(response.text), response.status_code

    def update_product(self, context, payload):
        '''Update a Product in HubSpot.'''

        product = HubspotProduct(**payload)
        url = f"products/{product.product_id}"
        request_body = self.get_product_body(product)
        response = util.rest("PATCH", url, context, request_body)
        return json.loads(response.text), response.status_code

    def update_ticket(self, context, payload):
        '''Update a Ticket in HubSpot.'''

        ticket = HubspotTicket(**payload)
        url = f'tickets/{ticket.ticket_id}'
        request_body = self.get_ticket_body(ticket)
        response = util.rest("PATCH", url, context, request_body)
        return json.loads(response.text), response.status_code
