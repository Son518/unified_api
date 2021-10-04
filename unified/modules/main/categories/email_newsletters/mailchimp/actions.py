from unified.core.actions import Actions
from email_newsletters.mailchimp import util
from email_newsletters.mailchimp.entities.mailchimp_subscriber import MailchimpSubscriber
from email_newsletters.mailchimp.entities.mailchimp_campaign import MailchimpCampaign
from email_newsletters.mailchimp.entities.mailchimp_list import MailchimpList


import json


class MailchimpAction(Actions):

    def add_subscriber(self, context, payload):
        '''Add a new subscriber to an audience of your choosing.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]

        subscriber = MailchimpSubscriber(**payload)

        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{subscriber.audience_id}/members"

        subscriber_body = {
            'email_address': subscriber.email,
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': subscriber.first_name,
                'LNAME': subscriber.last_name,
                'EMAIL': subscriber.email,
                "ADDRESS": {
                    "addr1": subscriber.street,
                    "addr2": subscriber.address2,
                    "city": subscriber.city,
                    "state": subscriber.state,
                    "zip": subscriber.zip,
                },
                "BIRTHDAY": subscriber.birthday,
                "country": subscriber.country,
                "PHONE": subscriber.phone
            },
        }

        response = util.rest("POST", url, api_key, subscriber_body)

        return response.text, response.status_code

    def update_subscriber(self, context, payload):
        '''Update subscriber to an audience of your choosing.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]

        subscriber = MailchimpSubscriber(**payload)

        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{subscriber.audience_id}/members/{subscriber.email}"

        subscriber_body = {
            'email_address': subscriber.email,
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': subscriber.first_name,
                'LNAME': subscriber.last_name,
                'EMAIL': subscriber.email,
                "ADDRESS": {
                    "addr1": subscriber.street,
                    "addr2": subscriber.address2,
                    "city": subscriber.city,
                    "state": subscriber.state,
                    "zip": subscriber.zip,
                },
                "BIRTHDAY": subscriber.birthday,
                "country": subscriber.country,
                "PHONE": subscriber.phone
            },
        }
        response = util.rest("PUT", url, api_key, subscriber_body)
        return response.text, response.status_code

    def delete_subscriber(self, context, payload):
        '''Delete subscriber to an audience of your choosing.'''
 
        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        subscriber = MailchimpSubscriber(**payload)
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{subscriber.audience_id}/members/{subscriber.subscriber_id}/actions/delete-permanent"
        response = util.rest("POST", url, api_key)
        return response.text, response.status_code

    def unsubscribe_email(self, context, payload):
        '''Unsubscribe an email address from an audience of your choosing.'''
        
        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        subscriber = MailchimpSubscriber(**payload)

        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{subscriber.audience_id}/members/{subscriber.email}"

        subscriber_body = {
            'email_address': subscriber.email,
            'status': 'unsubscribed'
        }
        response = util.rest("PUT", url, api_key, subscriber_body)
        return response.text, response.status_code

    def create_campaign(self, context, payload):
        '''Creates a campaign draft.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        url = f'https://{domain}.api.mailchimp.com/3.0/campaigns'
        campaign = MailchimpCampaign(**payload)

        campaign_body = {
            "type": "regular",
            "recipients": {
                "list_id": campaign.audience_id
            },  
            "settings": {
                "title": campaign.campaign_name,
                "subject_line": campaign.subject,
                "preview_text": campaign.preview_text,
                "from_name": campaign.from_name,
                "reply_to": campaign.from_email,
                "to_name": campaign.to_name
            },
            "content_type": "template"
        }

        response = util.rest("POST", url, api_key, campaign_body)
        return response.text, response.status_code

    def delete_campaign(self, context, payload):
        '''Delete a campaign .'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        campaign = MailchimpCampaign(**payload)
        url = f'https://{domain}.api.mailchimp.com/3.0/campaigns/{campaign.campaign_id}'

        response = util.rest("DELETE", url, api_key)
        return response.text, response.status_code

    def update_campaign(self, context, payload):
        '''update a campaign of you choose.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        campaign = MailchimpCampaign(**payload)

        url = f'https://{domain}.api.mailchimp.com/3.0/campaigns/{campaign.campaign_id}'

        campaign_body = {
            "type": "regular",
            "recipients": {
                "list_id": campaign.audience_id
            },
            "settings": {
                "title": campaign.campaign_name,
                "subject_line": campaign.subject,
                "preview_text": campaign.preview_text,
                "from_name": campaign.from_name,
                "reply_to": campaign.from_email,
                "to_name": campaign.to_name
            },
            "content_type": "template"
        }

        response = util.rest("PATCH", url, api_key, campaign_body)
        return response.text, response.status_code

    def send_campaign(self, context, payload):
        '''Sends a campaign of your choose'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        campaign = MailchimpCampaign(**payload)
        url = f'https://{domain}.api.mailchimp.com/3.0/campaigns/{campaign.campaign_id}/actions/send'

        response = util.rest("POST", url, api_key)
        return response.text, response.status_code

    def add_note_to_subscriber(self, context, payload):
        '''Adds a new note to an existing subscriber.'''
       
        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        subscriber = MailchimpSubscriber(**payload)
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{subscriber.audience_id}/members/{subscriber.subscriber_id}/notes"
        note_body = {
            "note": subscriber.note,
            "list_id": subscriber.audience_id,
            "subscriber_id": subscriber.subscriber_id
        }
        response = util.rest("POST", url, api_key, note_body)
        return response.text, response.status_code

    def add_subscriber_to_tag(self, context, payload):
        '''Add an email address to a tag within an audience.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        subscriber = MailchimpSubscriber(**payload)
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{subscriber.audience_id}/segments/{subscriber.tag_id}"
        tag_body = {"members_to_add": [
            subscriber.email
        ]}
        response = util.rest("POST", url, api_key, tag_body)
        return response.text, response.status_code

    def remove_subscriber_from_tag(self, context, payload):
        '''Removes an existing subscriber by email address from a tag within an audience.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        subscriber = MailchimpSubscriber(**payload)
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{subscriber.audience_id}/segments/{subscriber.tag_id}"
        tag_body = {"members_to_remove": [
            subscriber.email
        ]}
        response = util.rest("POST", url, api_key, tag_body)
        return response.text, response.status_code
    
    def create_list(self, context, payload):
        '''creates a list'''

        return self.create_audience(context, payload)
    
    def create_audience(self, context, payload):
        '''Creates a Audience.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        url = f'https://{domain}.api.mailchimp.com/3.0/lists'
        audience = MailchimpList(**payload)
        audience_body = {
            "name": audience.name,
            "contact": {
                "company": audience.company,
                "address1": audience.street,
                "address2": audience.address2,
                "city": audience.city,
                "state": audience.state,
                "zip": audience.zip,
                "country": audience.country,
                "phone": audience.phone
            },
            "permission_reminder": audience.permission_reminder,
            "email_type_option": audience.email_type_option,
            "campaign_defaults": {
                "from_name": audience.from_name,
                "from_email": audience.from_email,
                "subject": audience.subject,
                "language": audience.language
            }
        }
        response = util.rest("POST", url, api_key, audience_body)
        return response.text, response.status_code
    
    def update_list(self,context,payload):
        '''update list'''

        return self.update_audience(context, payload)
    
    def update_audience(self, context, payload):
        '''updates a Audience.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        audience = MailchimpList(**payload)

        url = f'https://{domain}.api.mailchimp.com/3.0/lists/{audience.audience_id}'
        audience_body = {
            "name": audience.name,
            "contact": {
                "company": audience.company,
                "address1": audience.street,
                "address2": audience.address2,
                "city": audience.city,
                "state": audience.state,
                "zip": audience.zip,
                "country": audience.country,
                "phone": audience.phone
            },
            "permission_reminder": audience.permission_reminder,
            "email_type_option": audience.email_type_option,
            "campaign_defaults": {
                "from_name": audience.from_name,
                "from_email": audience.from_email,
                "subject": audience.subject,
                "language": audience.language
            }
        }
        response = util.rest("PATCH", url, api_key, audience_body)
        
        return response.text, response.status_code

    def remove_member_from_segment(self, context, payload):
        '''Removes an existing subscriber by email address from a segment within an audience.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        subscriber = MailchimpSubscriber(**payload)
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{subscriber.audience_id}/segments/{subscriber.segment_id}"
        tag_body = {"members_to_remove": [
            subscriber.email
        ]}
        response = util.rest("POST", url, api_key, tag_body)
        return response.text, response.status_code

    def cancel_campaign(self, context, payload):
        '''Cancel a Campaign'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        campaign = MailchimpCampaign(**payload)
        url = f'https://{domain}.api.mailchimp.com/3.0/campaigns/{campaign.campaign_id}actions/cancel-send'

        response = util.rest("POST", url, api_key)
        return response.text, response.status_code

    def peform_campaign_action(self, context, payload):
        '''Peform Action of Campaign like cancel Campaign and Send Campaign'''
        
        campine_id = {
            'campaign_id': payload['campaign_id']
        }
        if payload.get('action_type') == 'cancel_campaign':
            return self.cancel_campaign(context, campine_id)
        else:
            return self.send_campaign(context, campine_id)
