from dataclasses import dataclass
from unified.core.util import epoch_to_format


@dataclass
class HubspotTicket:
    ticket_id: str = None
    name: str = None
    pipeline: int = 0
    ticket_status: str = None
    ticket_description: str = None
    source: str = None
    owner_id: str = None
    priority: str = None
    create_date: str = None
    company_id: str = None
    contact_id: str = None

    def __post__init(self):
        self.create_date = epoch_to_format("%Y-%m-%d", self.create_date) if not(
            self.create_date is None or "-" in self.create_date) else None
