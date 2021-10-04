import json
from core.triggers import Triggers
from customer_support.help_scout.entities.help_scout_conversation import HelpscoutConversation
from customer_support.help_scout.entities.help_scout_customer import HelpscoutCustomer


class HelpscoutTriggers(Triggers):

    def new_conversation(self, context, payload):
        """
        triggers when new conversation created 
        context holds the headers 
        payload holds the request.body
        """
        conversation = HelpscoutConversation(subject=payload["subject"],
                                             mailbox_id=payload["mailbox"]["id"],
                                             customer_id=payload["customer"]["id"],
                                             customer_email=payload["customer"]["email"],
                                             from_user_id=payload["owner"]["id"],
                                             status=payload["status"],
                                             assigned_user_id=payload["customer"]["id"],
                                             tag=payload["tags"],
                                             cc=payload["cc"]
                                             )
        return conversation.__dict__

    def new_customer(self, context, payload):
        """
        triggers when new customer created 
        context holds the headers 
        payload holds the request.body
        """
        customer_embedded = payload.get("_embedded") or {}
        customer = HelpscoutCustomer(first_name=payload.get("firstName") or None,
                                     last_name=payload.get("lastName") or None,
                                     phone=customer_embedded.get(
                                         "phones") if customer_embedded.get("phones") else None,
                                     email=customer_embedded.get(
                                         "emails") if customer_embedded.get("emails") else None,
                                     website=customer_embedded.get(
                                         "websites") if customer_embedded.get("websites") else None,
                                     customer_id=payload.get("id") or None,
                                     job_title=payload.get("jobTitle") or None,
                                     organization=payload.get(
                                         "organization") or None,
                                     address=customer_embedded.get(
                                         "address") or None
                                     )

        return customer.__dict__

    def new_conversation_assigned(self, context, payload):
        """
        triggers when new conversation asssigned created 
        context holds the headers 
        payload holds the request.body
        """
        #new coversation assigned and new conversation holding same payload
        return self.new_conversation(context, payload)
