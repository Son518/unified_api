from dataclasses import dataclass
from crm.entities.account import Account

@dataclass
class ZohocrmAccount(Account):
    owner_id:str=None
    billing_city:str=None
    billing_street:str=None
    billing_state:str=None
    billing_zip:str=None
    billing_country:str=None
    fax:str=None
    parent_account_id:str=None,
    rating_id:str=None
    industry_id:str=None
    account_site:str=None
    account_number:str=None