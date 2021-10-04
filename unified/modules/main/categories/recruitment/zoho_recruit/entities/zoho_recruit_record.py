from dataclasses import dataclass
from recruitment.zoho_recruit import util
from core.util import convert_epoch
from core.util import dateformat_to_epoch

@dataclass
class ZohorecruitRecord():

    module: str = None
    layout_id: str = None
    trigger: str = None
    origin: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    mobile: str = None
    phone: str = None
    fax: str = None
    website: str = None
    associated_tags: str = None
    career_page_invite_stage: str = None
    secondary_email: str = None
    street: str = None
    city: str = None
    state: str = None
    pin_code: str = None
    experience_in_years: str = None
    highest_qualification_held: str = None
    current_job_title: str = None
    current_employer: str = None
    expected_salary: str = None
    current_salary: str = None
    skill_set: str = None
    additional_info: str = None
    skype_id: str = None
    twitter: str = None
    salutation: str = None
    associated_any_social_profiles: bool = True
    last_emailed: str = None
    candidate_status: str = None
    source: str = None
    candidate_owner: str = None
    rating: str = None
    email_opt_out: bool = True
    is_locked: bool = True
    is_unqualified: bool = False
    is_attachment_present: bool = True
    institute: str = None
    department: str = None
    degree: str = None
    duration_from: str = None
    duration_to: str = None
    currently_pursuing: bool = False
    occupation: str = None
    company: str = None
    summary: str = None
    work_duration_from: str = None
    work_duration_to: str = None
    i_currently_work_here: bool = True
    record_id: str = None
    layout: str = None
    status: str = None
    comments: str = None
    id: str = None

    def __post_init__(self):
        self.duration_from = dateformat_to_epoch(self.duration_from) if self.duration_from is not None and "-" in self.duration_from else convert_epoch(self.duration_from, "%Y-%m-%d")
        self.duration_to = dateformat_to_epoch(self.duration_to) if self.duration_to is not None and "-" in self.duration_to else convert_epoch(self.duration_to, "%Y-%m-%d")
        self.work_duration_from = dateformat_to_epoch(self.work_duration_from) if self.work_duration_from is not None and "-" in self.work_duration_from else convert_epoch(self.work_duration_from, "%Y-%m-%d")
        self.work_duration_to = dateformat_to_epoch(self.work_duration_to) if self.work_duration_to is not None and "-" in self.work_duration_to else convert_epoch(self.work_duration_to, "%Y-%m-%d")