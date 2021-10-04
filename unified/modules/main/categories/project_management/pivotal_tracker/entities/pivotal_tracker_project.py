from dataclasses import dataclass
from project_management.pivotal_tracker import util

@dataclass
class PivotaltrackerProject:

    project_name: str = None