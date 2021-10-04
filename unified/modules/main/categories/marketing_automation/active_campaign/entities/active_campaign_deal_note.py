from dataclasses import dataclass

@dataclass
class ActiveCampaignDealNote:
    id: int = None
    deal_id: int = None
    note: str = None  