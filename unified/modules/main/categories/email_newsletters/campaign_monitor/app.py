# AsanaApp - extends App, AsanaTriggers, AsanaActions, AsanaAPI, ..

# from . import module
import json

from email_newsletters.campaign_monitor.actions import CampaignmonitorActions
from email_newsletters.campaign_monitor.triggers import CampaignmonitorTriggers
from email_newsletters.campaign_monitor.api import CampaignmonitorApi

from unified.core.app import App, AuthInfo


class CampaignmonitorApp(App, CampaignmonitorActions, CampaignmonitorApi, CampaignmonitorTriggers):

    def __init__(self):
        super().__init__(
            name="Campaign Monitor",
            description="Campaign Monitor is an email marketing tool built for designers. Campaign Monitor makes it easy to send beautiful emails, manage lists and subscribers, and track the results of your campaigns",
            category="Email Newsletter",
            logo="https://logo.500apps.com/campaign monitor",
            auth_info=None,
            auth_type='oauth2')
