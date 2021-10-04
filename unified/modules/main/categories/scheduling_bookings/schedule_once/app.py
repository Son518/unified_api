# from . import module
import json
from scheduling_bookings.schedule_once.triggers import ScheduleOnce_Triggers
from scheduling_bookings.schedule_once.api import ScheduleOnce_Api
from unified.core.app import App, AuthInfo


class ScheduleonceApp(App, ScheduleOnce_Triggers, ScheduleOnce_Api):

    def __init__(self):
        super().__init__(
            name="ScheduleOnce",
            description="ScheduleOnce offers contact management, marketing automation, telephony, analytics, web engagement, real-time alerts and social suite. Track, nurture, and sell like a pro.",
            category="Scheduling Bookings",
            logo="https://logo.500apps.com/scheduleOnce",
            auth_info=None,
            auth_type='oauth2')
