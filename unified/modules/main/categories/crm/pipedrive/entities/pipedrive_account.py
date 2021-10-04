from crm.entities.account import Account
from dataclasses import dataclass


@dataclass
class PipedriveCRMAccount(Account):

    address: str = None
    visible_to: str =  None
    organization_id: str = None
    label_id: str = None
    