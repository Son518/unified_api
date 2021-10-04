from unified.core.triggers import Triggers
from email_marketing.entities.email import Email


class MailsendTriggers(Triggers):

    def email_clicked(self, context, payload):
        email_click= Email(
            email = payload['email'],
            event_type= payload['event'],
            timestamp= payload['timestamp']
        ).__dict__
        return email_click 

    def email_opened(self, context, payload):
        email_open= Email(
            email = payload['email'],
            event_type= payload['event'],
            timestamp= payload['timestamp']
        ).__dict__
        return email_open

    def email_unsubscribe(self, context, payload):
        email_open= Email(
            email = payload['email'],
            event_type= payload['event'],
            timestamp= payload['timestamp']
        ).__dict__
        return email_open 