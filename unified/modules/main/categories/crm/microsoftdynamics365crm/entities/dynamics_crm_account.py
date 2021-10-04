from dataclasses import dataclass
from crm.entities.account import Account


@dataclass
class Microsoftdynamics365crmAccount(Account):

    fax: str = None
    relationship_type: str = None
    product_price_list: str = None
    street_1: str = None
    street_2: str = None
    street_3: str = None
    ownership: str = None
    city: str = None
    state: str = None
    zip: str = None
    country: str = None
