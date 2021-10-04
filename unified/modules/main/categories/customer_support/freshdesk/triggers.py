import json
from core.triggers import Triggers
from customer_support.freshdesk.entities.freshdesk_ticket import FreshdeskTicket

class FreshdeskTriggers(Triggers):
    
     def new_ticket(self,context,payload):
        """
        triggers when new ticket created
        context holds the headers 
        params holds ticket_id
        """
        ticket_obj = payload["freshdesk_webhook"]
        ticket = FreshdeskTicket(ticket_id=ticket_obj["ticket_id"],
                                subject=ticket_obj["ticket_subject"],
                                description=ticket_obj["ticket_description"]
                                )
        return ticket.__dict__