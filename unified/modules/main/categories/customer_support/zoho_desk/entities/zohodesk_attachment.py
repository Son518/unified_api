from dataclasses import dataclass


@dataclass
class ZohodeskAttachment:

    id: str = None
    size: str = None
    isTrashed: bool = None
    name: str = None
    isPublic: bool = None
    href: str = None
    ticketId: str = None
