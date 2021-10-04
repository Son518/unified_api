from dataclasses import dataclass
from marketing_automation.active_campaign import util

@dataclass
class ActiveCampaignDeal:
    deal_id: int = None
    title: str = None
    value: str = None  
    owner_id: int = None  
    currency: str = None
    stage: str = None
    contact_id: int = None  
    pipeline_id: int = None ## group
    account_id: int = None  
    contact_email_address: str = None
    contact_deal_role: str = None ## id or value?
    forecasted_close_date: str = None ## timestamp, or datetime?
    pipeline_title: str = None


    def __post_init__(self):
        self.forecasted_close_date_epoch()

    def forecasted_close_date_epoch(self):
        if self.forecasted_close_date is None or "-" in self.forecasted_close_date:
            self.forecasted_close_date = self.forecasted_close_date
        else:
            format = "%Y-%m-%d"
            self.forecasted_close_date = util.epoch_to_format(
                format, self.forecasted_close_date)
