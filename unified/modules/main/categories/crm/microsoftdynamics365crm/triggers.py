from unified.core.triggers import Triggers
from crm.microsoftdynamics365crm.api import DynamicscrmApi


class DynamicscrmTriggers(Triggers):

    def new_contact(self, context, payload):
        """ Trigger executing when new contact created """

        params = {
            "contactid": payload["contact_id"]
        }

        return DynamicscrmApi().contact(context, params)

    def contact_updated(self, context, payload):
        """ Trigger executing when contact updated """

        params = {
            "contactid": payload["contact_id"]
        }

        return DynamicscrmApi().contact(context, params)

    def new_account(self, context, payload):
        """ Trigger executing when new account created """

        params = {
            "accountid": payload["account_id"]
        }

        return DynamicscrmApi().account(context, params)

    def new_lead(self, context, payload):
        """ Trigger executing when new lead created """

        params = {
            "leadid": payload["lead_id"]
        }

        return DynamicscrmApi().lead(context, params)

    def lead_updated(self, context, payload):
        """ Trigger executing when lead updated """

        params = {
            "leadid": payload["lead_id"]
        }

        return DynamicscrmApi().lead(context, params)
