from unified.core.triggers import Triggers
from customer_support.zoho_desk.api import ZohodeskApi
from customer_support.zoho_desk.entities.zohodesk_agent import ZohodeskAgent
from customer_support.zoho_desk.entities.zohodesk_attachment import ZohodeskAttachment


class ZohodeskTriggers(Triggers):

    def new_account(self, context, payload):
        """ Triggers when a new account is created. """

        accounts = []
        for item in payload:
            if item['payload']:
                accounts.append(ZohodeskApi.get_account(item['payload']))

        return {
            "new_accounts": accounts
        }

    def new_agent(self, context, payload):
        """ Triggers when a new agent is added. """

        keys = list(ZohodeskAgent().__dict__.keys())
        agents = []

        for item in payload:
            if item['payload']:
                payld: dict = item['payload']
                agents.append(ZohodeskApi.adjust_payload(keys, payld))

        return {
            "new_agents": agents
        }

    def new_attachment(self, context, payload):
        """ Triggers when a new attachment is added to any ticket in the selected organization. """

        keys = list(ZohodeskAttachment().__dict__.keys())
        attachments = []

        for item in payload:
            if item['payload']:
                payld: dict = item['payload']
                attachments.append(ZohodeskApi.adjust_payload(keys, payld))

        return {
            "new_attachments": attachments
        }

    def new_comment(self, context, payload):
        """ Triggers when a new comment is added to any ticket in the selected department. """

        comments = []
        for item in payload:
            if item['payload']:
                comments.append(ZohodeskApi.get_comment(item['payload']))

        return {
            "new_comments": comments
        }

    def new_contact(self, context, payload):
        """ Triggers when a new customer is created. """

        contacts = []
        for item in payload:
            if item['payload']:
                contacts.append(ZohodeskApi.get_contact(item['payload']))

        return {
            "new_contacts": contacts
        }

    def new_status_change(self, context, payload):
        """ Triggers when a new status is changed. """

        return self.updated_ticket(context, payload)

    def new_ticket(self, context, payload):
        """ Triggers when a new ticket is added to a view. """

        tickets = []
        for item in payload:
            if item['payload']:
                tickets.append(ZohodeskApi.get_ticket(item['payload']))

        return {
            "new_tickets": tickets
        }

    def updated_ticket(self, context, payload):
        """ Triggers when a Ticket is updated. """

        tickets = []
        for item in payload:
            if item['payload']:
                tickets.append(ZohodeskApi.get_ticket(item['payload']))

        return {
            "updated_tickets": tickets
        }
