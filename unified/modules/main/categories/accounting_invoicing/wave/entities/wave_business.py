from dataclasses import dataclass, field
from accounting_invoicing.wave import util


@dataclass
class WaveBusiness():

    name: str = None
    business_id: str = None
    taxes: str = None
