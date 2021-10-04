import json
from email_newsletters.aweber import util
from email_newsletters.aweber.entities.aweber_tag import AweberTag
from email_newsletters.aweber.entities.aweber_list import AweberList
from email_newsletters.aweber.entities.aweber_customfield import AweberCustomfield
from email_newsletters.aweber.entities.aweber_subscriber import AweberSubscriber

class AweberApi():

    def subscriber(self, context, payload):
        '''get subscriber details'''

        access_token = util.get_acess_token(context["headers"])
        url = f"https://api.aweber.com/1.0/accounts/{payload['account_id']}/lists/{payload['list_id']}/subscribers/{payload['subscriber_id']}"
        response = json.loads(util.rest("GET", url, {}, access_token).text)
        subscriber = AweberSubscriber(
            subscriber_id=response.get('id'),
            email=response.get('email'),
            name=response.get('name'),
            tags=response.get('tags'),
            city=response.get('city'),
            country=response.get('country'),
            status=response.get('status')
        )

        return subscriber.__dict__

    def list(self, context, payload):
        '''get specified list details'''

        access_token = util.get_acess_token(context["headers"])
        url = f"https://api.aweber.com/1.0/accounts/{payload['account_id']}/lists/{payload['list_id']}"
        response = json.loads(util.rest("GET", url, {}, access_token).text)
        list_obj = AweberList(
            list_id=response.get('id'),
            title=response.get('name'),
            total_subscribers=response.get('total_subscribers'),
            total_unconfirmed_subscribers=response.get(
                'total_unconfirmed_subscribers')
        )

        return list_obj.__dict__

    def subscriber_by_email(self, context, payload):
        '''get subscriber by email '''

        access_token = util.get_acess_token(context["headers"])
        url = f"https://api.aweber.com/1.0/accounts/{payload['account_id']}/lists/{payload['list_id']}/subscribers"
        subscribers = json.loads(
            util.rest("GET", url, {}, access_token).text)['entries']
        subscriber = [
            subscriber for subscriber in subscribers if payload["email"] == subscriber['email']]
        subscriber = subscriber[0]
        subscriber_obj = AweberSubscriber(
            subscriber_id=subscriber.get('id'),
            email=subscriber.get('email'),
            name=subscriber.get('name'),
            tags=subscriber.get('tags'),
            city=subscriber.get('city'),
            country=subscriber.get('country'),
            status=subscriber.get('status')
        )

        return subscriber_obj.__dict__

    def custom_field(self, context, payload):
        '''list of custom fields'''

        access_token = util.get_acess_token(context["headers"])
        url = f"https://api.aweber.com/1.0/accounts/{payload['account_id']}/lists/{payload['list_id']}/custom_fields"
        custom_fields_list = json.loads(
            util.rest("GET", url, {}, access_token).text)['entries']
        custom_fields = []
        for customfield in custom_fields_list:
            customfield_obj = AweberCustomfield(
                custom_field_id=customfield.get('custom_field_id'),
                name=customfield.get('name'),
                is_subscriber_updateable=customfield.get(
                    'is_subscriber_updateable')
            )
            custom_fields.append(customfield_obj.__dict__)

        return json.dumps(custom_fields)

    def tags_by_list(self, context, payload):
        '''list of tags'''

        access_token = util.get_acess_token(context["headers"])
        url = f"https://api.aweber.com/1.0/accounts/{payload['account_id']}/lists/{payload['list_id']}/tags"
        tags = []
        tags_list = json.loads(util.rest("GET", url, {}, access_token).text)
        for tag in tags_list:
            tag_obj = AweberTag(
                tag_name=tag
            )
            tags.append(tag_obj.__dict__)

        return json.dumps(tags)

    def profile(self, context, payload):
        '''get subscriber details'''

        access_token = util.get_acess_token(context["headers"])
        url = f"https://api.aweber.com/1.0/accounts"
        response = util.rest("GET", url, {}, access_token).json()
        profile = {
            'id':response['entries'][0]['id']
        }

        return profile