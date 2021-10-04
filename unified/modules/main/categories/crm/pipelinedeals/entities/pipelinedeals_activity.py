from dataclasses import dataclass
from crm.pipelinedeals import util
@dataclass
class PipelinedealsActivity:

    person_id: str = None
    category_id: str = None
    deal_id: str = None
    company_id: str = None
    content: str = None