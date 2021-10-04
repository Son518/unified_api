from dataclasses import dataclass

@dataclass
class StripeRefund:
    id: str = None
    amount: float = None
    currency: str = None
    balance_transaction_id: str = None
    charge_id: str = None
    payment_intent_id: str = None
    reason: str = None
    receipt_number: str = None
    status: str = None
    source_transfer_reversal: str = None,
    transfer_reversal: str = None
