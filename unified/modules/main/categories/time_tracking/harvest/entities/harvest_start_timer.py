from dataclasses import dataclass

@dataclass
class HarvestStartTime:
    project: str = None
    task: str = None
    notes: str = None