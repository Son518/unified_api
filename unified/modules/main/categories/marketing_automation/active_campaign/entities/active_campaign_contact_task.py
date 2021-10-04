from dataclasses import dataclass

@dataclass
class ActiveCampaignContactTask:
    id: int = None  
    contact_id: int = None  
    task_title: str = None
    due_date: str = None  ## datetime
    task_type: str = None
    first_name: str = None
    last_name: str = None
    phone: str = None
    customer_acct_name: str = None
    orgname: str = None
    task_id: str = None
    task_type_title: str = None
    task_note: str = None