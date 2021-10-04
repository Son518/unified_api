from dataclasses import dataclass, field
from recruitment.bamboo_hr import util

@dataclass
class BambooTimeOffSummary():

    summary_id: str = None
    type: str = None
    employee_id: str = None
    start_date: str = None
    end_date: str = None
    employee_name: str = None
