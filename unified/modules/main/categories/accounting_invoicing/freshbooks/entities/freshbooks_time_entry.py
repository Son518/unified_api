from dataclasses import dataclass

@dataclass
class FreshbooksTimeentry():

    account_id: str = None
    user_id: str = None
    object_id: str = None
    name: str = None
    business_id: str = None
    project_id: str = None
    service_id: str = None
    task_id: str = None
    started_at: str = None
    created_at: str = None
    duration: str = None
    is_logged: bool = True
    customerid: str = None    
    billed: bool = True
    billable: bool = True
    internal: bool = True
    active: bool = True
    pending_client: str = None
    pending_project: str = None
    pending_task:str = None
    note: str = None