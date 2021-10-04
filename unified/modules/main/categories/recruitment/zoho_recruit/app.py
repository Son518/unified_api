import json
from recruitment.zoho_recruit.actions import ZohorecruitActions
from recruitment.zoho_recruit.api import ZohorecruitApi
from recruitment.zoho_recruit.triggers import ZohorecruitTriggers
from unified.core.app import App, AuthInfo

class ZohorecruitApp(App,ZohorecruitActions,ZohorecruitApi,ZohorecruitTriggers):

    def __init__(self):
        super().__init__(
            name="Zohorecruit",
            description="Zoho Recruit is a cloud based applicant tracking system that's built to provide diverse, end-to-end hiring solutions for staffing agencies, corporate HRs and temporary workforce.",
            category="recruitment",
            logo="https://logo.500apps.com/Zohorecruit",
            auth_info=None,
            auth_type='oauth2')