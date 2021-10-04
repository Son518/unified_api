import json
from accounting_invoicing.freshbooks.entities.freshbooks_invoice import FreshbooksInvoice
from accounting_invoicing.freshbooks.entities.freshbooks_client import FreshbooksClient
from accounting_invoicing.freshbooks import util

class FreshbooksApi():

    def invoice(self,context,params):
        """gets invoice by invoice_id"""
        url = f"https://api.freshbooks.com/accounting/account/{params['account_id']}/invoices/invoices/{params['invoice_id']}"
        result = json.loads(util.rest("GET", url, {}, context["headers"]["access_token"]).text)
        invoice = result["response"]["result"]["invoice"]
        invoice_obj = FreshbooksInvoice(
                                        account_id=invoice['accountid'],
                                        customerid=invoice['customerid'],                      
                                        invoice_id=invoice['invoiceid'],
                                        currency_code=invoice['currency_code'],
                                        language=invoice['language'],
                                        terms=invoice['terms'],
                                        discount_value=invoice['discount_value'],
                                        discount_amount=invoice['discount_total']['amount'],
                                        invoice_number=invoice['invoice_number'],
                                        po_number=invoice['po_number'],
                                        amount=invoice['amount']['amount'],
                                        code=invoice['amount']['code'],
                                        create_date=invoice['create_date']
                                    )
        return invoice_obj.__dict__    

    def client(self,context,params):
        """gets clients by customer_id"""
        url = f"https://api.freshbooks.com/accounting/account/{params['account_id']}/users/clients/{params['id']}"
        result = json.loads(util.rest("GET", url, {}, context["headers"]["access_token"]).text)
        client = result["response"]["result"]["client"]
        client_obj = FreshbooksClient(
                                    accounting_systemid=client['accounting_systemid'],                     
                                    first_name=client['fname'],
                                    last_name=client['lname'],
                                    email=client['email'],
                                    vat_name=client['vat_name'],
                                    vat_number=client['vat_number'],
                                    home_phone=client['home_phone'],
                                    organization=client['organization'],
                                    username=client['username']
                                )
        return client_obj.__dict__