from crm.freshworks import util
from crm.freshworks.entities.freshworks_contact import FreshworksContact
from crm.freshworks.entities.freshworks_deal import FreshworksDeal
from crm.freshworks.entities.freshworks_account import FreshworksAccount
from crm.freshworks.entities.freshworks_note import FreshworksNote
from unified.core.actions import Actions
import json


class FreshworksActions(Actions):

    def create_contact(self, context, contact_entity):
        """
        creates a contact 
        context holds the headers 
        contact_entity holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/contacts"
        contact_schema = FreshworksContact(**contact_entity)
        contact_data = {
            "contact": {
                "first_name": contact_schema.first_name,
                "last_name": contact_schema.last_name,
                "mobile_number": contact_schema.mobile_number,
                "owner_id": contact_schema.owner_id,
                "email": contact_schema.email,
                "subscription_status": [contact_schema.subscription_status],
                "lifecycle_stage_id": contact_schema.lifecycle_stage,
                "external_id": contact_schema.external_id
            }
        }
        result = util.rest("POST", url, json.dumps(
            contact_data), context["headers"]).text
        return json.loads(result)

    def create_deal(self, context, deal_entity):
        """
        creates a deal 
        context holds the headers 
        deal_entity holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/deals"
        deal_schema = FreshworksDeal(**deal_entity)
        deal_data = {
            "deal": {
                "name": deal_schema.name,
                "amount": deal_schema.value,
                "owner_id": deal_schema.owner_id,
                "contact_id": deal_schema.contact_id
            }
        }
        result = util.rest("POST", url, json.dumps(
            deal_data), context["headers"]).text
        return json.loads(result)

    def create_account(self, context, account_entity):
        """
        creates a account 
        context holds the headers 
        account_entity holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/sales_accounts"
        account_schema = FreshworksAccount(**account_entity)
        account_data = {
            "sales_account": {
                "name": account_schema.name,
                "website": account_schema.website,
                "phone": account_schema.business_phone,
                "owner_id": account_schema.owner_id,
                "mailing_street": account_schema.mailing_street,
                "city": account_schema.city,
                "state": account_schema.state,
                "zipcode": account_schema.zipcode,
                "country": account_schema.country,
                "facebook": account_schema.facebook,
                "linkedin": account_schema.linkedin,
                "twitter": account_schema.twitter,
                "industry_type_id": account_schema.industry_id
            }
        }
        result = util.rest("POST", url, json.dumps(
            account_data), context["headers"]).text
        return json.loads(result)

    def add_note_contact(self, context, note_entity):
        """
        add note to contact 
        context holds the headers 
        note_entity holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/notes"
        note_schema = FreshworksNote(**note_entity)
        note_data = {
            "note": {
                "description": note_schema.note,
                "targetable_type": "Contact",
                "targetable_id": note_schema.contact_id
            }
        }
        result = util.rest("POST", url, json.dumps(
            note_data), context["headers"]).text
        return json.loads(result)

    def update_contact(self, context, contact_entity):
        """
        updates existing contact 
        context holds the headers 
        contact_entity holds the request.body
        """
        domain = context["headers"]["domain"]
        contact_schema = FreshworksContact(**contact_entity)
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/contacts/{contact_schema.contact_id}"
        contact_data = {
            "contact": {
                "first_name": contact_schema.first_name,
                "last_name": contact_schema.last_name,
                "mobile_number": contact_schema.mobile_number,
                "owner_id": contact_schema.owner_id,
                "work_number": contact_schema.business_phone,
                "email": contact_schema.email,
                "facebook": contact_schema.facebook,
                "address": contact_schema.address,
                "city": contact_schema.mailing_city,
                "state": contact_schema.mailing_state,
                "zipcode": contact_schema.mailing_zip,
                "country": contact_schema.mailing_country,
                "linkedin": contact_schema.linkedin,
                "twitter": contact_schema.twitter
            }
        }
        result = util.rest("PUT", url, json.dumps(
            contact_data), context["headers"]).text
        return json.loads(result)
