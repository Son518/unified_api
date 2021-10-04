from dataclasses import dataclass

@dataclass
class GoogleCalendarQuickAddEvent():

    calendar_id: str = None
    describe_event: str = None
    calendar: str = None
    attendees: str = None
    timezone: str = None