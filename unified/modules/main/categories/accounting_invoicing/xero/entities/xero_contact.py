from dataclasses import dataclass
from accounting_invoicing.entities.contact import Contact


@dataclass
class XeroContact(Contact):

    organization_id: str = None
    account_number: str = None