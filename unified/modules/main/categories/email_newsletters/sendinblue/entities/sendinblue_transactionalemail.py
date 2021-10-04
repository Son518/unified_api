from dataclasses import dataclass
from email_newsletters.entities.transactional_email import Transactionalemail


@dataclass
class SendinblueTransactionalemail(Transactionalemail):
    email:str=None
    name:str=None
