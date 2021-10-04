from marketing_automation.entities.contact import Contact
from dataclasses import dataclass
from marketing_automation import util


@dataclass
class OntraportContact(Contact):

    address: str = None
    city: str = None
    state: str = None
    zip_code: str = None
    address2: str = None
    country: str = None
    office_phone: str = None
    sms_number: str = None
    birthday: str = None
    title: str = None
    fax: str = None
    website: str = None
    company: str = None
    first_campaign: str = None
    first_content: str = None
    first_lead_source: str = None
    first_medium: str = None
    first_term: str = None
    last_campaign: str = None
    last_content: str = None
    last_lead_source: str = None
    last_medium: str = None
    last_term: str = None
    facebook_link: str = None
    instagram_link: str = None
    twitter_link: str = None
    linkedin_link: str = None
    profile_image: str = None
    sequence: str = None
    tag: str = None
    date: str = None
    unique_id: str = None
    owner: str = None
    contact_cat: str = None


    def __post_init__(self):
        self.date_epoch()


    def date_epoch(self):
        if self.date is None or "-" in self.date:
            self.date = self.date
        else:
            format = "%Y-%m-%d"
            self.date = util.epoch_to_format(
                format, self.date).replace("-", "")
