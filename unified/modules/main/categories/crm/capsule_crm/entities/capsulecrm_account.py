from dataclasses import dataclass
from crm.entities.account import Account

@dataclass
class CapsulecrmAccount(Account):
    email: str = None
    tags: str = None
