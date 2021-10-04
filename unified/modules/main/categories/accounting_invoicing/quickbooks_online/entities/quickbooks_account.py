from dataclasses import dataclass


@dataclass
class QuickbooksonlineAccount:
    name: str = None
    full_qualified_name: str = None
    account_type: str = None
    account_sub_type: str = None
    current_balance: str = None
    current_balance_with_sub_accounts: str = None
    currency: str = None
    account_id: str = None
    is_active: str = None
