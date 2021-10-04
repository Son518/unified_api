from dataclasses import dataclass


@dataclass
class Payment():

    payment_id: str = None
    amount: str = None
    reference: str = None