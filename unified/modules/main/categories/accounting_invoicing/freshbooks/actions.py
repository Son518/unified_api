import json
from unified.core.actions import Actions
from accounting_invoicing.freshbooks import util
from accounting_invoicing.freshbooks.entities.freshbooks_client import FreshbooksClient
from accounting_invoicing.freshbooks.entities.freshbooks_invoice import FreshbooksInvoice
from accounting_invoicing.freshbooks.entities.freshbooks_estimate import FreshbooksEstimate
from accounting_invoicing.freshbooks.entities.freshbooks_expense import FreshbooksExpense
from accounting_invoicing.freshbooks.entities.freshbooks_project import FreshbooksProject
from accounting_invoicing.freshbooks.entities.freshbooks_time_entry import FreshbooksTimeentry
from accounting_invoicing.freshbooks.entities.freshbooks_other_income import FreshbooksOtherIncome
from accounting_invoicing.freshbooks.entities.freshbooks_recurring_invoice import FreshbooksRecurringinvoice
from accounting_invoicing.freshbooks.entities.freshbooks_add_payment_to_invoice import FreshbooksAddPaymentToInvoice

class FreshbooksActions(Actions):

    def create_client(self,context,client_payload):
        """
        creates a client 
        context holds the headers 
        client_payloads holds the request.body  
        """
        client_entity = FreshbooksClient(**client_payload)
        data= {
            "client":{
                    "fname": client_entity.first_name,
                    "lname": client_entity.last_name,
                    "email": client_entity.email,
                    "organization": client_entity.organization,
                    "vat_name": client_entity.vat_name,
                    "vat_number": client_entity.vat_number,
                    "home_phone": client_entity.home_phone,
                    "p_street": client_entity.primary_street_1,
                    "p_street2": client_entity.primary_street_2,
                    "p_city": client_entity.primary_city,
                    "p_country": client_entity.primary_country,
                    "currency_code": client_entity.currency_code,
                    "language": client_entity.language,
                    "late_fee": {
                        "first_tax_name": client_entity.first_tax_name,
                        "first_tax_percent": client_entity.first_tax_percent,
                        "repeat": client_entity.repeat_late_fee,
                        "second_tax_name": client_entity.second_tax_name,
                        "second_tax_percent": client_entity.second_tax_percent,
                        "type": "percent",
                    },
                    "contacts": [
                                {
                                "email": client_entity.email,
                                "fname": client_entity.first1,
                                "lname": client_entity.last1,
                                }
                            ]
                        }
                    }                
        url = f"https://api.freshbooks.com/accounting/account/{client_entity.account_id}/users/clients"                        
        response = util.rest("POST",url,data,context["headers"]["access_token"])
        return json.loads(response.text)

    def create_invoice(self,context,invoice_payload):
        """
        creates a invoice 
        context holds the headers 
        invoice_payloads holds the request.body  
        """
        invoice_entity = FreshbooksInvoice(**invoice_payload)
        data1= {
                "invoice": {
                        "language": invoice_entity.language,
                        "currency_code": invoice_entity.currency_code,
                        "discount_value": invoice_entity.discount_value,
                        "invoice_number": invoice_entity.invoice_number,
                        "po_number": invoice_entity.po_number,
                        "terms": invoice_entity.terms,
                        "contactid": invoice_entity.contactid,
                        "late_fee": {
                                    "type": "percent",
                                    },
                        "lines":[
                                {
                                "description": invoice_entity.line_item_description,
                                "taxName1": invoice_entity.line_item_tax1_name,
                                "name": invoice_entity.line_item_name,
                                "qty": invoice_entity.line_item_quantity,
                                "type": invoice_entity.type,
                                "unit_cost": {
                                            "amount": invoice_entity.amount,
                                            "code": invoice_entity.code,
                                            },
                                }
                            ],
                        "owner": invoice_entity.owner,
                        "presentation": invoice_entity.presentation,
                        "customerid": invoice_entity.customerid,
                        "create_date": invoice_entity.create_date,
                        }
                    }          
        url = f"https://api.freshbooks.com/accounting/account/{invoice_entity.account_id}/invoices/invoices"                        
        response = util.rest("POST",url,data1,context["headers"]["access_token"])
        return json.loads(response.text)

    def create_estimate(self,context,estimate_payload):
        """
        creates a estimate 
        context holds the headers 
        estimate_payloads holds the request.body  
        """
        estimate_entity = FreshbooksEstimate(**estimate_payload)
        data2= {
                "estimate":{
                            "customerid": estimate_entity.customer_id,
                            "create_date": estimate_entity.create_date, 
                            }
                        }
        url = f"https://api.freshbooks.com/accounting/account/{estimate_entity.account_id}/estimates/estimates"                        
        response = util.rest("POST",url,data2,context["headers"]["access_token"])
        return json.loads(response.text)

    def create_expense(self,context,expense_payload):
        """
        creates a expense 
        context holds the headers 
        expense_payloads holds the request.body  
        """
        expense_entity = FreshbooksExpense(**expense_payload)
        data3= {
                "expense":{
                            "amount":{
                            "amount": expense_entity.amount,
                            },
                            "categoryid": expense_entity.category,
                            "staffid": expense_entity.staff_member,
                            "date": expense_entity.date,
                        }
                    }
        url = f"https://api.freshbooks.com/accounting/account/{expense_entity.account_id}/expenses/expenses"                        
        response = util.rest("POST",url,data3,context["headers"]["access_token"])
        return json.loads(response.text)

    def create_project(self,context,project_payload):
        """
        creates a project 
        context holds the headers 
        project_payloads holds the request.body  
        """
        project_entity = FreshbooksProject(**project_payload)
        data4= {
                "project": {
                            "title": project_entity.title,
                            "project_type": project_entity.project_type,
                            "fixed_price": project_entity.fixed_price,
                            }
                        }
        url = f"https://api.freshbooks.com/projects/business/{project_entity.business_id}/project"                        
        response = util.rest("POST",url,data4,context["headers"]["access_token"])
        return json.loads(response.text)

    def create_time_entry(self,context,time_entry_payload):
        """
        creates a time_entry 
        context holds the headers 
        time_entry_payloads holds the request.body  
        """
        time_entity = FreshbooksTimeentry(**time_entry_payload)
        data5= {
                "time_entry": {
                                "is_logged": time_entity.is_logged,
                                "duration": time_entity.duration,
                                "note": time_entity.note,
                                "started_at": time_entity.started_at,
                                "customerid": time_entity.customerid,
                                "project_id": time_entity.project_id,
                                }
                            }
        url = f"https://api.freshbooks.com/timetracking/business/{time_entity.business_id}/time_entries"                        
        response = util.rest("POST",url,data5,context["headers"]["access_token"])
        return json.loads(response.text)

    def create_other_income(self,context,other_income_payload):
        """
        creates a other_income
        context holds the headers 
        other_income_payloads holds the request.body  
        """
        income_entity = FreshbooksOtherIncome(**other_income_payload)
        data6= {
                "other_income": {
                    "amount": {
                                "amount": income_entity.amount, 
                                "code": income_entity.amount_code,
                                },
                    "category_name": income_entity.category_name,      
                    "date": income_entity.date,
                    "note": income_entity.note,
                    "payment_type": income_entity.payment_type,
                    "source": income_entity.source,
                    "taxes": [
                                {
                                "amount": income_entity.tax_amount,
                                "name": income_entity.name,
                                }
                            ]
                        }
                    }
        url = f"https://api.freshbooks.com/accounting/account/{income_entity.account_id}/other_incomes/other_incomes"                       
        response = util.rest("POST",url,data6,context["headers"]["access_token"])
        return json.loads(response.text)

    def create_recurring_invoice(self,context,recurring_invoice_payload):
        """
        creates a recurring_invoice
        context holds the headers 
        recurring_invoice_payloads holds the request.body  
        """
        recurring_entity = FreshbooksRecurringinvoice(**recurring_invoice_payload)
        data7= {
                "invoice_profile": {
                    "customerid": recurring_entity.customerid,
                    "create_date": recurring_entity.create_date,
                    "frequency": recurring_entity.frequency,
                    "numberRecurring": recurring_entity.numberRecurring,
                    }
                }
        url = f"https://api.freshbooks.com/accounting/account/{recurring_entity.account_id}/invoice_profiles/invoice_profiles"                       
        response = util.rest("POST",url,data7,context["headers"]["access_token"])
        return json.loads(response.text)

    def add_payment_to_invoice(self,context,payment_invoice_payload):
        """
        creates a addpaymenttoinvoice
        context holds the headers 
        payment_invoice_payloads holds the request.body  
        """
        payment_entity = FreshbooksAddPaymentToInvoice(**payment_invoice_payload)
        data8= {
                "payment":{
                            "invoiceid": payment_entity.invoice_id,
                            "amount": {
                                        "amount": payment_entity.amount
                                    },
                            "date": payment_entity.date,
                            "type": payment_entity.payment_type,
                        }
                    }
        url = f"https://api.freshbooks.com/accounting/account/{payment_entity.account_id}/payments/payments"                       
        response = util.rest("POST",url,data8,context["headers"]["access_token"])
        return json.loads(response.text)

    def create_invoice_pdf(self,context,invoice_payload):
        """
        creates a invoicepdf
        context holds the headers 
        invoice_payloads holds the request.body  
        """
        invoice_entity = FreshbooksInvoice(**invoice_payload)
        data9= {
                "invoice": {
                        "language": invoice_entity.language,
                        "currency_code": invoice_entity.currency_code,
                        "discount_value": invoice_entity.discount_value,
                        "invoice_number": invoice_entity.invoice_number,
                        "po_number": invoice_entity.po_number,
                        "terms": invoice_entity.terms,
                        "contactid": invoice_entity.contactid,
                        "customerid": invoice_entity.customerid,
                        "create_date": invoice_entity.create_date,
                        "invoiceid": invoice_entity.invoice_id,
                        }
                    }          
        url = f"https://api.freshbooks.com/accounting/account/{invoice_entity.account_id}/invoices/invoices"                        
        response = util.rest("POST",url,data9,context["headers"]["access_token"])
        return json.loads(response.text)

    def update_client(self,context,client_payload):
        """update a client_detailes"""
        client_entity = FreshbooksClient(**client_payload)
        data10= {
                "client": {
                    "fname": client_entity.first_name
                    }
                }
        url = f"https://api.freshbooks.com/accounting/account/{client_entity.account_id}/users/clients/{client_entity.user_id}"
        response = util.rest("PUT",url,data10,context["headers"]["access_token"])
        return json.loads(response.text)

    def update_invoice(self, context, invoice_payload):
        """update invoice"""
        invoice_entity = FreshbooksInvoice(**invoice_payload)
        data11= {
                "invoice": {
                    "due_offset_days": invoice_entity.days_due_from_issue,
                    }
                }
        url = f"https://api.freshbooks.com/accounting/account/{invoice_entity.account_id}/invoices/invoices/{invoice_entity.invoice_id}"
        response = util.rest("PUT",url,data11,context["headers"]["access_token"])
        return json.loads(response.text)
    
    def send_invoice(self,context,invoice_payload):
        """send invoice by email"""
        invoice_entity = FreshbooksInvoice(**invoice_payload)
        data12= {
                "invoice": {
                            "email_recipients": invoice_entity.email_recipients, 
                            "email_subject": invoice_entity.email_subject,
                            "email_body": invoice_entity.email_body,
                            "action_email": invoice_entity.action_email,
                            }
                        }
        url = f"https://api.freshbooks.com/accounting/account/{invoice_entity.account_id}/invoices/invoices/{invoice_entity.invoice_id}"
        response = util.rest("PUT",url,data12,context["headers"]["access_token"])
        return json.loads(response.text)

    def send_estimate(self,context,estimate_payload):
        """send estimate by email"""
        estimate_entity = FreshbooksEstimate(**estimate_payload)
        data13= {
                "estimate": {
                            "email_recipients": estimate_entity.email_recipients,                   
                            "email_subject": estimate_entity.email_subject,
                            "email_body": estimate_entity.email_body,
                            "action_email": estimate_entity.action_email,                           
                            }
                        }
        url = f"https://api.freshbooks.com/accounting/account/{estimate_entity.account_id}/estimates/estimates/{estimate_entity.estimate_id}"
        response = util.rest("PUT",url,data13,context["headers"]["access_token"])
        return json.loads(response.text)