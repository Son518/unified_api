import json
from core.actions import Actions
from customer_support.freshdesk import util
from customer_support.freshdesk.entities.freshdesk_ticket import FreshdeskTicket
from customer_support.freshdesk.entities.freshdesk_contact import FreshdeskContact
from customer_support.freshdesk.entities.freshdesk_company import FreshdeskCompany
from customer_support.freshdesk.entities.freshdesk_forum import FreshdeskForum


class FreshdeskActions(Actions):

    def create_ticket(self, context, ticket_entity):
        """
        creates a new ticket 
        context holds the headers 
        ticket_entity holds the request.body
        """
        client = util.get_freshdesk_client(context["headers"])
        ticket_schema = FreshdeskTicket(**ticket_entity)
        ticket = client.tickets.create_ticket(ticket_schema.subject,
                                              email=ticket_schema.email,
                                              type=ticket_schema.type,
                                              description=ticket_schema.description,
                                              priority=ticket_schema.priority,
                                              cc_emails=[
                                                  ticket_schema.cc_email]
                                              )

        # response from sdk call is given in the format of object
        keys = (ticket.__dict__)["_keys"]
        response = {}
        for key in keys:
            response[key] = (ticket.__dict__)[key]
        return response

    def create_contact(self, context, contact_entity):
        """
        creates a new contact 
        context holds the headers 
        ticket_entity holds the request.body
        """
        client = util.get_freshdesk_client(context["headers"])
        contact_schema = FreshdeskContact(**contact_entity)
        contact = client.contacts.create_contact(name=contact_schema.name,
                                                 email=contact_schema.email,
                                                 address=contact_schema.address,
                                                 description=contact_schema.description,
                                                 phone=contact_schema.phone,
                                                 job_title=contact_schema.job_title,
                                                 tags=[contact_schema.tags]
                                                 )

        # response from sdk call is given in the format of object
        keys = (contact.__dict__)["_keys"]
        response = {}
        for key in keys:
            response[key] = (contact.__dict__)[key]
        return response

    def create_company(self, context, company_entity):
        """
        creates a new company 
        context holds the headers 
        ticket_entity holds the request.body
        """
        client = util.get_freshdesk_client(context["headers"])
        company_schema = FreshdeskCompany(**company_entity)
        company = client.companies.create_company(name=company_schema.name,
                                                  description=company_schema.description,
                                                  note=company_schema.notes,
                                                  domains=[
                                                      company_schema.domains]
                                                  )

        # response from sdk call is given in the format of object
        keys = (company.__dict__)["_keys"]
        response = {}
        for key in keys:
            response[key] = (company.__dict__)[key]
        return response

    def add_note_to_ticket(self, context, note_entity):
        """
        adds note to ticket
        context holds the headers 
        ticket_entity holds the request.body
        """
        client = util.get_freshdesk_client(context["headers"])
        note_schema = FreshdeskTicket(**note_entity)

        note = client.comments.create_note(
            int(note_schema.ticket_id), note_schema.notes, private=note_schema.private)

        # response from sdk call is given in the format of object
        keys = (note.__dict__)["_keys"]
        response = {}
        for key in keys:
            response[key] = (note.__dict__)[key]
        return response

    def create_forum_category(self, context, forum_entity):
        """
        creates forum in category
        context holds the headers 
        ticket_entity holds the request.body
        """
        forum_schema = FreshdeskForum(**forum_entity)
        forum_data = {
            "name": forum_schema.name,
            "description": forum_schema.description
        }

        # sdk call is not available for this method
        response = util.rest("POST", "categories",
                             context["headers"], forum_data).text
        print(type(response))
        return json.loads(response)

    def create_forum(self, context, forum_entity):
        """
        creates forum 
        context holds the headers 
        ticket_entity holds the request.body
        """
        domain = context["headers"]["domain"]
        forum_schema = FreshdeskForum(**forum_entity)
        category = ["forums", forum_schema.forum_category]

        forum_visibility = {"all": 1, "logged in users": 2,
                            "agents": 3, "select companies": 4}
        forum_type = {"questions": 1, "ideas": 2,
                      "problems": 3, "anouncements": 4}
        forum_data = {
            "name": forum_schema.name,
            "forum_type": forum_type[forum_schema.type.lower()],
            "forum_visibility": forum_visibility[forum_schema.visibility.lower()],
            "description": forum_schema.description
        }

        # sdk call is not available for this method
        response = util.rest(
            "POST", category, context["headers"], forum_data).text
        return json.loads(response)

    def create_forum_topic(self, context, forum_entity):
        """
        creates topic in forum
        context holds the headers 
        ticket_entity holds the request.body
        """
        domain = context["headers"]["domain"]
        forum_schema = FreshdeskForum(**forum_entity)
        category = ["topics", forum_schema.forum_category]
        forum_data = {
            "title": forum_schema.title,
            "sticky": forum_schema.sticky,
            "locked": forum_schema.locked,
            "message": forum_schema.topic_description
        }

        # sdk call is not available for this method
        response = util.rest(
            "POST", category, context["headers"], forum_data).text
        return json.loads(response)
