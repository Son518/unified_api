from dataclasses import dataclass
from project_management.entities.task import Task



@dataclass
class PaymoClient():

    name:str = None
    email:str = None
    address:str = None
    city:str = None
    state:str = None
    postal_code:str = None
    country:str = None
    phone:str = None
    fax:str = None
    website_url:str = None
    fiscal_information:str = None
    id:str =None 
    due_interval:str = None
    image:str = None
    active:str = None
    created_on:str = None
    updated_on:str = None
    additional_privileges:str = None

