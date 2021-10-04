from dataclasses import dataclass


@dataclass
class RedboothWorkspace:
    organization_id: str = None
    name: str = None
    tracks_time: str = None
    publish_pages: str = None
    is_public: str = None