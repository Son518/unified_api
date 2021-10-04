from dataclasses import dataclass

@dataclass
class SquarePayment:
    id: str = None
    source_id: str = None
    status: str = None
    amount: int = None
    currency_code: str = None
    tip_amount: int = None
    tip_currency_code: str = None
    app_fee_amount: int = None
    app_fee_currency_code: str = None
    autocomplete: str = None
    customer_id: str = None
    order_id: str = None
    location_id: str = None
    reference_id: str = None
    idempotency_key: str = None
