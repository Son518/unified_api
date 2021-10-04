import json
from typing import Pattern
from email_newsletters.mailjet import util
from email_newsletters.mailjet.entities.mailjet_subscriber import MailjetSubscriber
from email_newsletters.mailjet.entities.mailjet_campaign import MailjetCampaign


class MailjetApi():

    def subscribers(self, context, payload):
        """ Get subscribers by Id"""

        mailjet_client = util.mailjet_client(context['headers'])
        subscribers_list = json.loads(mailjet_client.contact.get().text)
        subscribers_value = subscribers_list.get('Data') or {}
        subscribers_obj = []

        for subscriber in subscribers_value:
            subscriber_seq = MailjetSubscriber(email=subscriber.get(
                'Email'), name=subscriber.get('Name'), account_id=subscriber.get('ID'))
            subscribers_obj.append(subscriber_seq.__dict__)

        return json.dumps(subscribers_obj)

    def contacts(self, context, payload):
        """ Get list of contacts"""

        return self.subscribers(context, payload)


    def subscriber(self, context, params):
        """ Get subscriber by Id"""
        
        mailjet_client = util.mailjet_client(context['headers'])
        subscriber = json.loads(mailjet_client.contact.get(
            id=params.get("account_id")).text)

        subscriber_value = subscriber.get('Data')[0] or {}
        subscriber_obj = MailjetSubscriber(email=subscriber_value.get(
            'Email'), name=subscriber_value.get('Name'), account_id=subscriber_value.get('ID'))

        return subscriber_obj.__dict__

    def contact(self, context, payload):
        """ Get a contact by Id"""

        return self.subscriber(context, payload)


    def campaigns(self, context, payload):
        """ Get campaigns by Id"""

        mailjet_client = util.mailjet_client(context['headers'])
        campaigns_list = json.loads(mailjet_client.campaign.get().text)
        camapigns_value = campaigns_list.get('Data') or {}
        campaigns_obj = []

        for campaign in camapigns_value:
            campaign_seq = MailjetCampaign(email=campaign.get(
                'Email') or None, name=campaign.get('Name') or None, account_id=campaign.get('ID') or None)
            campaigns_obj.append(campaign_seq.__dict__)

        return json.dumps(campaigns_obj)


    def campaign(self, context, payload):
        """ Get campaign by list_id"""

        mailjet_client = util.mailjet_client(context['headers'])
        campaigns = mailjet_client.campaign.get(
            id=payload.get("list_id")).text
        return json.loads(campaigns)

    def campaigns_created_by_time(self, context, payload):
        """ Get campaign by created_time"""

        mailjet_client = util.mailjet_client(context['headers'])
        campaigns = mailjet_client.campaign.get(
            created_at=payload.get("created_time")).text
        return json.loads(campaigns)


    def messages(self, context, payload):
        """ Get Messages"""

        mailjet_client = util.mailjet_client(context['headers'])
        campaigns = mailjet_client.message.get().text
        return json.loads(campaigns)


    def draft_campaigns(self, context, payload):
        """ Get Daft Campaign data"""

        mailjet_client = util.mailjet_client(context['headers'])
        campaigns = mailjet_client.campaigndraft.get().text
        return json.loads(campaigns)

    def profile(self,context,payload):
        """
        get call to show user authenticated information
        """
        mailjet_client = util.mailjet_client(context['headers'])
        response = mailjet_client.myprofile.get().json()
        profile = {
            'id':response['Data'][0]['UserID'],
            'name':response['Data'][0]['Firstname'],
            'email':response['Data'][0]['BillingEmail']
        }
        return profile
    
    def verify(self,context,params):
        """
        get call to verify user authenticated information
        """
        mailjet_client = util.mailjet_client(context['headers'])
        response = mailjet_client.myprofile.get()
        return response.json()