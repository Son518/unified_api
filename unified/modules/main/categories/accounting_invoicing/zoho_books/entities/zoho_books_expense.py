from dataclasses import dataclass

@dataclass
class ZohobooksExpense(): 
    account_id: str = None
    date: str = None
    amount: str = None