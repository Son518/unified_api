import json
from video_conferencing.clickmeeting.actions import ClickmeetingActions
from unified.core.app import App, AuthInfo

class ClickmeetingApp(App,ClickmeetingActions):

    def __init__(self):
        super().__init__(
            name="Clickmeeting",
            description="ClickMeeting is a browser-based webinar solution, brings the power of webinars to organizations of any size, from one-person firms to multinational enterprises.",
            category="video_conferencing",
            logo="https://logo.500apps.com/clickmeeting",
            auth_info=None,
            auth_type='Basic')