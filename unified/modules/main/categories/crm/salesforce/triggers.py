from unified.core.triggers import Triggers
from crm.salesforce.api import SalesforceApi


class SalesforceTriggers(Triggers):

    def new_contact(self, context, payload):
        """ Triggers when a new contact is added """

        return SalesforceApi.get_contact_data(payload['new'][0])

    def contact_updated(self, context, payload):
        """ Triggers when a contact is updated """

        return SalesforceApi.get_contact_data(payload['new'][0])

    def new_account(self, context, payload):
        """ Triggers when a new account is added """

        return SalesforceApi.get_account_data(payload['new'][0])

    def account_updated(self, context, payload):
        """ Triggers when a account is updated """

        return SalesforceApi.get_account_data(payload['new'][0])

    def new_deal(self, context, payload):
        """ Triggers when a new deal is added """

        return SalesforceApi.get_deal_data(payload['new'][0])

    def deal_updated(self, context, payload):
        """ Triggers when a deal is updated """

        return SalesforceApi.get_deal_data(payload['new'][0])

    def new_leads(self, context, payload):
        """ Triggers when a new lead is added """

        return SalesforceApi.get_lead_data(payload['new'][0])

    def lead_updated(self, context, payload):
        """ Triggers when a lead is updated """

        return SalesforceApi.get_lead_data(payload['new'][0])

    def new_event(self, context, payload):
        """ Triggers when a new event is added """

        return SalesforceApi.get_event_data(payload['new'][0])

    def event_updated(self, context, payload):
        """ Triggers when an event is updated """

        return SalesforceApi.get_event_data(payload['new'][0])

    def new_task(self, context, payload):
        """ Triggers when a new task is added """

        return SalesforceApi.get_task_data(payload['new'][0])

    def task_updated(self, context, payload):
        """ Triggers when a task is updated """

        return SalesforceApi.get_task_data(payload['new'][0])

    def new_note(self, context, payload):
        """ Triggers when a new note is added """

        return SalesforceApi.get_note_data(payload['new'][0])

    def note_updated(self, context, payload):
        """ Triggers when a note is updated """

        return SalesforceApi.get_note_data(payload['new'][0])
