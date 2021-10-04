from crm.entities.deal import Deal
from dataclasses import dataclass
from crm.pipelinedeals import util

@dataclass
class PipelinedealsDeal(Deal):

    deal_id: str = None
    name: str = None
    expected_close_date: str = None
    company_name: str = None
    primary_contact_id: str = None
    status: str = None
    value: str = None
    stage_id: str = None
    source_id: str = None
    product_interest_id: str = None
    account_id: str = None
    trigger: str = None
    company_id: str = None
    probability: str = None
    updated_by_user_id: str = None
    deal_pipeline_id: str = None
    deal_stage_id: str = None

    def __post_init__(self):
        self.expected_close_date_epoch()

    def expected_close_date_epoch(self):
        if not(self.expected_close_date is None or "-" in self.expected_close_date):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.expected_close_date = util.epoch_to_format(format, self.expected_close_date)