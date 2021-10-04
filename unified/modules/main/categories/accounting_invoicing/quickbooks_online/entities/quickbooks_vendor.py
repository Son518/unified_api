from dataclasses import dataclass


@dataclass
class QuickbooksonlineVendors:
    full_name: str = None
    phone: str = None
    email: str = None
    website: str = None
    address_line1: str = None
    address_line2: str = None
    vendor_id: str = None
    address_city: str = None
    address_state_code: str = None
    address_zip_code: str = None
