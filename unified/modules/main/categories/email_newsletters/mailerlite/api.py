from mailerlite import MailerLiteApi
from requests.models import Response
from werkzeug.wrappers import response
from email_newsletters.mailerlite.entities.mailerlite_subsciber import MalierliteSubscriber
from email_newsletters.mailerlite.entities.mailerlite_campaign import MalierliteCampaign
from email_newsletters.mailerlite.entities.mailerlite_group import MalierliteGroup
from mailerlite.constants import Subscriber, Campaign, Group
import requests
from flask import jsonify
import json


class MailerliteAPI():

    def subscriber_by_email(self, context, params):
        """" Get a subscriber by email"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")     

        api = MailerLiteApi(api_key)        
        response = api.subscribers.get(email=params.get("email"))

        data_obj = response._asdict()
        fields = data_obj.get("fields")
        fields_data = []

        for field in fields:
            fields_obj = field._asdict()
            fields_data.append(fields_obj)
        data_obj["fields"] = fields_data        

        response_obj = MalierliteSubscriber(
            subscriber_id= data_obj["id"],
            name= data_obj["name"],
            email= data_obj["email"],
            fields= data_obj["fields"],
            type = data_obj["type"],
            date_created= data_obj["date_created"],
            date_updated= data_obj["date_updated"]
        )

        return response_obj.__dict__


    def subscriber(self, context, params):
        """ Get a subscriber by Id"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        api = MailerLiteApi(api_key)
        response = api.subscribers.get(id=params.get("id"))
        response = response._asdict()

        data = MalierliteSubscriber(
            subscriber_id = response["id"],
            email = response["email"],
            name = response["name"],
            type = response["type"],
            date_created = response["date_created"]
        )
        return data.__dict__


    def campaigns(self, context, params):
        """ Get list of Campaigns"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        api = MailerLiteApi(api_key)
        response = api.campaigns.all()

        if len(response) == 0:
            return jsonify({"message":"No activities found"})

        data = MalierliteCampaign(
            name= response("name"),
            campaign_id= response["id"],
            subject= response["subject"],
            from_name= response["from_name"],
            from_email= response["from_email"]
        )
        return data.__dict__


    def subscribers(self, context, params):
        """ Get list of Subscribers"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        api = MailerLiteApi(api_key)
        response = api.subscribers.all()

        data = []

        for resp_obj in response:
            data_obj = resp_obj._asdict()
            fields = data_obj.get("fields")
            fields_data = []
            fields_obj = {}
            response_obj = {}

            for field in fields:
                fields_obj = field._asdict()
                fields_data.append(fields_obj)
            data_obj["fields"] = fields_data

            response_obj = MalierliteSubscriber(
                subscriber_id= data_obj["id"],
                name= data_obj["name"],
                email= data_obj["email"],
                fields= data_obj["fields"],
                type = data_obj["type"],
                date_created= data_obj["date_created"],
                date_updated= data_obj["date_updated"]
            )

            data.append(response_obj.__dict__)
        return json.dumps(data)

    def group(self, context, params):

        """ Get Group by Id"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        headers= {
            "X-MailerLite-ApiKey": api_key
        }

        result = requests.request("GET", f"https://api.mailerlite.com/api/v2/groups/{params.get('id')}", headers= headers ).text
        result = json.loads(result)

        if result.get("error"):
            return jsonify({"message": result["error"]["message"]})

        data = MalierliteGroup(
            group_id = result["id"],
            name = result["name"]
        )
        return data.__dict__


    def group_subscriber(self, context, params):
        """ Get Group Subscriber"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        api = MailerLiteApi(api_key)
        response = api.groups.subscriber(group_id=params.get("group_id"), subscriber_id=params.get("subscriber_id"))

        data_obj = response._asdict()
        fields = data_obj.get("fields")
        fields_data = []
        
        for field in fields:
            fields_obj = field._asdict()
            fields_data.append(fields_obj)           
        data_obj["fields"] = fields_data
        
        response_obj = MalierliteSubscriber(
            subscriber_id= data_obj["id"],
            name= data_obj["name"],
            email= data_obj["email"],
            fields= data_obj["fields"],
            type = data_obj["type"],
            date_created= data_obj["date_created"],
            date_updated= data_obj["date_updated"]
        )
        return response_obj.__dict__


    def groups(self, context, params):
        """ Get list of Groups"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        api = MailerLiteApi(api_key)
        response = api.groups.all()
        data = []
        for group in response:
            data_obj = group._asdict()
            result = MalierliteGroup(
                group_id= data_obj["id"],
                group_name= data_obj["name"],
                date_created= data_obj["date_created"],
                date_updated= data_obj["date_updated"]
            )
            data.append(result)
        return jsonify(data)

    def profile(self, context, params):
        """ Get profile details"""

        api_key = context.get('headers').get('api_key')

        if api_key is None:
            raise Exception("Please provide API-Key")

        api = MailerLiteApi(api_key)
        response_data = api.account.info()
        response = response_data
        response = response["account"]
        data = {
            "id": response["id"],
            "name": response["name"],
            "email": response["email"]
        }
        return data

    def verify(self, context, params):
        """Verify the app"""

        return self.profile(context, params) 