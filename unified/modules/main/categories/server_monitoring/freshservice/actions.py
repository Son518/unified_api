from unified.core.actions import Actions
from server_monitoring.freshservice.entities.freshservice_ticket import FreshserviceTicket
from server_monitoring.freshservice.entities.freshservice_requester import FreshserviceRequester
from server_monitoring.freshservice import util


class FreshserviceActions(Actions):

    @staticmethod
    def get_priority(str_name):
        """ utility function for getting priority as number """

        if str_name == None or str_name.title() == "Low":
            return 1
        elif str_name.title() == "Medium":
            return 2
        elif str_name.title() == "High":
            return 3
        elif str_name.title() == "Urgent":
            return 4
        else:
            return str_name

    @staticmethod
    def get_status(str_name):
        """ utility function for getting status as number """

        if str_name == None or str_name.title() == "Open":
            return 2
        elif str_name.title() == "Pending":
            return 3
        elif str_name.title() == "Resolved":
            return 4
        elif str_name.title() == "Closed":
            return 5
        else:
            return str_name

    def create_ticket(self, context, payload):
        """ Create a new ticket """

        ticket = FreshserviceTicket(**payload)
        data = {
            "subject": ticket.subject,
            "email": ticket.email,
            "description": ticket.description,
            "priority": self.get_priority(ticket.priority),
            "status": self.get_status(ticket.status)
        }

        if ticket.cc_emails:
            data['cc_emails'] = ticket.cc_emails.split(',')

        resp = util.rest("POST", "tickets", context, body=data)

        return resp

    def create_requester(self, context, payload):
        """ Create a new requester """

        requester = FreshserviceRequester(**payload)
        data = {
            "first_name": requester.name,
            "primary_email": requester.email,
            "address": requester.address,
            "background_information": requester.background_information,
            "work_phone_number": requester.phone,
            "job_title": requester.job_title
        }

        resp = util.rest("POST", "requesters", context, body=data)

        return resp
