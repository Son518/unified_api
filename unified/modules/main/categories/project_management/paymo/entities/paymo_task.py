from dataclasses import dataclass
from project_management.entities.task import Task
from core.util import convert_epoch


@dataclass
class PaymoTask():

    project_id:str = None
    task_list_id:str = None
    name:str = None
    description:str = None
    priority_id:str = None   
    start_date:str = None
    due_date:str = None
    billable:str = None
    budget_hours:str = None
    price_per_hour:str = None
    assigned_users:str = None
    id:str=None
    code:str=None
    user_id:str=None
    complete:str=None
    completed_on:str=None
    completed_by:str=None
    cover_file_id:str=None
    status_id:str=None
    flat_billing:str=None
    seq:str=None
    estimated_price:str=None
    price:str=None
    invoiced:str=None
    invoice_item_id:str=None
    users:str=None
    created_on:str=None
    updated_on:str=None
    priority:str=None
    recurring_profile_id:str=None
    progress_status:str=None
    billing_type:str=None 
	
    
    def __post_init__(self):
        self.start_date = convert_epoch(self.start_date,"%Y-%m-%d")
        self.due_date = convert_epoch(self.due_date,"%Y-%m-%d")
