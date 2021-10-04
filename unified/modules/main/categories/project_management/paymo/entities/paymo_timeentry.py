from dataclasses import dataclass, field
from project_management.entities.task import Task



@dataclass
class PaymoTimeEntry():

    project_id:str = None
    task_list_id:str = None
    task_id:str = None
    start_time:str = None
    end_time:str = None   
    description:str = None
    added_manually:str=None
    invoice_item_id:str=None
    billed:str=None
    is_bulk:str=None
    user_id:str=None
    id:str=None
    created_on:str=None
    updated_on:str=None
    duration:str=None
    date:str=None
    
    

