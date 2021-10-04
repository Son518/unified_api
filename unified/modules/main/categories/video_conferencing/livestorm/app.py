import json
from video_conferencing.livestorm.actions import LivestormActions
from video_conferencing.livestorm.api import LivestormApi
from video_conferencing.livestorm.triggers import LivestormTriggers
from unified.core.app import App, AuthInfo

class LivestormApp(App,LivestormActions,LivestormApi,LivestormTriggers):

    def __init__(self):
        super().__init__(
            name="Livestorm",
            description="Livestorm is the end-to-end video engagement platform enabling organizations to create on-demand, live, or pre-recorded events at scale—from your browser.",
            category="video_conferencing",
            logo="https://logo.500apps.com/livestorm",
            auth_info=None,
            auth_type='Basic')