import json
from unified.core.actions import Actions
from email_newsletters.aweber.entities.aweber_subscriber import AweberSubscriber
from email_newsletters.aweber.entities.aweber_list import AweberList
from email_newsletters.aweber import util


class AweberActions(Actions):

    def add_subscriber(self, context, subscriber_entity):
        '''add a new subscriber'''

        access_token = util.get_acess_token(context["headers"])
        subscriber_schema = AweberSubscriber(**subscriber_entity)
        url = f"https://api.aweber.com/1.0/accounts/{subscriber_schema.account_id}/lists/{subscriber_schema.list_id}/subscribers"
        subscriber_data = {
            "ad_tracking": "ebook",
            'email': subscriber_schema.email,
            'name': subscriber_schema.name,
            'strict_custom_fields': False,
            'tags': [subscriber_schema.tags]
        }
        response = util.rest("POST", url, json.dumps(
            subscriber_data), access_token).text

        return response

    def update_subscriber(self, context, subscriber_entity):
        '''update a subsciber'''

        access_token = util.get_acess_token(context["headers"])
        subscriber_schema = AweberSubscriber(**subscriber_entity)
        url = f"https://api.aweber.com/1.0/accounts/{subscriber_schema.account_id}/lists/{subscriber_schema.list_id}/subscribers/{subscriber_schema.subscriber_id}"
        subscriber_data = {
            "ad_tracking": "ebook",
            'email': subscriber_schema.email,
            'name': subscriber_schema.name,
            'strict_custom_fields': False,
            'tags': [subscriber_schema.tags]
        }
        response = util.rest("PATCH", url, json.dumps(
            subscriber_data), access_token).text

        return response

    def delete_subscriber(self, context, subscriber_entity):
        '''Delete a subscriber'''

        access_token = util.get_acess_token(context["headers"])
        subscriber_schema = AweberSubscriber(**subscriber_entity)
        url = f"https://api.aweber.com/1.0/accounts/{subscriber_schema.account_id}/lists/{subscriber_schema.list_id}/subscribers/{subscriber_schema.subscriber_id}"
        response = util.rest("DELETE", url, {}, access_token).text

        return response

    def create_custom_field(self, context, custom_entity):
        '''add a new custom field'''

        access_token = util.get_acess_token(context["headers"])
        custom_schema = AweberList(**custom_entity)
        custom_data = {
            'name': custom_schema.name,
            'ws.op': 'create',
        }

        url = f'https://api.aweber.com/1.0/accounts/{custom_schema.account_id}/lists/{custom_schema.list_id}/custom_fields'
        response = util.rest("POST", url, json.dumps(
            custom_data), access_token).text

        return response

    def update_custom_field(self, context, custom_entity):
        '''update a custom field'''

        access_token = util.get_acess_token(context["headers"])
        custom_schema = AweberList(**custom_entity)
        custom_data = {
            'name': custom_schema.name,
            'is_subscriber_updateable': True,
        }

        url = f'https://api.aweber.com/1.0/accounts/{custom_schema.account_id}/lists/{custom_schema.list_id}/custom_fields/{custom_schema.custom_fields_id}'
        response = util.rest("PATCH", url, json.dumps(
            custom_data), access_token).text

        return response

    def delete_custom_field(self, context, custom_entity):
        '''Delete a custom field'''

        access_token = util.get_acess_token(context["headers"])
        custom_schema = AweberList(**custom_entity)
        url = f'https://api.aweber.com/1.0/accounts/{custom_schema.account_id}/lists/{custom_schema.list_id}/custom_fields/{custom_schema.custom_fields_id}'
        response = util.rest("DELETE", url, {}, access_token)
        
        return response.status_code
