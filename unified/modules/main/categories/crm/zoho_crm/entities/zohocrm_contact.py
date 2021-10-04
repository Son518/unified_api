from dataclasses import dataclass
from crm.entities.contact import Contact
from crm.zoho_crm import util


@dataclass
class ZohocrmContact(Contact):
    owner_id: str = None
    department: str = None
    lead_source_id: str = None
    mobile: str = None
    date_of_birth: str = None
    title: str = None
    salutation: str = None
    fax: str = None
    home_phone: str = None
    other_phone: str = None
    report_to_id: str = None
    skype_id: str = None
    twitter: str = None
    assistant_name: str = None
    assistant_phone: str = None
    email_opt_out: bool = False

    def __post_init__(self):
        if not (self.date_of_birth is None or "-" in self.date_of_birth):
            format="%Y-%m-%d"
            self.date_of_birth = util.epoch_to_format(format,self.date_of_birth)
