from unified.core.app import App
from marketing_automation.active_campaign.actions import ActiveCampaignActions
from marketing_automation.active_campaign.api import ActiveCampaignApi
from marketing_automation.active_campaign.triggers import ActiveCampaignTriggers


class ActivecampaignApp(App, ActiveCampaignActions, ActiveCampaignTriggers, ActiveCampaignApi):

    def __init__(self):
        super().__init__(
            name="ActiveCampaign",
            description="ActiveCampaign gives the email marketing, marketing automation, and CRM tools you need to create incredible customer experiences.",
            category="Marketing Automation",  # is this field really required???
            logo="https://logo.500apps.com/active_campaign",
            auth_info=None,
            auth_type='basic'
        )