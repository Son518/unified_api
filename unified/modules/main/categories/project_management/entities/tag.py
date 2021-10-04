from dataclasses import dataclass, field


@dataclass
class Tag:
    id: str = None
    name: str = None
    notes: str = None
    created_date: str = None