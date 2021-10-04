from dataclasses import dataclass

@dataclass
class KeapEmail():

    contacts_id: str = None
    subject: str = None
    text_body: str = None
    html_body: str = None
    user_id: str = None
    file_name: str = None
    file_data: str = None
