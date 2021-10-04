from dataclasses import dataclass
from email_newsletters.entities.transactional_email import Transactionalemail


@dataclass
class MailjetTransactionalemail(Transactionalemail):
    from_name: str = None
    from_address: str = None
    from_number: str = None
    to_number: str = None
    text: str = None
    template: str = None
    template_language: str = None
    template_variables: str = None
    error_reporting_email: str = None
    campaign: str = None
