from dataclasses import dataclass
from scheduling_bookings.google_calendar import util


@dataclass
class GoogleCalendarEvent():

    calendar_id: str = None
    event: str = None
    email: str = None
    summary: str = None
    description: str = None
    location: str = None
    start_date_time: str = None
    end_date_time: str = None
    repeat_frequency: str = None
    repeat_until: str = None
    repeat_how_many_times: str = None
    all_day: str = None
    color: str = None
    attendees: str = None
    visibility: str = None
    use_default_reminders: str = None
    reminders: str = None
    minutes_before_remainders: str = None
    show_me_as_free_or_busy: str = None
    guests_can_modify_event: str = None
    notify_attendes: str = None
    calendar: str = None
    use_default_remainders: str = None
    repeat_every_days: str = None
    remainders: str = None
    event_id: str = None
    name: str = None
    add_conferencing: str = None
    repeat_on_these_days_of_the_week: str = None
    repeat_every_week: str = None
    guest_can_modify_event: str  = None
    timezone: str = None

    def __post_init__(self):
        self.start_date_time_epoch()
        self.end_date_time_epoch()

    def start_date_time_epoch(self):
        if not(self.start_date_time is None or "-" in self.start_date_time):
            format = "%Y-%m-%dT%H:%M:%S+00:00"
            self.start_date_time = util.epoch_to_format(
                format, self.start_date_time)

    def end_date_time_epoch(self):
        if not(self.end_date_time is None or "-" in self.end_date_time):
            format = "%Y-%m-%dT%H:%M:%S+00:00"
            self.end_date_time = util.epoch_to_format(
                format, self.end_date_time)