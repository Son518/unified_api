from dataclasses import dataclass
from crm.entities.deal import Deal


@dataclass
class SalesforceOpportunity(Deal):

    opportunity_id: str = None
    private: str = None
    amount: str = None
    opportunity_name: str = None
    end_date: str = None
    type: str = None
    lead_source: str = None
    next_step: str = None
    stage: str = None
    primary_campaign_score: str = None
    order_number: str = None
    current_generator: str = None
    tracking_number: str = None
    main_competitor: str = None
    delivery_status: str = None
