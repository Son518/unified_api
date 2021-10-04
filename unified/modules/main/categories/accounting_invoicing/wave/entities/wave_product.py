from dataclasses import dataclass, field
from accounting_invoicing.wave import util


@dataclass
class WaveProduct():

    business_id: str = None
    name: str = None
    description: str = None
    price: str = None
    income_account: str = None
    expence_account: str = None
