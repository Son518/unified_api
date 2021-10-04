from dataclasses import dataclass, field

@dataclass
class ClickSend_Letter():

    pdf_file_url: str = None
    priority: str = None
    template_used: str = None
    colour: str = None
    duplex: str = None
    address_name: str = None
    line_1: str = None
    city: str = None
    state: str = None
    postal_code: str = None
    country: str = None
    return_address: str = None
