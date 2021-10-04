import json
from customer_support.freshdesk import util
from customer_support.freshdesk.entities.freshdesk_ticket import FreshdeskTicket
from customer_support.freshdesk.entities.freshdesk_contact import FreshdeskContact

class FreshdeskApi():

    def find_ticket_by_id(self,context,params):
        """
        gets a ticket using ticket_id
        context holds the headers 
        params holds ticket_id
        """        
        client = util.get_freshdesk_client(context["headers"])
        response = client.tickets.get_ticket(int(params["id"]))

        #response is returned as object
        ticket_obj = response.__dict__
        ticket = FreshdeskTicket(ticket_id=ticket_obj["id"],
                                subject=ticket_obj["subject"],
                                email=ticket_obj["to_emails"],
                                type=ticket_obj["type"],
                                description=ticket_obj["description"],
                                priority=ticket_obj["_priority"],
                                cc_email=ticket_obj["cc_emails"]
                                )
        return ticket.__dict__

    def find_contact(self,context,params):
        """
        gets a contact using email
        context holds the headers 
        params holds email
        """        
        client = util.get_freshdesk_client(context["headers"])
        contacts = client.contacts.list_contacts()
        contact_list = []
        for contact in contacts:
            contact = contact.__dict__
            if contact["email"] == params["email"]:
                contact_obj = FreshdeskContact(name=contact["name"],
                                                email=contact["email"],
                                                address=contact["address"],
                                                description=contact["description"],
                                                phone=contact["phone"],
                                                job_title=contact["job_title"],
                                                contact_id=contact["id"]
                                                )
                contact_list.append(contact_obj.__dict__)  
        return json.dumps(contact_list)