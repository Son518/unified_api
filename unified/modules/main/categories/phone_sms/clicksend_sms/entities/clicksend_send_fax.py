from dataclasses import dataclass, field

@dataclass
class ClickSend_Send_Fax():

    to: str = None
    sent_from: str = None
    pdf_file_url: str = None
