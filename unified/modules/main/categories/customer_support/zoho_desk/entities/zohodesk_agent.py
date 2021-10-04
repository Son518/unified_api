from dataclasses import dataclass


@dataclass
class ZohodeskAgent:

    id: str = None
    lastName: str = None
    mobile: str = None
    emailId: str = None
    firstName: str = None
    photoURL: str = None
    phone: str = None
    channelExpert: list = None
    name: str = None
    aboutInfo: str = None
    status: str = None
