import json
from core.triggers import Triggers
from customer_support.zendesk.entities.zendesk_ticket import ZendeskTicket


class ZendeskTriggers(Triggers):

    def new_ticket(self, context, payload):
        """
        triggers when new ticket created 
        context holds the headers 
        payload holds the request.body
        """
        ticket = ZendeskTicket(ticket_id=payload["id"],
                               subject=payload["subject"],
                               description=payload["description"],
                               type=payload["type"],
                               status=payload["status"],
                               priority=payload["priority"],
                               due_at=payload["due_by"] if payload["due_by"] else "",
                               requester_name=payload["contact_name"],
                               requester_email=payload["contact_email"]
                               )
        return ticket.__dict__

    def updated_ticket(self, context, payload):
        """
        triggers when ticket updated
        context holds the headers 
        payload holds the request.body
        """
        updated_ticket = ZendeskTicket(ticket_id=payload["id"],
                                       subject=payload["subject"],
                                       description=payload["description"],
                                       type=payload["type"],
                                       status=payload["status"],
                                       priority=payload["priority"],
                                       due_at=payload["due_by"],
                                       requester_name=payload["contact_name"],
                                       requester_email=payload["contact_email"]
                                       )
        return updated_ticket.__dict__
