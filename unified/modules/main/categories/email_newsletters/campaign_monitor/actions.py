from createsend import *
import json
from unified.core.actions import Actions
from email_newsletters.campaign_monitor import util
from email_newsletters.campaign_monitor.entities.campaignmonitor_subscriber import CampaingnmonitorSubcriber


class CampaignmonitorActions(Actions):

    def create_subscriber(self, context, subscriber_entities):
        """Create a new subscriber"""

        api_key = context['headers']['api_key']
        campaign_client = Subscriber({'api_key': f"{api_key}"})
        subscriber_schema = CampaingnmonitorSubcriber(**subscriber_entities)
        response = campaign_client.add(subscriber_schema.list_id, subscriber_schema.email,
                                       subscriber_schema.name, custom_fields=[], resubscribe=subscriber_schema.resubscribe, consent_to_track='no',
                                       restart_subscription_based_autoresponders=subscriber_schema.restart_autoresponders)
        # getting response in string
        return {"response": response}

    def add_subscriber(self, context, subscriber_entities):
        """Add a new subscriber"""

        return self.create_subscriber(context, subscriber_entities)

    def update_subscriber(self, context, subscriber_entities):
        """Update an existing subscriber"""

        access_token = util.get_basic_token(context['headers'])
        subscriber_schema = CampaingnmonitorSubcriber(**subscriber_entities)
        url = f"https://api.createsend.com/api/v3.2/subscribers/{subscriber_schema.list_id}.json?email={subscriber_schema.email}"

        body = {
            "EmailAddress": subscriber_schema.new_email,
            "Name": subscriber_schema.name,
            "CustomFields": [],
            "Resubscribe": subscriber_schema.resubscribe,
            "RestartSubscriptionBasedAutoresponders": subscriber_schema.restart_autoresponders,
            "ConsentToTrack": "Yes"
        }
        response = util.rest('PUT', url, json.dumps(body), access_token).text

        return response

    def unsubscribe(self, context, subscriber_entities):
        """Unsubscribe an existing subscriber"""

        access_token = util.get_basic_token(context['headers'])
        subscriber_schema = CampaingnmonitorSubcriber(**subscriber_entities)
        url = f"https://api.createsend.com/api/v3.2/subscribers/{subscriber_schema.list_id}/unsubscribe.json"

        body = {
            "EmailAddress": subscriber_schema.email
        }

        response = util.rest('POST', url, json.dumps(body), access_token).text
        return response

    def unsubscribe_email(self, context, subscriber_entities):
        """Unsubscribe an existing subscriber"""

        return self.unsubscribe(context, subscriber_entities)
