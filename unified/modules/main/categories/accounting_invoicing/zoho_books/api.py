from accounting_invoicing.zoho_books import util
from accounting_invoicing.zoho_books.entities.zoho_books_sales_invoice import ZohobooksSalesinvoice
import json


class ZohobooksApi():

    def find_invoice(self, context, params):
        ''' gets all invoices'''
        access_token = util.get_access_token(context['headers'])
        #url = f"https://books.zoho.in/api/v3/invoices/{params['invoice_id']}/?organization_id={params['organization_id']}"
        response = json.loads(util.rest("GET", 'invoices', {}, access_token,params['organization_id'],params['invoice_id']).text)
        print(response)
        invoice = response.get('invoice')
    
        invoice_obj = ZohobooksSalesinvoice(
                                            customer_id=invoice['customer_id'],                      
                                            invoice_number=invoice['invoice_number'],
                                            exchange_rate=invoice['exchange_rate'],
                                            item_id=invoice['line_items'][0]['item_id'],
                                            description=invoice['line_items'][0]['description'],
                                            quantity=invoice['line_items'][0]['quantity'],
                                            rate=invoice['line_items'][0]['rate'],
                                            discount=invoice['discount'],
                                            line_items_discount=invoice['line_items'][0]['discounts'],
                                            payment_options=invoice['payment_options'],
                                            shipping_charge=invoice['shipping_charge'],
                                            adjustment=invoice['adjustment'],
                                            note=invoice['notes']
                                            )
        return invoice_obj.__dict__