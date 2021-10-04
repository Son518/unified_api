import json
import os
import requests
from unified.core.actions import Actions
from customer_support.zoho_desk.entities.zohodesk_ticket import ZohodeskTicket
from customer_support.zoho_desk.entities.zohodesk_contact import ZohodeskContact
from customer_support.zoho_desk.entities.zohodesk_account import ZohodeskAccount
from customer_support.zoho_desk.entities.zohodesk_comment import ZohodeskComment
from customer_support.zoho_desk import util


class ZohodeskActions(Actions):

    def add_attachment(self, context, payload):
        """ Add an attachment to a ticket. """

        token = util.get_access_token(context)
        url = util.get_url() + f"tickets/{payload['ticket_id']}/attachments"
        if payload.get('public'): url += f"?isPublic={payload['public']}"
        file_url = payload['file']
        file_name = file_url.split('/')[-1]
        response = requests.get(file_url)

        if response.status_code >= 400:
            raise Exception('Error: ', response.text)

        files = {
            "file": (file_name, response.content)
        }
        response = util.rest("POST", url, token, payload['organization_id'], files=files)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def add_comment(self, context, payload):
        """ Add a comment to a ticket. """

        token = util.get_access_token(context)
        comment = ZohodeskComment(**payload)
        url = util.get_url() + f"tickets/{comment.ticket_id}/comments"
        data = comment.get_as_data(include_none=False)
        response = util.rest("POST", url, token, comment.organization_id, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def create_ticket(self, context, payload):
        """ Create a new ticket. """

        token = util.get_access_token(context)
        url = util.get_url() + "tickets"
        ticket = ZohodeskTicket(**payload)
        data = ticket.get_as_data()
        response = util.rest("POST", url, token, ticket.organization_id, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def create_contact(self, context, payload):
        """ Create a new contact """

        token = util.get_access_token(context)
        url = util.get_url() + "contacts"
        contact = ZohodeskContact(**payload)
        data = contact.get_as_data()
        response = util.rest("POST", url, token, contact.organization_id, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def create_account(self, context, payload):
        """ Create a new account """

        token = util.get_access_token(context)
        url = util.get_url() + "accounts"
        account = ZohodeskAccount(**payload)
        data = account.get_as_data()
        response = util.rest("POST", url, token, account.organization_id, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def update_ticket(self, context, payload):
        """ Update an existing ticket status or add comments. """

        token = util.get_access_token(context)
        ticket = ZohodeskTicket(**payload)
        url = util.get_url() + f"tickets/{ticket.ticket_id}"
        data = ticket.get_as_data(include_none=False)
        response = util.rest("PATCH", url, token, ticket.organization_id, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)

    def update_contact(self, context, payload):
        """ Update an existing contact. """

        token = util.get_access_token(context)
        contact = ZohodeskContact(**payload)
        url = util.get_url() + f"contacts/{contact.contact_id}"
        data = contact.get_as_data(include_none=False)
        response = util.rest("PATCH", url, token, contact.organization_id, data)

        if response.status_code > 400:
            raise Exception("Error: ", response.text)

        return json.loads(response.text)
