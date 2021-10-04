from dataclasses import dataclass


@dataclass
class CanceledBookingRecheduled():
								
    booking_id: str = None
    creation_time: str = None
    event_type: str = None
    event_description: str = None
    subject: str = None
    status: str = None
    creation_time: str = None
    starting_time: str = None
    owner: str = None
    duration_minutes: str = None
    virtual_or_physical_location: str = None
    guests: str = None
    booking_link: str = None
    time_zone_description: str = None
    cancel_reschedule_link: str = None
    cancel_reschedule_reason: str = None
    canceled_rescheduled_user: str = None
    canceled_rescheduled_customer: str = None