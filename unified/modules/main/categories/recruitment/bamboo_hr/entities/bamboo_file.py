from dataclasses import dataclass, field
from recruitment.bamboo_hr import util

@dataclass
class BambooFile():

    file_name: str = None
    employee_id: str = None
    share_this_file_with_employee: str = None
    category_id: str = None
    file_url: str = None
    file_content: str = None
