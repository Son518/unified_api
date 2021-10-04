from dataclasses import dataclass, field
from accounting_invoicing.wave import util


@dataclass
class WaveAccount():

    name: str = None
    account_id: str = None
    type: str = None
