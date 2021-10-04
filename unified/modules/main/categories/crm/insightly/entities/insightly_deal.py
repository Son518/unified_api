from dataclasses import dataclass, field
from crm.entities.deal import Deal
from datetime import datetime, timezone
from crm.insightly import util

# Insightly application Specific Deal entites

@dataclass
class InsightlyDeal(Deal):
    organization_id: str = None
    opportunity_name: str = None
    bid_amount: str = None
    cuurent_state_id: str = None
    tags: str = None
    bid_duration: str = None
    bid_type: str = None
    bid_category: str = None
    forecast_close_date: str = None
    bid_currency: str = None
    probability_of_winning: str = None
    opportunity_owner_id: str = None
    opportunity_id: str = None
    current_state: str = None
    actual_close_date: str = None
    category: str = None
    visible_to: str = None
    user_responsible_id: str = None
    image: str = None
    date_created: str = None
    date_updated: str = None
    opportunity_value: str = None
    visible_team_id: str = None
    last_activity: str = None
    next_activity: str = None
    pipeline: str = None
    stage: str = None
    created_user_id: str = None
    customfields: str = None
    links: str = None
    def __post_init__(self):
        self.actual_close_date_epoch()


    def actual_close_date_epoch(self):
        if not(self.actual_close_date is None or "-" in self.actual_close_date):
            format = "%Y-%m-%dT%H:%M:%SZ"
            self.actual_close_date = util.epoch_to_format(format, self.actual_close_date)
