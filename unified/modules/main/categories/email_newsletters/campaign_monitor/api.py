from createsend import *
from email_newsletters.campaign_monitor.entities.campaignmonitor_subscriber import CampaingnmonitorSubcriber


class CampaignmonitorApi():

    def subscriber_by_email(self, context, params):
        '''get subscriber by email '''

        campaign_client = Subscriber(
            {'api_key': f'{context["headers"]["api_key"]}'})
        subscriber = campaign_client.get(
            params['list_id'], params['email'])
        subscriber_obj = CampaingnmonitorSubcriber(
            email=subscriber.EmailAddress,
            date=subscriber.Date,
            custom_fields=subscriber.CustomFields,
            state=subscriber.State
        )

        return subscriber_obj.__dict__
    
    def profile(self, context, params):
        """
        get call to show authenticated user information
        """
        campaign_client = CreateSend(
            {'api_key': f'{context["headers"]["api_key"]}'})
        response = campaign_client.administrators()
        profile = {
            'name':response[0].Name,
            'email':response[0].EmailAddress
        }  
        return profile

    def verify(self,context,params):
        """
        get call to verify user authenticated information
        """
        campaign_client = CreateSend({'api_key': f'{context["headers"]["api_key"]}'})
        response = campaign_client.clients()
        result = {
            'client_id':response[0].ClientID,
            'name':response[0].Name
        }
        return result