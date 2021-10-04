from unified.core.triggers import Triggers
from email_newsletters.sendinblue.entities.sendinblue_subscriber import SendinblueSubscriber


class SendinblueTriggers(Triggers):

    def new_list(self, context, payload):

        list = SendinblueSubscriber(
            contact_id=payload['id'], 
            email=payload['email'], 
            list_id=payload['list_id'], 
            created_date=payload['date']
        )

        return list.__dict__

    def contact_updated(self, context, payload):

        update_contact = SendinblueSubscriber(
            contact_id=payload['id'],
            created_date=payload['date'],
            email =payload['content'][0]['email'],
            first_name=payload['content'][0]['attributes']['FIRSTNAME'],
            last_name=payload['content'][0]['attributes']['LASTNAME'],
            sms=payload['content'][0]['attributes']['SMS']
        )

        return update_contact.__dict__

    def contact_add_to_specific_list(self, context, payload):
        
        add_contact = SendinblueSubscriber(
            contact_id=payload['id'], 
            email=payload['email'], 
            list_id=payload['list_id'], 
            created_date=payload['date']
        )
        return add_contact.__dict__ 