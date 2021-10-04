from dataclasses import dataclass
from project_management.entities.task import Task



@dataclass
class PaymoExpense():

    client_id:str = None
    name:str = None
    amount:str = None
    currency:str = None
    date:str = None
    notes:str = None
    
