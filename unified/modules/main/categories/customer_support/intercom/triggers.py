import json
from core.triggers import Triggers
from customer_support.intercom import util
from customer_support.intercom.entities.intercom_contact import IntercomContact


class IntercomTriggers(Triggers):

    def new_user(self, context, payload):
        """
        triggers when new user created
        context holds headers
        payload holds request.body
        """
        data = payload["data"]
        user_obj = IntercomContact(email=data["item"]["email"],
                                   full_name=data["item"]["name"],
                                   user_id=data["item"]["id"],
                                   created_date=data["item"]["created_at"] if '-' in str(data["item"]["created_at"]) else util.epoch_to_date(
            data["item"]["created_at"]),
            unsubscribed=data["item"]["unsubscribed_from_emails"],
            lookup_email=data["item"]["email"],
            phone_number=data["item"]["phone"],
            unsubscribed_from_emails=data["item"]["unsubscribed_from_emails"],
            company=data["item"]["companies"],
            tag_name=data["item"]["tags"],
            user=data["item"]["id"],
            tag_id=data["item"]["tags"]["tags"],
            id=data["item"]["id"],
        )
        return user_obj.__dict__

    def new_lead(self, context, payload):
        """
        triggers when new lead created
        context holds headers
        payload holds request.body
        """
        data = payload["data"]
        lead_obj = IntercomContact(email=data["item"]["email"],
                                   full_name=data["item"]["name"],
                                   lead_id=data["item"]["id"],
                                   lead=data["item"]["id"],
                                   created_date=data["item"]["created_at"] if '-' in str(data["item"]["created_at"]) else util.epoch_to_date(
            data["item"]["created_at"]),
            unsubscribed=data["item"]["unsubscribed_from_emails"],
            lookup_email=data["item"]["email"],
            phone_number=data["item"]["phone"],
            unsubscribed_from_emails=data["item"]["unsubscribed_from_emails"],
            company=data["item"]["companies"],
            tag_name=data["item"]["tags"],
            tag_id=data["item"]["tags"],
            id=data["item"]["id"],
        )
        return lead_obj.__dict__

    def new_unsubscription(self, context, payload):
        """
        triggers when user or lead unsubscribed
        context holds headers
        payload holds request.body
        """
        data = payload["data"]
        unsubscription_obj = IntercomContact(email=data["item"]["email"],
                                             full_name=data["item"]["name"],
                                             user_id=data["item"]["id"],
                                             created_date=data["item"]["created_at"] if '-' in str(data["item"]["created_at"]) else util.epoch_to_date(
                                                 data["item"]["created_at"]),
                                             unsubscribed=data["item"]["unsubscribed_from_emails"],
                                             lookup_email=data["item"]["email"],
                                             phone_number=data["item"]["phone"],
                                             unsubscribed_from_emails=data["item"]["unsubscribed_from_emails"],
                                             company=data["item"]["companies"],
                                             tag_name=data["item"]["tags"]["tags"],
                                             user=data["item"]["id"],
                                             tag_id=data["item"]["tags"],
                                             id=data["item"]["id"],
                                             )
        return unsubscription_obj.__dict__

    def tag_added_to_lead(self, context, payload):
        """
        triggers when tag added to lead
        context holds headers
        payload holds request.body
        """
        data = payload["data"]["item"]["contact"]
        created_date = payload["data"]["item"]["created_at"]
        tag_obj = IntercomContact(email=data["email"],
                                  full_name=data["name"],
                                  created_date=util.epoch_to_date(created_date),
            unsubscribed=data["unsubscribed_from_emails"],
            lookup_email=data["email"],
            phone_number=data["phone"],
            unsubscribed_from_emails=data["unsubscribed_from_emails"],
            company=data["companies"],
            tag_name=payload["data"]["item"]["tag"]["name"],
            lead=data["id"],
            lead_id=data["id"],
            tag_id=payload["data"]["item"]["tag"]["id"],
            id=data["id"],
        )
        return tag_obj.__dict__

    def tag_added_to_user(self, context, payload):
        """
        triggers when tag added to user
        context holds headers
        payload holds request.body
        """
        data = payload["data"]["item"]["user"]
        created_date = payload["data"]["item"]["created_at"]
        tag_obj = IntercomContact(email=data["email"],
                                  full_name=data["name"],
                                  created_date=util.epoch_to_date(created_date),
            unsubscribed=data["unsubscribed_from_emails"],
            lookup_email=data["email"],
            phone_number=data["phone"],
            unsubscribed_from_emails=data["unsubscribed_from_emails"],
            company=data["companies"],
            tag_name=payload["data"]["item"]["tag"]["name"],
            user=data["id"],
            user_id=data["id"],
            tag_id=payload["data"]["item"]["tag"]["id"],
            id=data["id"],
        )
        return tag_obj.__dict__
