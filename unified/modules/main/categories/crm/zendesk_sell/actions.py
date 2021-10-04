from core.actions import Actions
from crm.zendesk_sell.entities.zendesk_sell_contact import ZendesksellContact
from crm.zendesk_sell.entities.zendesk_sell_company import ZendesksellCompany
from crm.zendesk_sell.entities.zendesk_sell_deal import ZendesksellDeal
from crm.zendesk_sell.entities.zendesk_sell_lead import ZendesksellLead
from crm.zendesk_sell.entities.zendesk_sell_note import ZendesksellNote
from crm.zendesk_sell.entities.zendesk_sell_catalog import ZendesksellCatalog
from crm.zendesk_sell.entities.zendesk_sell_enrollment import ZendesksellEnrollment
from crm.zendesk_sell.entities.zendesk_sell_task import ZendesksellTask
from crm.zendesk_sell import util
import basecrm
import json

class ZendesksellActions(Actions):

    def create_contact(self,context,contact_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        contact_schema = ZendesksellContact(**contact_entity)

        if contact_schema.prospect_status is None:
            contact_schema.prospect_status = 'none'

        if contact_schema.customer_status is None:
            contact_schema.customer_status = 'none'
        
        contact_data = {
                        "first_name": contact_schema.first_name,
                        "last_name": contact_schema.last_name,
                        "title": contact_schema.title,
                        "email": contact_schema.email,
                        "phone": contact_schema.work_number,
                        "mobile": contact_schema.mobile_number,
                        "industry": contact_schema.industry,
                        "tags": [contact_schema.tags],
                        "address":{"line1": contact_schema.street,
                        "city": contact_schema.city,
                        "postal_code": contact_schema.postal_code,
                        "state": contact_schema.state,
                        "country": contact_schema.country},
                        "owner": contact_schema.owner,
                        "website": contact_schema.website,
                        "facebook": contact_schema.facebook,
                        "linkedin": contact_schema.linkedin,
                        "twitter": contact_schema.twitter,
                        "skype": contact_schema.skype,
                        "fax": contact_schema.fax_number,
                        "description": contact_schema.description,
                        "prospect_status":contact_schema.prospect_status,
                        "customer_status":contact_schema.customer_status
                         }
        print(contact_data)
        response = client.contacts.create(contact_data)
        return response
    
    def create_company(self,context,company_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        company_schema = ZendesksellCompany(**company_entity)
        company_data = {
                        "name": company_schema.name,
                        "email": company_schema.email,
                        "phone": company_schema.work_number,
                        "mobile": company_schema.mobile_number,
                        "industry": company_schema.industry,
                        "parent_organization_id":company_schema.parent_company,
                        "is_organization": True,
                        "tags": [company_schema.tags],
                        "address":{"line1": company_schema.street,
                        "city": company_schema.city,
                        "postal_code": company_schema.postal_code,
                        "state": company_schema.state,
                        "country": company_schema.country},
                        "owner": company_schema.owner,
                        "website": company_schema.website,
                        "facebook": company_schema.facebook,
                        "linkedin": company_schema.linkedin,
                        "twitter": company_schema.twitter,
                        "skype": company_schema.skype,
                        "fax": company_schema.fax_number,
                        "description": company_schema.description
                         }
        response = client.contacts.create(company_data)
        return response

    def create_deal(self,context,deal_entity):
        
        access_token = context["headers"]["access_token"]
        deal_schema = ZendesksellDeal(**deal_entity)
        
        deal_data ={
            "data":{
            "name" :deal_schema.name,
            "value":deal_schema.value,
            "currency":deal_schema.currency,
            "hot":True,
            "tags":[deal_schema.tag],
        },
        'meta': {
                    'type': 'deal'
                }
                }
        if deal_schema.primary_contact is not None:
            deal_data["data"]["contact_id"] =  int(deal_schema.primary_contact)

        if deal_schema.stage is not None:
            deal_data["data"]["stage_id"] =  int(deal_schema.stage)
        print(deal_data)
        url='https://api.getbase.com/v2/deals'
        response = util.rest("POST", url, deal_data, access_token).text
        return json.loads(response)

    def create_lead(self,context,lead_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        lead_schema = ZendesksellLead(**lead_entity)
        lead_data = { 
                        "first_name": lead_schema.first_name,
                        "last_name": lead_schema.last_name,
                        "title": lead_schema.title,
                        "company_name": lead_schema.company_name,
                        "email": lead_schema.email,
                        "phone": lead_schema.work_number,
                        "mobile": lead_schema.mobile_number,
                        "industry": lead_schema.industry,
                        "tags": [lead_schema.tags],
                        "address":{"line1": lead_schema.street,
                        "city": lead_schema.city,
                        "postal_code": lead_schema.postal_code,
                        "state": lead_schema.state,
                        "country": lead_schema.country},
                        "owner": lead_schema.owner,
                        "website": lead_schema.website,
                        "facebook": lead_schema.facebook,
                        "linkedin": lead_schema.linkedin,
                        "twitter": lead_schema.twitter,
                        "skype": lead_schema.skype,
                        "fax": lead_schema.fax_number,
                        "description": lead_schema.description,
                        "source":lead_schema.source,
                        "status":lead_schema.status   
                         }
        response = client.leads.create(lead_data)
        return response

    def create_note(self,context,note_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        note_schema = ZendesksellNote(**note_entity)
        note_data = {
                        "resource_type" :note_schema.related_to,
                        "resource_id":int(note_schema.id),
                        "content":note_schema.content
                         }
        response = client.notes.create(note_data)
        return response

    def create_product_in_catalog(self,context,catalog_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        catalog_schema = ZendesksellCatalog(**catalog_entity)
        catalog_data = {
                        "name":catalog_schema.name,
                        "descrption":catalog_schema.description,
                        "max_discount":catalog_schema.max_discount,
                        "cost_currency":catalog_schema.unit_cost_currency,
                        "prices": [{"amount": catalog_schema.unit_price, "currency": catalog_schema.currency}]
                        }

        if catalog_schema.active is not None:
            catalog_data["active"] = catalog_schema.active 
        else:
            catalog_data["active"] = "false"

        if catalog_schema.sku is not None:
            catalog_data["sku"] = catalog_schema.active 
        else:
            catalog_data["sku"] = 0
            
        if catalog_schema.sku is not None:
            catalog_data["max_markup"] = catalog_schema.max_markup
        else:
            catalog_data["max_markup"] = 0
        
        if catalog_schema.unit_cost is not None:
            catalog_data["cost"] = catalog_schema.unit_cost 
        else:
            catalog_data["cost"] = 0.0
        
        if catalog_schema.unit_cost_currency is not None:
            catalog_data["cost_currency"] = catalog_schema.unit_cost_currency 
        else:
            catalog_data["cost_currency"] = catalog_schema.currency

        response = client.products.create(catalog_data)
        return response

    def create_task(self,context,task_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        task_schema = ZendesksellTask(**task_entity)
        task_data = {
                    "resource_type": task_schema.related_to,
                    "resource_id": int(task_schema.lead),
                    "due_date": task_schema.due_date,
                    "content":task_schema.task_content,
                    "remind_at":task_schema.alert_date
                    }
        response = client.tasks.create(task_data)
        return response
    
    def update_contact(self,context,contact_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        contact_schema = ZendesksellContact(**contact_entity)
        if contact_schema.prospect_status is None:
            contact_schema.prospect_status = 'none'

        if contact_schema.customer_status is None:
            contact_schema.customer_status = 'none'

        contact_data = {
                        "first_name": contact_schema.first_name,
                        "last_name": contact_schema.last_name,
                        "title": contact_schema.title,
                        "email": contact_schema.email,
                        "phone": contact_schema.work_number,
                        "mobile": contact_schema.mobile_number,
                        "industry": contact_schema.industry,
                        "tags": [contact_schema.tags],
                        "address":{"line1": contact_schema.street,
                        "city": contact_schema.city,
                        "postal_code": contact_schema.postal_code,
                        "state": contact_schema.state,
                        "country": contact_schema.country},
                        "owner": contact_schema.owner,
                        "website": contact_schema.website,
                        "facebook": contact_schema.facebook,
                        "linkedin": contact_schema.linkedin,
                        "twitter": contact_schema.twitter,
                        "skype": contact_schema.skype,
                        "fax": contact_schema.fax_number,
                        "description": contact_schema.description,
                        "prospect_status":contact_schema.prospect_status,
                        "customer_status":contact_schema.customer_status
                         }
        response = client.contacts.update(contact_schema.contact_id,contact_data)
        return response
    
    def update_company(self,context,company_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        company_schema = ZendesksellCompany(**company_entity)
        company_data = {
                        "name": company_schema.name,
                        "email": company_schema.email,
                        "phone": company_schema.work_number,
                        "mobile": company_schema.mobile_number,
                        "industry": company_schema.industry,
                        "parent_organization_id":company_schema.parent_company,
                        "is_organization": True,
                        "tags": [company_schema.tags],
                        "address":{"line1": company_schema.street,
                        "city": company_schema.city,
                        "postal_code": company_schema.postal_code,
                        "state": company_schema.state,
                        "country": company_schema.country},
                        "owner": company_schema.owner,
                        "website": company_schema.website,
                        "facebook": company_schema.facebook,
                        "linkedin": company_schema.linkedin,
                        "twitter": company_schema.twitter,
                        "skype": company_schema.skype,
                        "fax": company_schema.fax_number,
                        "description": company_schema.description
                         }
        response = client.contacts.update(company_schema.company_id,company_data)
        return response

    def update_deal(self,context,deal_entity):

        access_token = context["headers"]["access_token"]
        deal_schema = ZendesksellDeal(**deal_entity)
        deal_data ={
            "data":{
            "name" :deal_schema.name,
            "value":deal_schema.value,
            "currency":deal_schema.currency,
            "hot":True,
            "tags":[deal_schema.tag],
        },
        'meta': {
                    'type': 'deal'
                }
                }
        if deal_schema.primary_contact is not None:
            deal_data["data"]["contact_id"] =  int(deal_schema.primary_contact)

        if deal_schema.stage is not None:
            deal_data["data"]["stage_id"] =  int(deal_schema.stage)
            
        url=f'https://api.getbase.com/v2/deals/{deal_schema.deal_id}'
        response = util.rest("PUT", url, deal_data, access_token).text
        return response

    def update_lead(self,context,lead_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        lead_schema = ZendesksellLead(**lead_entity)
        lead_data = { 
                        "first_name": lead_schema.first_name,
                        "last_name": lead_schema.last_name,
                        "title": lead_schema.title,
                        "company_name": lead_schema.company_name,
                        "email": lead_schema.email,
                        "phone": lead_schema.work_number,
                        "mobile": lead_schema.mobile_number,
                        "industry": lead_schema.industry,
                        "tags": [lead_schema.tags],
                        "address":{"line1": lead_schema.street,
                        "city": lead_schema.city,
                        "postal_code": lead_schema.postal_code,
                        "state": lead_schema.state,
                        "country": lead_schema.country},
                        "owner": lead_schema.owner,
                        "website": lead_schema.website,
                        "facebook": lead_schema.facebook,
                        "linkedin": lead_schema.linkedin,
                        "twitter": lead_schema.twitter,
                        "skype": lead_schema.skype,
                        "fax": lead_schema.fax_number,
                        "description": lead_schema.description,
                        "source":lead_schema.source,
                        "status":lead_schema.status   
                         }
        response = client.leads.update(lead_schema.lead_id,lead_data)
        return json.dumps(response)

    def update_product_in_catalog(self,context,catalog_entity):

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        catalog_schema = ZendesksellCatalog(**catalog_entity)
        catalog_data = {
                        "name":catalog_schema.name,
                        "descrption":catalog_schema.description,
                        "max_discount":catalog_schema.max_discount,
                        "cost_currency":catalog_schema.unit_cost_currency,
                        "prices": [{"amount": catalog_schema.unit_price, "currency": catalog_schema.currency}]
                        }

        if catalog_schema.active is not None:
            catalog_data["active"] = catalog_schema.active 
        else:
            catalog_data["active"] = "false"

        if catalog_schema.sku is not None:
            catalog_data["sku"] = catalog_schema.active 
        else:
            catalog_data["sku"] = 0
            
        if catalog_schema.sku is not None:
            catalog_data["max_markup"] = catalog_schema.max_markup
        else:
            catalog_data["max_markup"] = 0
        
        if catalog_schema.unit_cost is not None:
            catalog_data["cost"] = catalog_schema.unit_cost 
        else:
            catalog_data["cost"] = 0.0
        
        if catalog_schema.unit_cost_currency is not None:
            catalog_data["cost_currency"] = catalog_schema.unit_cost_currency 
        else:
            catalog_data["cost_currency"] = catalog_schema.currency

        response = client.products.update(catalog_schema.catalog_id,catalog_data)
        return response
