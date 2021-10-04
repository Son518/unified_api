from dataclasses import dataclass, field
from crm.entities.contact import Contact
from crm.freshworks import util
from datetime import datetime


@dataclass
class FreshworksContact(Contact):
    
    mobile_number: str = None
    facebook: str = None
    twitter: str = None
    linkedin: str = None
    address: str = None
    created_date: str = None
    updated_date: str = None
    display_name: str = None
    job_title: str = None
    external_id: str = None
    source_name: str = None
    campaign_name: str = None
    recent_note: str = None
    lead_score: str = None
    subscription_status: str = None
    lifecycle_stage: str = None

    def __post_init__(self):
        self.created_date_epoch()
        self.updated_date_epoch()

    def created_date_epoch(self):
        # for api, convert date in app's format to epoch
        if not(self.created_date is None or "-" in self.created_date):
            format = "%Y-%m-%dT%H:%M:%S"
            self.created_date = (
                util.epoch_to_format(format, self.created_date))

    def updated_date_epoch(self):
        # for api, convert date in app's format to epoch
        if not(self.updated_date is None or "-" in self.updated_date):
            format = "%Y-%m-%d"
            self.updated_date = util.epoch_to_format(format, self.updated_date)
