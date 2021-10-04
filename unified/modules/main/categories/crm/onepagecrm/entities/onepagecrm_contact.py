from dataclasses import dataclass
from crm.entities.contact import Contact
from crm.onepagecrm import util


@dataclass
class OnepagecrmContact(Contact):

    action_id: str = None
    created_date: str = None
    updated_date: str = None
    company: str = None
    job_title: str = None
    phone_work: str = None
    phone_mobile: str = None
    website: str = None
    tags: str = None
    text: str = None
    note_id: str = None
    company_id: str = None
    company_size: str = None
    status: str = None
    done: str = None
    address: str = None
    city: str = None
    state: str = None
    zip: str = None
    country: str = None
    lead_source: str = None
    background: str = None
    next_action: str = None
    next_action_date: str = None
    mark_as_starred: str = None
    email_work: str = None
    email_home: str = None

    def __post_init__(self):
        self.created_date_epoch()
        self.updated_date_epoch()

    def created_date_epoch(self):
        if not(self.created_date is None or "-" in self.created_date):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.created_date = util.epoch_to_format(format, self.created_date)

    def updated_date_epoch(self):
        if not(self.updated_date is None or "-"  in self.updated_date):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.updated_date = util.epoch_to_format(format, self.updated_date)
