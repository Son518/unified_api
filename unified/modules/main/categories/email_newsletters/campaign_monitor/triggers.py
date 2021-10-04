from unified.core.triggers import Triggers
from email_newsletters.campaign_monitor.entities.campaignmonitor_subscriber import CampaingnmonitorSubcriber


class CampaignmonitorTriggers(Triggers):

    def new_subscriber(self, context, payload):
        """New subscriber event"""
        
        subscriber = CampaingnmonitorSubcriber(
            list_id=payload['ListID'],
            email=payload['Events'][0]['EmailAddress'],
            name=payload['Events'][0]['Name'],
            date=payload["Events"][0]['Date'],
            event_type=payload["Events"][0]['Type'],
            state=payload["Events"][0]['State']
        )

        return subscriber.__dict__
        

    def new_unsubscribe(self, context, payload):
        """New unsubscribe event."""

        subscriber = CampaingnmonitorSubcriber(
            list_id=payload['ListID'],
            email=payload['Events'][0]['EmailAddress'],
            name=payload['Events'][0]['Name'],
            date=payload["Events"][0]['Date'],
            event_type=payload["Events"][0]['Type'],
            state=payload["Events"][0]['State']
        )

        return subscriber.__dict__
