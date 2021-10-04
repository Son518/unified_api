from dataclasses import dataclass


@dataclass
class QuickbooksonlineProductService:
    product_id: str = None
    sku: str = None
    product_type: str = None
    name: str = None
    income_account_type_id: str = None
    expense_account_type_id: str = None
    description_on_sales_forms: str = None
    sales_price: str = None
    description_on_purchase_forms: str = None
    cost: str = None
    category_id: str = None
    is_taxable: bool = False
    unit_price: str = None
