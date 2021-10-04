from dataclasses import dataclass, field
from crm.entities.contact import Contact
from datetime import datetime, timezone
from crm.insightly import util


@dataclass
class InsightlyContact(Contact):

    organization_id: str = None
    phone: str = None
    phone_mobile: str = None
    date_of_birth: str = None
    title: str = None
    prefix: str = None
    fax: str = None
    phone_home: str = None
    phone_other: str = None
    twitter: str = None
    assistant_name: str = None
    assistant_phone: str = None
    email_opted_out: str = None
    facebook: str = None
    linkedin: str = None
    tags: str = None
    contact_owner_id: str = None
    mailing_postal_code: str = None
    due_date: str = None
    other_city: str = None
    visible_to: str = None
    other_country: str = None
    other_postal_code: str = None
    other_city: str = None
    other_state: str = None
    other_street: str = None
    image_url: str = None
    visible_to: str = None
    date_created: str = None
    date_updated: str = None
    last_activity: str = None
    next_activity: str = None
    created_user_id: str = None
    organization_id: str = None
    customfields: str = None
    links: str = None


    note_id: str = None
    note_title: str = None
    date_created: str = None
    date_updated: str = None
    body: str = None

    def __post_init__(self):
        self.date_created_epoch()
        self.date_updated_epoch()
        self.due_date_epoch()

    def date_created_epoch(self):
        if not(self.date_created is None or "-" in self.date_created):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.date_created = util.epoch_to_format(format, self.date_created)
    def date_updated_epoch(self):
        if not(self.date_updated is None or "-" in self.date_updated):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.date_updated = util.epoch_to_format(format, self.date_updated)

    def due_date_epoch(self):
        if not(self.due_date is None or "-" in self.due_date):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.due_date = util.epoch_to_format(format, self.due_date)
