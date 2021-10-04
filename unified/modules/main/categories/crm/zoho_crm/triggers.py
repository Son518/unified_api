from unified.core.triggers import Triggers
from crm.zoho_crm.api import ZohocrmApi


class ZohocrmTriggers(Triggers):

    def new_account(self, context, payload):
        '''trigger when new account is added '''

        params = {
            "account_id": payload['id']
        }
        return ZohocrmApi().account(context, params)

    def account_updated(self, context, payload):
        '''trigger when account is updated'''

        params = {
            "account_id": payload['id']
        }
        return ZohocrmApi().account(context, params)

    def new_contact(self, context, payload):
        '''trigger when contact is added '''

        params = {
            "contact_id": payload['id']
        }
        return ZohocrmApi().contact(context, params)

    def contact_updated(self, context, payload):
        '''trigger when contact is updated'''

        params = {
            "contact_id": payload['id']
        }
        return ZohocrmApi().contact(context, params)

    def new_deal(self, context, payload):
        '''trigger when deal is created '''

        params = {
            "deal_id": payload['id']
        }
        return ZohocrmApi().deal(context, params)

    def deal_updated(self, context, payload):
        '''trigger when deal is updated'''

        params = {
            "deal_id": payload['id']
        }
        return ZohocrmApi().deal(context, params)

    def new_lead(self, context, payload):
        '''trigger when new lead added'''

        params = {
            "lead_id": payload['id']
        }
        return ZohocrmApi().lead(context, params)

    def lead_updated(self, context, payload):
        '''trigger when lead is updated '''
        
        params = {
            "lead_id": payload['id']
        }
        return ZohocrmApi().lead(context, params)
