from unified.core.actions import Actions
from crm.redtailcrm.entities.redtailcrm_contact import RedtailcrmContact
from crm.redtailcrm.entities.redtailcrm_account import RedtailcrmAccount
from crm.redtailcrm.entities.redtailcrm_deal import RedtailcrmDeal
from crm.redtailcrm import util
import json


class RedtailcrmActions(Actions):

    def create_contact(self, context, contact_entity):
        ''' creates new contact'''

        access_token = util.get_basic_token(context["headers"])
        url = "https://smf.crm3.redtailtechnology.com/api/public/v1/contacts"
        contact_schema = RedtailcrmContact(**contact_entity)

        contact_data = {
            "type": "Crm::Contact::Individual",
            "status_id": contact_schema.status,
            "category_id": contact_schema.category,
            "first_name": contact_schema.first_name,
            "last_name": contact_schema.last_name
        }

        response = util.rest("POST", url, contact_data, access_token).text

        # util.rest sending  response object
        return json.loads(response)

    def create_organization(self, context, account_entity):
        ''' creates new organization'''

        access_token = util.get_basic_token(context["headers"])
        account_schema = RedtailcrmAccount(**account_entity)
        url = f"https://smf.crm3.redtailtechnology.com/api/public/v1/contacts/{account_schema.contact_id}/accounts"

        account_data = {
            "number": account_schema.subject,
            "account_type_id": account_schema.account_id,
            "status": account_schema.activity_type,
            "start_date": account_schema.start_date,
            "end_date": account_schema.end_date,
            "all_day": account_schema.all_day,
            "location": account_schema.location,
            "email_address": account_schema.email_address
        }

        response = util.rest("POST", url, account_data, access_token).text

        # util.rest sending  response object
        return json.loads(response)

    def create_opportunity(self, context, deal_entity):
        ''' creates new opportunity'''

        access_token = util.get_basic_token(context["headers"])
        deal_schema = RedtailcrmDeal(**deal_entity)
        url = f"https://smf.crm3.redtailtechnology.com/api/public/v1/opportunities"

        deal_data = {
            "name": deal_schema.name,
            "description": deal_schema.description,
            "opportunity_type": deal_schema.type
        }

        response = util.rest("POST", url, deal_data, access_token).text

        # util.rest sending  response object
        return json.loads(response)

    def create_activity(self, context, note_entity):
        ''' adds new activity to contact'''

        access_token = util.get_basic_token(context["headers"])
        note_schema = RedtailcrmContact(**note_entity)
        url = f"https://smf.crm3.redtailtechnology.com/api/public/v1/contacts/{note_schema.contact_id}/notes"

        note_data = {
            "category_id": note_schema.category,
            "note_type": note_schema.activity_type,
            "pinned": note_schema.pinned,
            "draft": note_schema.draft,
            "body": note_schema.description
        }

        response = util.rest("POST", url, note_data, access_token).text

        # util.rest sending  response object
        return json.loads(response)
