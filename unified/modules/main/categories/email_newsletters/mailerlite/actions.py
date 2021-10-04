from mailerlite import MailerLiteApi
from unified.core.actions import Actions
from email_newsletters.mailerlite.entities.mailerlite_subsciber import MalierliteSubscriber
from email_newsletters.mailerlite.entities.mailerlite_campaign import MalierliteCampaign
from email_newsletters.mailerlite.entities.mailerlite_group import MalierliteGroup
import requests
from flask import jsonify
import json


class MailerliteActions(Actions):

    def add_subscriber(self, context, payload):
        """ Add or create Subscriber  """

        api_key = context.get('headers').get('api_key')        

        if api_key is None:
            raise Exception("Please provide API-Key")     

        api = MailerLiteApi(api_key)
        subscriber = MalierliteSubscriber(**payload)

        data = {
            'name': subscriber.name,
            'email': subscriber.email,
            'fields': {
                'company': subscriber.company
                }
            }
        response = api.subscribers.create(data)
        return response._asdict()


    def update_subscriber(self, context, payload):
        """ Update subscriber """
        
        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")   

        api = MailerLiteApi(api_key)
        subscriber = MalierliteSubscriber(**payload)

        data = {
            'name': subscriber.name,
            'fields': {
                'company': subscriber.company
                }
            }
        response = api.subscribers.update(data, id=subscriber.subscriber_id)
        return response._asdict()


    def delete_subscriber(self, context, payload):
        """" Delete a Subscriber """

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")       

        api = MailerLiteApi(api_key)
        subscriber = MalierliteSubscriber(**payload)
        response = api.groups.delete_subscriber(group_id=subscriber.group_id, subscriber_id=subscriber.subscriber_id)
        return jsonify(response)


    def unsubscribe_email(self, context, payload):
        """  Unsubscribe Email """

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        headers= {
            "X-MailerLite-ApiKey": api_key
        }       

        subscriber = MalierliteSubscriber(**payload)
        response = requests.request("DELETE", f"https://api.mailerlite.com/api/v2/groups/{subscriber.subscriber_group_id}/subscribers/{subscriber.email}", headers=headers).text
        return response


    def create_campain(self, context, payload):
        """ Create Campaign """

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")     

        api = MailerLiteApi(api_key)
        campaign = MalierliteCampaign(**payload)

        data = {
            "subject": campaign.subject,
            "groups": campaign.groups_ids,
            "type": campaign.type
            }
        response = api.campaigns.create(data)
        return jsonify(response)


    def delete_campaign(self, context, payload):
        """ Delete Campaign """

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")   

        api = MailerLiteApi(api_key)
        campaign = MalierliteCampaign(**payload)
        response = api.campaigns.delete(campaign_id=campaign.campaign_id)
        return jsonify(response)
        

    # Send Campaign
    def send_campaign(self, context, payload):
        """ Send Campaign """

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")   

        api = MailerLiteApi(api_key)
        campaign = MalierliteCampaign(**payload)

        headers = {
            "Content-Type": "application/json",
            "X-MailerLite-ApiKey": f"{api_key}"
        }

        url = f"https://api.mailerlite.com/api/v2/campaigns/{campaign.campaign_id}/actions/send"
        response = requests.request("POST", url, headers=headers).text
        return response


    def create_group(self, context, payload):
        """ Create Group"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")   

        api = MailerLiteApi(api_key)
        group = MalierliteGroup(**payload)
        response = api.groups.create(name=group.group_name)
        response = response._asdict()
        response["subscriber_group_id"] = response["id"]

        return response


    def update_group(self, context, payload):
        """  Update Group"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")   

        api = MailerLiteApi(api_key)
        group = MalierliteGroup(**payload)
        response = api.groups.update(group_id=group.group_id, name=group.group_name)
        return response._asdict()

    
    def remove_group(self, context, payload):
        """ Remove Group"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        api = MailerLiteApi(api_key)
        group = MalierliteGroup(**payload)
        headers = {
            "api_key": api_key
        }
        response = api.groups.delete(group_id=payload.get('group_id'))
        return json.dumps(response)


    def add_subscriber_to_group(self, context, payload):
        """ Add Subscriber to a Group"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        api = MailerLiteApi(api_key)
        group = MalierliteGroup(**payload)
        response = api.groups.add_single_subscriber(group_id=group.subscriber_group, subscribers_data={"email": group.email, "name": group.name}, autoresponders=False, resubscribe=False, as_json=False)
        response = response._asdict()
        response["id"] = payload.get("subscriber_group")
        response["subscriber_id"] = response["id"]
        return response


    def remove_member_from_group(self, context, payload):
        """ Remove a Member from a Segment or Group"""

        api_key = context.get('headers').get('api_key')
        if api_key is None:
            raise Exception("Please provide API-Key")
        api = MailerLiteApi(api_key)
        group = MalierliteGroup(**payload)
        response = api.groups.delete_subscriber(group_id=group.subscriber_group_id, subscriber_id=group.subscriber_id)
        return json.dumps(response)