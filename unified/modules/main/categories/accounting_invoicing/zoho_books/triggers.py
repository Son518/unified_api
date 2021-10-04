from unified.core.triggers import Triggers
from accounting_invoicing.zoho_books.entities.zoho_books_customer import  ZohobooksCustomer
from accounting_invoicing.zoho_books.entities.zoho_books_item import ZohobooksItem
from accounting_invoicing.zoho_books.entities.zoho_books_sales_invoice import ZohobooksSalesinvoice
from accounting_invoicing.zoho_books.entities.zoho_books_estimate import ZohobooksEstimate
from accounting_invoicing.zoho_books.entities.zoho_books_expense import ZohobooksExpense
import json


class ZohobooksTriggers(Triggers):

    def new_customer(self, context, payload):
        ''' triggers when new customer created'''
        customer=payload["JSONString"]["contact"]
        customer_obj = ZohobooksCustomer(
                                    contact_name = customer["contact_name"],
                                    company_name = customer["company_name"],
                                    website = customer["website"],
                                    payment_terms= customer["payment_terms"],
                                    notes= customer["notes"],
                                    billing_address=customer["billing_address"],
                                    billing_address_city= customer["billing_address"]["city"],
                                    billing_address_state= customer["billing_address"]["state"],
                                    billing_address_zip= customer["billing_address"]["zip"],
                                    billing_address_country= customer["billing_address"]["country"],
                                    billing_address_fax= customer["billing_address"]["fax"],               
                                    shipping_address=customer["shipping_address"],
                                    shipping_address_city= customer["shipping_address"]["city"],
                                    shipping_address_state= customer["shipping_address"]["state"],
                                    shipping_address_zip= customer["shipping_address"]["zip"],
                                    shipping_address_country= customer["shipping_address"]["country"],
                                    shipping_address_fax= customer["shipping_address"]["fax"],
                                    first_name=customer["first_name"],
                                    last_name= customer["last_name"],
                                    email= customer["email"],
                                    phone= customer["phone"],
                                    mobile= customer["mobile"]
                                    )
        return customer_obj.__dict__
    

    def new_estimate(self, context, payload):
        ''' triggers when new estimate created'''
        estimate=payload["JSONString"]["estimate"]
        data=estimate["line_items"][0]
        estimate_obj = ZohobooksEstimate(
                                        customer_id= estimate["customer_id"],
                                        start_date= estimate["date"],
                                        end_date= estimate["expiry_date"],
                                        exchange_rate= estimate["exchange_rate"],
                                        discount= data["discount"],
                                        item_id= data["item_id"],
                                        rate= data["rate"],
                                        quantity= data["quantity"],
                                        estimate_notes= estimate["notes"],
                                        estimate_terms= estimate["terms"]
                                        )
        return estimate_obj.__dict__


    def new_item(self, context, payload):
        ''' triggers when new item created'''
        item=payload["JSONString"]["item"]
        item_obj = ZohobooksItem(
                                 item_name= item["name"],
                                 description= item["description"],
                                 rate= item["rate"],
                                 tax_percentage= item["tax_percentage"]
                                )
        return item_obj.__dict__


    def new_sales_invoice(self, context, payload):
        ''' triggers when new invoice created'''
        print(payload.keys())
        invoice=payload['JSONString']["invoice"]
        data=invoice["line_items"][0]
        
        invoice_obj = ZohobooksSalesinvoice(
                                            customer_id= invoice["customer_id"],
                                            exchange_rate= invoice["exchange_rate"],
                                            item_id= data["line_item_id"],
                                            description= data["description"],
                                            rate= data["rate"],
                                            quantity= data["quantity"],
                                            discount= data["discount"],
                                            adjustment= invoice["adjustment_description"],
                                            start_date= invoice["date"],
                                           
                                          )
        
        return invoice_obj.__dict__


    def new_expense(self, context, payload):
        ''' triggers when new expence created'''
        expense=payload["JSONString"]["expense"]
        expense_obj = ZohobooksExpense(
                                       account_id= expense["account_id"],
                                       date= expense["date"],
                                       amount= expense["amount"]
                                      )
        return expense_obj.__dict__

                                    