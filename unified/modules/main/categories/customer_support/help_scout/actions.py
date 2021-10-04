import json
from flask import jsonify
from core.actions import Actions
from customer_support.help_scout import util
from customer_support.help_scout.entities.help_scout_conversation import HelpscoutConversation
from customer_support.help_scout.entities.help_scout_customer import HelpscoutCustomer


class HelpscoutActions(Actions):

    def create_conversation(self, context, conversation_payload):
        """
        creates a conversation
        context holds the headers 
        conversation_payload holds the request.body
        """
        access_token = util.help_scout_token(context["headers"])
        conversation_entity = HelpscoutConversation(**conversation_payload)
        conversation_data = {
                            "subject": conversation_entity.subject,
                            "autoReply": conversation_entity.trigger_auto_reply,
                            "imported": conversation_entity.import_only,
                            "customer": {
                                "email": conversation_entity.customer_email
                                        },
                            "mailboxId": conversation_entity.mailbox_id,
                            "type": "email",
                            "status": "active",
                            "threads": [{
                                "type": "customer",
                                "customer": {
                                    "email": conversation_entity.customer_email
                                            },
                                "text": conversation_entity.text
                                        }],
                            "tags": [conversation_entity.tag] if conversation_entity.tag else [" "]
                            }
        response = util.rest("POST", "conversations",
                             conversation_data, access_token)
        if response.status_code == 201:
            return {"status": "completed"}
        return json.loads(response.text)

    def create_customer(self, context, customer_payload):
        """
        creates a customer
        context holds the headers 
        customer_payload holds the request.body
        """
        access_token = util.help_scout_token(context["headers"])
        customer_entity = HelpscoutCustomer(**customer_payload)
        customer_data = {
                         "firstName": customer_entity.first_name,
                         "lastName": customer_entity.last_name,
                         "jobTitle": customer_entity.job_title,
                         "location": customer_entity.location,
                         "organization": customer_entity.organization,
                         "emails": [{
                             "type": "work",
                             "value": customer_entity.email
                         }],
                         "phones": [{
                             "type": "work",
                             "value": customer_entity.phone
                         }],
                         "websites": [{"value": customer_entity.website}],
                         "address": {
                             "city": customer_entity.city,
                             "state": customer_entity.state,
                             "postalCode": customer_entity.pin_code,
                             "country": customer_entity.country,
                             "lines": [customer_entity.address]
                                    }
                        }
        response = util.rest("POST", "customers", customer_data, access_token)
        if response.status_code == 201:
            return {"status": "completed"}
        return json.loads(response.text)

    def add_note_to_conversation(self, context, note_payload):
        """
        adds note to conversation
        context holds the headers 
        note_payload holds the request.body
        """
        access_token = util.help_scout_token(context["headers"])
        note_entity = HelpscoutConversation(**note_payload)
        note_data = {"text": note_entity.text}
        response = util.rest("POST", "notes", note_data,
                             access_token, note_entity.conversation_id)
        if response.status_code == 201:
            return {"status": "completed"}
        return json.loads(response.text)

    def send_reply(self, context, reply_payload):
        """
        sends reply in conversation
        context holds the headers 
        reply_payload holds the request.body
        """
        access_token = util.help_scout_token(context["headers"])
        reply_entity = HelpscoutConversation(**reply_payload)
        reply_data = {
                    "customer": {
                        "id": reply_entity.customer_id
                                },
                    "text": reply_entity.text,
                    "draft": reply_entity.create_as_draft,
                    "user": reply_entity.user_id
                    }
        response = util.rest("POST", "reply", reply_data,
                             access_token, reply_entity.conversation_id)
        if response.status_code == 201:
            return {"status": "completed"}
        return json.loads(response.text)
