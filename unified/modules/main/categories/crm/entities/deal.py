from dataclasses import dataclass


@dataclass
class Deal:

    deal_id: str = None
    account_id: str = None
    name: str = None
    close_date: str = None
    description: str = None
    stage_id: str = None
    value: str = None
    probability: str = None
    owner_id : str = None
    contact_id: str = None
    currency_id: str = None