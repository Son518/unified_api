import json
from marketing_automation.hubspot.util import rest
from marketing_automation.hubspot.entities.hubspot_deal import HubspotDeal
from marketing_automation.hubspot.entities.hubspot_owner import HubspotOwner
from marketing_automation.hubspot.entities.hubspot_ticket import HubspotTicket
from marketing_automation.hubspot.entities.hubspot_product import HubspotProduct
from marketing_automation.hubspot.entities.hubspot_company import HubspotCompany


class HubspotApi:
    def company(self, context, payload):
        '''get company by id'''

        url = f"companies/v2/companies/{payload['company_id']}"
        response = rest('GET', url, context).json()
        return (self.company_mappings(response))

    def deal(self, context, payload):
        '''get deal by id'''

        url = f"deals/v1/deal/{payload['deal_id']}"
        response = rest('GET', url, context).json()
        return self.deal_mappings(response)

    def owner(self, context, payload):
        '''get owner by id'''

        url = f"crm/v3/owners/{payload['account_id']}"
        response = rest('GET', url, context).json()
        owner = HubspotOwner(
            owner_id=response.get('id'),
            email=response.get('email'),
            first_name=response.get('firstName'),
            last_name=response.get('lastName'),
            user_id=response.get('userId'),
            archived=response.get('archived')
        ).__dict__
        return owner

    def product(self, context, payload):
        '''get product by id'''

        url = f"crm/v3/objects/products/{payload['product_id']}"
        response = rest('GET', url, context).json()
        response_properties = response.get('properties')
        product = HubspotProduct(
            product_id=response['id'],
            product_name=response_properties.get('name'),
            description=response_properties.get('description'),
            unit_price=response_properties.get('price')
        ).__dict__
        return product

    def ticket(self, context, payload):
        '''get ticket by id'''

        url = f"crm/v3/objects/tickets/{payload['ticket_id']}"
        response = rest('GET', url, context).json()
        response_properties = response.get("properties")
        ticket = HubspotTicket(
            ticket_id=response['id'],
            name=response_properties.get('subject'),
            ticket_description=response_properties.get('content'),
            priority=response_properties.get('hs_ticket_priority'),
            pipeline=response_properties.get("hs_pipeline"),
            source=response_properties.get('hs_pipeline_stage')
        ).__dict__
        return ticket

    def company_mappings(self, response):
        response_properites = response['properties']
        company = HubspotCompany(
            company_id=response.get('companyId') or response.get('objectId'),
            name=response_properites.get('name').get(
                'value') if response_properites.get('name') else None,
            industry=response_properites.get('industry').get(
                'value') if response_properites.get('industry') else None,
            type=response_properites.get('type').get(
                'value') if response_properites.get('type') else None,
            city=response_properites.get('city').get(
                'value') if response_properites.get('city') else None,
            state=response_properites.get('state').get(
                'value') if response_properites.get('state') else None,
            phone=response_properites.get('phone').get(
                'value') if response_properites.get('phone') else None,
            number_of_employess=response_properites.get('numberofemployees').get(
                'value') if response_properites.get('numberofemployees') else None,
            annual_revenue=response_properites.get('annualrevenue').get(
                'value') if response_properites.get('annualrevenue') else None,
            domain=response_properites.get('domain').get(
                'value') if response_properites.get('domain') else None,
            description=response_properites.get('description').get(
                'value') if response_properites.get('description') else None,
        )
        return company.__dict__

    def deal_mappings(self, response):
        response_properites = response['properties']
        deal = HubspotDeal(
            deal_id=response.get('dealId'),
            name=response_properites.get('dealname').get(
                "value") if response_properites.get('dealname') else None,
            pipeline=response_properites.get("pipeline").get(
                'value') if response_properites.get('pipeline') else None,
            deal_stage=response_properites.get('dealstage').get(
                "value") if response_properites.get('dealstage') else None,
            ammount=response_properites.get("amount").get(
                'value') if response_properites.get('amount') else None,
            end_date=response_properites.get('closedate').get(
                "value") if response_properites.get('closedate') else None,
            deal_type=response_properites.get("dealtype").get(
                'value') if response_properites.get('dealtype') else None,
            priority=response_properites.get('hs_priority').get(
                "value") if response_properites.get('hs_priority') else None,
            company_id=response.get("associations").get(
                'associatedCompanyIds') if response_properites.get('associations') else None,
            contact_id=response.get('associations').get(
                "associatedVids") if response_properites.get('associations') else None,
            owner_id=response_properites.get("hubspot_owner_id").get(
                'value') if response_properites.get('hubspot_owner_id') else None,
        )
        return deal.__dict__
    
    def verify(self, context, payload):
        url ="integrations/v1/me"
        response_data = rest('GET', url, context)
        response = response_data.json()
        return response
    
    def profile(self, context, payload):
        url = "crm/v3/owners/"
        response_data = rest('GET', url, context)
        response = response_data.json()['results'][0]
        profile = {
            'id':response['id'],
            'email':response['email'],
            'name':response['firstName']
        }
        return profile