from unified.core.triggers import Triggers
from email_newsletters.mailerlite.entities.mailerlite_subsciber import MalierliteSubscriber


class MailerliteTriggers(Triggers):

    def new_subscriber(self, context, payload):
        """ New Subscriber"""

        data = MalierliteSubscriber(
            subscriber_id = payload["events"][0]["data"]["subscriber"]["id"],
            email = payload["events"][0]["data"]["subscriber"]["email"],
            name = payload["events"][0]["data"]["subscriber"]["name"],
            type = payload["events"][0]["data"]["subscriber"]["type"],
            account_id = payload["events"][0]["account_id"],
            date_created = payload["events"][0]["data"]["subscriber"]["date_created"]
        )        
        return data.__dict__


    def new_unsubscribe(self, context, payload):
        """ New Unsubscribe"""

        data = MalierliteSubscriber(
            subscriber_id = payload["events"][0]["data"]["subscriber"]["id"],
            email = payload["events"][0]["data"]["subscriber"]["email"],
            name = payload["events"][0]["data"]["subscriber"]["name"],
            type = payload["events"][0]["data"]["subscriber"]["type"],
            account_id = payload["events"][0]["account_id"],
            date_created = payload["events"][0]["data"]["subscriber"]["date_created"],
            date_unsubscribe = payload["events"][0]["data"]["subscriber"]["date_unsubscribe"]
        )
        return data.__dict__


    def subscriber_bounced(self, context, payload):
        """ Subscriber Bounced"""
    
        data = MalierliteSubscriber(
            subscriber_id = payload["events"][0]["data"]["subscriber"]["id"],
            email = payload["events"][0]["data"]["subscriber"]["email"],
            name = payload["events"][0]["data"]["subscriber"]["name"],
            type = payload["events"][0]["data"]["subscriber"]["type"],
            account_id = payload["events"][0]["account_id"],
            date_created = payload["events"][0]["data"]["subscriber"]["date_created"]
        )
        return data.__dict__

    
    def subscriber_removed_from_group(self, context, payload):
        """ Subscriber Removed From Group"""

        data = MalierliteSubscriber(
            subscriber_id = payload["events"][0]["data"]["subscriber"]["id"],
            email = payload["events"][0]["data"]["subscriber"]["email"],
            name = payload["events"][0]["data"]["subscriber"]["name"],
            type = payload["events"][0]["data"]["subscriber"]["type"],
            account_id = payload["events"][0]["account_id"],
            group_id = payload["events"][0]["data"]["group"]["id"],
            date_created = payload["events"][0]["data"]["subscriber"]["date_created"]
        )
        return data.__dict__


    def subscriber_removed_from_group(self, context, payload):
        """ Subscriber Removed From Group"""

        data = MalierliteSubscriber(
            subscriber_id = payload["events"][0]["data"]["subscriber"]["id"],
            email = payload["events"][0]["data"]["subscriber"]["email"],
            name = payload["events"][0]["data"]["subscriber"]["name"],
            type = payload["events"][0]["data"]["subscriber"]["type"],
            account_id = payload["events"][0]["account_id"],
            group_id = payload["events"][0]["data"]["group"]["id"],
            date_created = payload["events"][0]["data"]["subscriber"]["date_created"]
        )
        return data.__dict__


    def subscriber_added_to_group(self, context, payload):
        """ Subscriber Added to Group"""

        data = MalierliteSubscriber(
            subscriber_id = payload["events"][0]["data"]["subscriber"]["id"],
            email = payload["events"][0]["data"]["subscriber"]["email"],
            name = payload["events"][0]["data"]["subscriber"]["name"],
            type = payload["events"][0]["data"]["subscriber"]["type"],
            account_id = payload["events"][0]["account_id"],
            group_id = payload["events"][0]["data"]["group"]["id"],
            date_created = payload["events"][0]["data"]["subscriber"]["date_created"]
        )
        return data.__dict__
