from email_newsletters.mailchimp.entities.mailchimp_subscriber import MailchimpSubscriber
from email_newsletters.mailchimp.entities.mailchimp_campaign import MailchimpCampaign
from email_newsletters.mailchimp.entities.mailchimp_list import MailchimpList
from email_newsletters.mailchimp.entities.mailchimp_report import MailchimpReport
from email_newsletters.mailchimp.entities.mailchimp_list_activitie import MailchimpListActivity
from email_newsletters.mailchimp.entities.mailchimp_member_activity import MailchimpMemberActivity
from email_newsletters.mailchimp.entities.mailchim_tag import MailchimpTag
from email_newsletters.mailchimp import util
import json


class MailchimpApi:
    def subscriber_by_email(self, context, params):
        '''Get Subscriber For provided Email '''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        audiance_id = params.get('audiance_id') or params.get('list_id')
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{audiance_id}/members/{params.get('email')}"
        response = util.rest("GET", url, api_key)
        subscribers = []
        subscribers.append(json.loads(response.text))

        return json.dumps(self.subscriber_mappings(subscribers)), response.status_code

    def subscribers(self, context, params):
        '''Get  Susbsciber from a audiance'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        audiance_id = params.get('audiance_id') or params.get('list_id')
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{audiance_id}/members"
        response = util.rest("GET", url, api_key)

        return json.dumps(self.subscriber_mappings(json.loads(response.text)['members'])), response.status_code

    def subscriber(self, context, params):
        '''Get Susbsciber for the provided Subscriber id'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        audiance_id = params.get('audiance_id') or params.get('list_id')
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{audiance_id}/members/{params.get('subscriber_id')}"
        response = util.rest("GET", url, api_key)
        subscribers = []
        subscribers.append(json.loads(response.text))

        return json.dumps(self.subscriber_mappings(subscribers)), response.status_code

    def subscriber_mappings(self, subscriber_list):
        subscribers = []
        for subscriber in subscriber_list:
            subscriber_obj = MailchimpSubscriber(
                subscriber_id = subscriber.get('id'),
                email = subscriber.get('email_address'),
                name = subscriber.get('full_name'),
                audience_id = subscriber.get('list_id'),
                tags = subscriber.get('tags'),
                first_name = subscriber.get('merge_fields').get('FNAME'),
                last_name = subscriber.get('merge_fields').get('LNAME'),
                street = subscriber.get('merge_fields').get('ADDRESS').get(
                    'addr1') if subscriber.get('merge_fields').get('ADDRESS') else None,
                address2 = subscriber.get('merge_fields').get('ADDRESS').get(
                    'addr2') if subscriber.get('merge_fields').get('ADDRESS') else None,
                city = subscriber.get('merge_fields').get('ADDRESS').get(
                    'city') if subscriber.get('merge_fields').get('ADDRESS') else None,
                state = subscriber.get('merge_fields').get('ADDRESS').get(
                    'state') if subscriber.get('merge_fields').get('ADDRESS') else None,
                zip = subscriber.get('merge_fields').get('ADDRESS').get(
                    'zip')if subscriber.get('merge_fields').get('ADDRESS') else None,
                country = subscriber.get('merge_fields').get('ADDRESS').get(
                    'country') if subscriber.get('merge_fields').get('ADDRESS') else None,
                phone = subscriber.get('PHONE'),
                birthday = subscriber.get('BIRTHDAY')
            )
            subscribers.append(subscriber_obj.__dict__)
        return subscribers

    def campaign(self, context, params):
        '''Get Campaign for the provided Campaign Id'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        url = f"https://{domain}.api.mailchimp.com/3.0/campaigns/{params['campaign_id']}"
        response = util.rest("GET", url, api_key)
        campaigns = []
        campaigns.append(json.loads(response.text))

        return json.dumps(self.campaigns_mappings(campaigns)), response.status_code

    def campaigns(self, context, params):
        '''get All Campaign in Account'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        url = f"https://{domain}.api.mailchimp.com/3.0/campaigns"
        response = util.rest("GET", url, api_key)

        return json.dumps(self.campaigns_mappings(json.loads(response.text)['campaigns'])), response.status_code

    def campaigns_mappings(self, campaigns_list):
        campaigns = []
        for campaign in campaigns_list:
            camp_obj = MailchimpCampaign(
                campaign_id = campaign.get('id'),
                campaign_name = campaign.get('settings').get('title'),
                audience_id = campaign.get('recipients').get('list_id'),
                subject = campaign.get('settings').get('subject_line'),
                preview_text = campaign.get('settings').get('preview_text'),
                from_email = campaign.get('settings').get('reply_to'),
                from_name = campaign.get('settings').get('from_name'),
                to_name = campaign.get('settings').get('to_name')
            )
            campaigns.append(camp_obj.__dict__)
        
        return campaigns

    def list(self, context, params):
        '''get specified list in Account'''

        return self.audiance(context, params)

    def audiance(self, context, params):
        '''get specified Audiances in Account'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        audiance_id = params.get('audiance_id') or params.get('list_id')
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{audiance_id}"
        response = util.rest("GET", url, api_key)
        lists = []
        lists.append(json.loads(response.text))

        return json.dumps(self.audiance_mappings(lists)), response.status_code

    def lists(self, context, params):
        '''get All lists in Account'''
        
        return self.audiances(context, params)
    
    def audiances(self, context, params):
        '''get All Audiances in Account'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        url = f"https://{domain}.api.mailchimp.com/3.0/lists"
        response = util.rest("GET", url, api_key)

        return json.dumps(self.audiance_mappings(json.loads(response.text)['lists'])), response.status_code

    def audiance_mappings(self, audiances_list):
        audiances = []
        for audiance in audiances_list:
            audiance_obj = MailchimpList(
                audience_id = audiance.get('id'),
                name = audiance.get('name'),
                company = audiance.get('contact').get('company'),
                street = audiance.get('contact').get('address1'),
                address2 = audiance.get('contact').get('address2'),
                city = audiance.get('contact').get('city'),
                state = audiance.get('contact').get('state'),
                zip = audiance.get('contact').get('zip'),
                country = audiance.get('contact').get('country'),
                phone = audiance.get('contact').get('phone'),
                permission_reminder = audiance.get('permission_reminder'),
                email_type_option = audiance.get('email_type_option'),
                from_name = audiance.get('campaign_defaults').get('from_name'),
                from_email = audiance.get('campaign_defaults').get('from_email'),
                subject = audiance.get('campaign_defaults').get('subject'),
                language = audiance.get('campaign_defaults').get('language'),
            )
            audiances.append(audiance_obj.__dict__)
        return audiances

    def campaign_report(self, context, params):
        '''Get campaign Report of a Campaign'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        url = f"https://{domain}.api.mailchimp.com/3.0/reports/{params['campaign_id']}"
        response = util.rest("GET", url, api_key)
        campaign = json.loads(response.text)
        campaign_obj = MailchimpReport(
            campaign_id = campaign.get('id'),
            campaign_name = campaign.get('campaign_title'),
            audience_id = campaign.get('list_id'),
            audience_name = campaign.get('list_name'),
            subject_line = campaign.get('subject_line'),
            preview_text = campaign.get('preview_text'),
            emails_sent = campaign.get('emails_sent'),
            abuse_reports = campaign.get('abuse_reports'),
            unsubscribed = campaign.get('unsubscribed'),
            hard_bounces = campaign.get('bounces').get('hard_bounces'),
            soft_bounces = campaign.get('bounces').get('soft_bounces'),
            forwards_count = campaign.get('forwards').get('forwards_count'),
            forwards_opens = campaign.get('forwards').get('forwards_opens'),
            opens_total = campaign.get('opens').get('opens_total'),
            unique_clicks = campaign.get('opens').get('unique_clicks'),
        )

        return campaign_obj.__dict__
    
    def list_activities(self,context,params):
        '''Retrieves up to the previous 180 days of daily detailed aggregated activity stats for a list.'''
        
        return self.audiance_activity(context, params)
    
    def audiance_activity(self, context, params):
        '''Retrieves up to the previous 180 days of daily detailed aggregated activity stats for a audiance.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        audiance_id = params.get('audiance_id') or params.get('list_id')
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{audiance_id}/activity"
        response = util.rest("GET", url, api_key)
        audiance_activity_list = json.loads(response.text)['activity']
        audiance_activitys = []

        for audiance_activity in audiance_activity_list:
            activity_obj = MailchimpListActivity(
                day = audiance_activity.get('day'),
                emails_sent = audiance_activity.get('emails_sent'),
                unique_opens = audiance_activity.get('day'),
                recipient_clicks = audiance_activity.get('recipient_clicks'),
                hard_bounce = audiance_activity.get('hard_bounce'),
                soft_bounce = audiance_activity.get('soft_bounce'),
                subs = audiance_activity.get('subs'),
                unsubs = audiance_activity.get('unsubs'),
                other_adds = audiance_activity.get('other_adds'),
                other_removes = audiance_activity.get('other_removes')
            )
            audiance_activitys.append(activity_obj.__dict__)

        return json.dumps(audiance_activitys)

    def list_member_activities(self, context, params):
        '''Get the last 50 events of a member's activity on a specific list.'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{params['audiance_id']}/members/{params['email']}/activity"
        response = util.rest("GET", url, api_key)
        member_activities = json.loads(response.text)
        activites_obj = MailchimpMemberActivity(
            activity = member_activities.get('activity'),
            email_id = member_activities.get('email_id'),
            audiance_id = member_activities.get('list_id'),
            total_items = member_activities.get('total_items')
        )

        return json.dumps(activites_obj.__dict__)

    def segment_members(self, context, params):
        '''Get  Susbsciber from a audiance'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        audiance_id = params.get('audiance_id') or params.get('list_id')
        url = f"https://{domain}.api.mailchimp.com/3.0/lists/{audiance_id}/segments/{params['segment_id']}/members"
        response = util.rest("GET", url, api_key)

        return json.dumps(self.subscriber_mappings(json.loads(response.text)['members'])), response.status_code

    def member_tags(self, context, params):
        '''Get  Susbsciber from a audiance'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        audiance_id = params.get('audiance_id') or params.get('list_id')
        url = f"https://us2.api.mailchimp.com/3.0/lists/{audiance_id}/members/{params['email']}/tags"
        response = util.rest("GET", url, api_key)
        member_tag_list = json.loads(response.text)['tags']

        if len(member_tag_list) == 0:
            raise Exception('No members for specified tag id')

        member_tags = []
        for tag in member_tag_list:
            tag_obj = MailchimpTag(
                tag_id=tag.get('id'),
                tag_name=tag.get('name')
            )
            member_tags.append(tag_obj.__dict__)

        return json.dumps(member_tags)

    def verify(self, context, params):
        '''Verify details'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        url = f"https://{domain}.api.mailchimp.com/3.0/ping"
        response = util.rest("GET", url, api_key)
        return response.text, response.status_code
    
    def profile(self, context, params):
        '''Details of authenticated user'''

        api_key = context['headers']['api_key']
        domain = api_key.split("-")[1]
        url = f"https://{domain}.api.mailchimp.com/3.0"
        response = util.rest("GET", url, api_key).json()
        profile = {
            'id':response['account_id'],
            'email':response['email'],
            'name':response['first_name']
        }
        return profile