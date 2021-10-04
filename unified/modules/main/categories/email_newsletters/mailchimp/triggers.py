from unified.core.triggers import Triggers
from email_newsletters.mailchimp.entities.mailchimp_subscriber import MailchimpSubscriber


class MailchimpTrigger(Triggers):
    def new_subscriber(self, context, payload):
        '''Triggers when a subscriber is added in an audience.'''

        return self.subscriber_mapping(payload)

    def new_unsubscriber(self, context, payload):
        '''Triggers when a unsubscriber is added in an audience.'''

        return self.subscriber_mapping(payload)

    def subscriber_mapping(self, payload):
        subscriber = MailchimpSubscriber(
            subscriber_id = payload.get('data[id]'),
            email = payload.get('data[email]'),
            audience_id = payload.get('data[list_id]'),
            first_name = payload.get('data[merges][FNAME]'),
            last_name = payload.get('data[merges][LNAME]'),
            street = payload.get('data[merges][ADDRESS][addr1]'),
            address2 = payload.get('data[merges][ADDRESS][addr2]'),
            city = payload.get('data[merges][ADDRESS][city]'),
            state = payload.get('data[merges][ADDRESS][state]'),
            zip = payload.get('data[merges][ADDRESS][zip]'),
            country = payload.get('data[merges][ADDRESS][country]'),
            phone = payload.get('data[merges][PHONE]'),
            birthday = payload.get('data[merges][BIRTHDAY]')
        )
        return subscriber.__dict__
