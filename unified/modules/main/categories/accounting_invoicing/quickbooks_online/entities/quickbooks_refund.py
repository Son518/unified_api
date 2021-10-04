from dataclasses import dataclass


@dataclass
class QuickbooksonlineRefund:
    customer_id: str = None
    refund_receipt_date: str = None
    refund_receipt_number:str=None
    payment_method:str=None
    refund_from:str=None
    product_id:str=None
    product_amount:str=None
    product_description:str=None
    message_displayed_on_refund_receipt:str=None
    memo:str=None
    product_tax:str=None
