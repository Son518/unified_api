import json
from customer_support.zoho_desk.entities.zohodesk_comment import ZohodeskComment
from customer_support.zoho_desk.entities.zohodesk_account import ZohodeskAccount
from customer_support.zoho_desk.entities.zohodesk_ticket import ZohodeskTicket
from customer_support.zoho_desk.entities.zohodesk_contact import ZohodeskContact
from customer_support.zoho_desk import util


class ZohodeskApi:

    @staticmethod
    def adjust_payload(keys: list, payload: dict):
        """ utility function for clearing payload fields
            in relation to list of needed keys """

        return { key : value for key, value in payload.items() if key in keys }

    @staticmethod
    def get_ticket(ticket_data):
        """ utility function for parsing ticket data and return as dict """

        return ZohodeskTicket(
            ticket_id = ticket_data.get('id'),
            department_id = ticket_data.get('departmentId'),
            contact_id = ticket_data.get('contactId'),
            subject = ticket_data.get('subject'),
            email = ticket_data.get('email'),
            phone = ticket_data.get('phone'),
            description = ticket_data.get('description'),
            category = ticket_data.get('category'),
            sub_category = ticket_data.get('subCategory'),
            status = ticket_data.get('status'),
            assignee = ticket_data.get('assigneeId'),
            priority = ticket_data.get('priority'),
            channel = ticket_data.get('channel'),
            classification = ticket_data.get('classification'),
            due_date = ticket_data.get('dueDate'),
        ).__dict__

    @staticmethod
    def get_account(account_data):
        """ utility function for parsing account data and return as dict """

        return ZohodeskAccount(
            id = account_data.get('id'),
            name = account_data.get('accountName'),
            description = account_data.get('description'),
            email = account_data.get('email'),
            website = account_data.get('website'),
            fax = account_data.get('fax'),
            phone = account_data.get('phone'),
            industry = account_data.get('industry'),
            owner_id = account_data.get('ownerId'),
            street = account_data.get('street'),
            city = account_data.get('city'),
            state = account_data.get('state'),
            country = account_data.get('country'),
            zip_code = account_data.get('code'),
            annual_revenue = account_data.get('annualrevenue'),
        ).__dict__

    @staticmethod
    def get_contact(contact_data):
        """ utility function for parsing contact data and return as dict """

        return ZohodeskContact(
            contact_id = contact_data.get('id'),
            account_id = contact_data.get('id'),
            last_name = contact_data.get('id'),
            first_name = contact_data.get('id'),
            title = contact_data.get('title'),
            description = contact_data.get('description'),
            type = contact_data.get('type'),
            email = contact_data.get('email'),
            secondary_email = contact_data.get('secondaryEmail'),
            facebook = contact_data.get('facebook'),
            twitter = contact_data.get('twitter'),
            phone = contact_data.get('phone'),
            mobile = contact_data.get('mobile'),
            street_address = contact_data.get('street'),
            city = contact_data.get('city'),
            state = contact_data.get('state'),
            country = contact_data.get('country'),
            zip_code = contact_data.get('zip'),
        ).__dict__

    @staticmethod
    def get_comment(comment_data):
        """ utility function for parsing comment data and return as dict """

        return ZohodeskComment(
            comment_id = comment_data.get('id'),
            ticket_id = comment_data.get('ticketId'),
            content = comment_data.get('content'),
            public = comment_data.get('isPublic'),
            attachment_ids = comment_data.get('attachmentIds'),
            content_type = comment_data.get('contentType'),
            commenter = comment_data.get('commenter'),
        ).__dict__

    def contact_by_email(self, context, params):
        """ Finds contact by provided email """

        token = util.get_access_token(context)
        url = util.get_url() + f"search?searchStr={params['email']}&module=contacts"
        response = util.rest("GET", url, token, params['organization_id'])
        data = json.loads(response.text)

        if response.status_code > 400:
            return data

        if response.status_code == 204:
            return { "result": "Nothing found" }

        return data['data']

    def ticket(self, context, params):
        """ Finds an existing ticket. """

        token = util.get_access_token(context)
        url = util.get_url() + f"tickets/{params['ticket_id']}"
        response = util.rest("GET", url, token, params['organization_id'])
        data = json.loads(response.text)

        if response.status_code > 400:
            return data

        return ZohodeskApi.get_ticket(data)
