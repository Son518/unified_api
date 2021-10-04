from dataclasses import dataclass


@dataclass
class Segement:
    name: str = None
    criteria: str = None
    list_id: str = None
    segment_id: str = None
