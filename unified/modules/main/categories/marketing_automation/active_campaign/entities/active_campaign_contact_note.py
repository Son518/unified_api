from dataclasses import dataclass

@dataclass
class ActiveCampaignContactNote:
    contact_id: str = None  ## int or str?
    list_id: str = None  ## int, float or str?
    note: str = None  ## ??