from crm.entities.deal import Deal
from dataclasses import dataclass
from crm.copper_crm import util


@dataclass
class CoppercrmDeal(Deal):
    assignee: str = None
    status: str = None
    pipeline: str = None
    monetary_value: str = None
    priority: str = None
    win_probability: str = None
    source: str = None
    tags: str = None
    match_by_type: str = None
    match_by_value: str = None
    primary_contact: str = None
    pipe_line: str = None
    replace_or_append_tags: str = None
    subscription_id: str = None
    event: str = None
    type: str = None
    updated_attributes: str = None
    last_stage_at: str = None
    days_in_stage: str = None
    stage: str = None
    ids: str = None
    

    def __post_init__(self):
        if not(self.close_date is None or "-" in self.close_date):
            format = "%m/%d/%Y"
            self.close_date = util.epoch_to_format(format, self.close_date)