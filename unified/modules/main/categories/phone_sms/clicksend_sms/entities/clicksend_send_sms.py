from dataclasses import dataclass, field

@dataclass
class ClickSend_Send_SMS():

    message: str = None
    schedule: str = None
    contact_list_name: str = None
    sent_from: str = None
