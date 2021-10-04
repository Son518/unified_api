from dataclasses import dataclass, field

@dataclass
class StripeBalanceTransaction:
    id: str = None
    amount: int = 0  ## cents
    currency: str = None
    description: str = None
    fee: str = None
    ## fee_details: dict = field(default_factory=dict)  # Fee details
    net_amount: int = None
    source_id: str = None
    status: str = None
    txn_type: str = None
    created: int = None
    available_on: int = None # datetime / timestamp
