from dataclasses import dataclass
from customer_support.drift import util

@dataclass
class DriftContact():
    
    email_address: str = None
    contact_id: str = None
    account_owner: str = None
    lead_stage: str = None
    cql_score: str = None
    alias: str = None
    city: str = None
    country: str = None
    display_location: str = None
    display_name: str = None
    employment_role: str = None
    employment_seniority: str = None
    employment_title: str = None
    first_name: str = None
    has_consent: bool = True
    last_active: str = None
    last_contacted: str = None
    last_name: str = None
    latitude: str = None
    linkedin_handle: str = None
    longitude: str = None
    name: str = None
    original_utm_campaign: str = None
    original_utm_content: str = None
    original_conversation_started_page_title: str = None
    original_conversation_started_page_url: str = None
    original_entrance_page_title: str = None
    original_entrance_page_url: str = None
    original_utm_medium: str = None
    original_referer_url: str = None
    original_utm_team: str = None
    phone: str = None
    pin_code: str = None
    recent_utm_campaign: str = None
    recent_utm_content: str = None
    recent_conversation_started_page_title: str = None
    recent_entrance_page_title: str = None
    recent_entrance_page_url: str = None
    recent_utm_medium: str = None
    recent_referer_url: str = None
    recent_utm_source: str = None
    recent_utm_team: str = None
    start_date: str = None
    state: str = None
    time_zone:  str = None
    custom_attributes: str = None
    user_id: str = None

    def __post_init__(self):
        self.start_date = self.date_epoch(self.start_date, "%Y-%m-%dT%H:%M:%SZ")
        self.last_active = self.date_epoch(self.last_active, "%Y-%m-%dT%H:%M:%SZ")
        self.last_contacted = self.date_epoch(self.last_contacted, "%Y-%m-%dT%H:%M:%SZ")

    def date_epoch(self, field_name, date_time_format):
        if not(field_name is None or "-" in field_name):
            format = date_time_format
            field_name = util.epoch_to_format(format, field_name)
            return field_name