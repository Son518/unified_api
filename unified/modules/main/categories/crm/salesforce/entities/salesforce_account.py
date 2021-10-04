from dataclasses import dataclass
from crm.entities.account import Account


@dataclass
class SalesforceAccount(Account):

    account_name: str = None
    parent_id: str = None
    account_number: str = None
    account_site: str = None
    type: str = None
    industry: str = None
    annual_revenue: str = None
    rating: str = None
    business_phone: str = None
    fax: str = None
    ticker_symbol: str = None
    ownership: str = None
    employees: str = None
    sic_code: str = None
    billing_street: str = None
    billing_city: str = None
    billing_zip: str = None
    billing_state: str = None
    billing_country: str = None
    shipping_street: str = None
    shipping_city: str = None
    shipping_zip: str = None
    shipping_state: str = None
    shipping_country: str = None
    customer_priority: str = None
    end_date: str = None
    number_of_locations: str = None
    active: str = None
    sla: str = None
    sla_serial_number: str = None
    upsell_opportunity: str = None
