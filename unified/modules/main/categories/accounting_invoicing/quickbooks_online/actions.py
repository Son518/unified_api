import random
from unified.core.actions import Actions
from accounting_invoicing.quickbooks_online import util
from accounting_invoicing.quickbooks_online.entities.quickbooks_bill import QuickbooksonlineBill
from accounting_invoicing.quickbooks_online.entities.quickbooks_refund import QuickbooksonlineRefund
from accounting_invoicing.quickbooks_online.entities.quickbooks_vendor import QuickbooksonlineVendors
from accounting_invoicing.quickbooks_online.entities.quickbooks_payment import QuickbooksonlinePayment
from accounting_invoicing.quickbooks_online.entities.quickbooks_journal import QuickbooksonlineJournal
from accounting_invoicing.quickbooks_online.entities.quickbooks_invoice import QuickbooksonlineInvoice
from accounting_invoicing.quickbooks_online.entities.quickbooks_purchase import QuickbooksonlinePurchase
from accounting_invoicing.quickbooks_online.entities.quickbooks_customer import QuickbooksonlineCustomer
from accounting_invoicing.quickbooks_online.entities.quickbooks_estimate import QuickbooksonlineEstimate
from accounting_invoicing.quickbooks_online.entities.quickbooks_bill_item import QuickbooksonlineBillItem
from accounting_invoicing.quickbooks_online.entities.quickbooks_credit_memo import QuickbooksonlineCreditMemo
from accounting_invoicing.quickbooks_online.entities.quickbooks_sales_receipt import QuickbooksonlieSalesReceipt
from accounting_invoicing.quickbooks_online.entities.quickbooks_time_activity import QuickbooksOnlineTimeActivity
from accounting_invoicing.quickbooks_online.entities.quickbooks_product_service import QuickbooksonlineProductService
import requests


class QuickbooksonlineActions(Actions):
    def create_customer(self, context, payload):
        '''creates a specific customer.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        customer = QuickbooksonlineCustomer(**payload)
        url = f"v3/company/{headers['realm_id']}/customer"
        request_body = {
            "FullyQualifiedName": customer.full_name,
            "PrimaryEmailAddr": {
                "Address": customer.email
            },
            "DisplayName": customer.display_name,
            "Title": customer.title,
            "FamilyName": customer.middle_name,
            "PrimaryPhone": {
                "FreeFormNumber": customer.phone
            },
            "CompanyName": customer.company,
            "BillAddr": {
                "CountrySubDivisionCode": customer.billing_address_state,
                "City": customer.billing_address_city,
                "PostalCode": customer.billing_address_zipcode,
                "Line1": customer.billing_address_street,
                "Country": customer.billing_address_country
            },
            "GivenName": customer.first_name,
            "Fax": {
                "FreeFormNumber": customer.fax
            },
            "WebAddr": {
                "URI": customer.website
            }, "Mobile": {
                "FreeFormNumber": customer.mobile
            }
        }
        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_estimate(self, context, payload):
        '''Create a new estimate'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/estimate?minorversion=59"
        estimate = QuickbooksonlineEstimate(**payload)
        request_body = {
            "ExpirationDate": estimate.expiration_date,
            "Line": [{
                "Description": estimate.line_decription,
                "DetailType": "SalesItemLineDetail",
                "SalesItemLineDetail": {
                    "TaxCodeRef": {
                        "value": estimate.line_item_tax_code
                    },
                    "Qty": estimate.line_item_quantity,
                    "ItemRef": {
                        "value": estimate.line_item
                    }
                },
                "Amount": estimate.line_amount,
                "Id": "1"
            }],
            "CustomerRef": {
                "value": estimate.customer_id
            }, "CustomerMemo": {
                "value": estimate.message_displayed_on_estimate
            },
        }
        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_invoice(self, context, payload):
        '''Adds a new invoice '''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/invoice"
        invoice = QuickbooksonlineInvoice(**payload)
        request_body = {
            "TxnDate": invoice.invoice_date,
            "Line": [
                {
                    "Description": invoice.product_description,
                    "DetailType": "SalesItemLineDetail",
                    "SalesItemLineDetail": {
                        "TaxCodeRef": {
                            "value": invoice.product_tax
                        },
                        "Qty": invoice.product_quantity,
                        "ItemRef": {
                            "value": invoice.product_id
                        },
                        "UnitPrice": invoice.product_rate,
                    },
                    "Amount": int(invoice.product_rate)*int(invoice.product_quantity),
                    "Id": "1",

                }
            ],
            "CustomerRef": {
                "value": invoice.customer_id
            },
            "DocNumber": invoice.invoice_id,
            "SalesTermRef": {
                "value": invoice.terms
            },
            "DueDate": invoice.due_date,
            "PrivateNote": invoice.message_displayed_on_statement,
            "CustomerMemo": {
                "value": invoice.message_displayed_on_invoice
            },
        }
        if invoice.send_later == 'true':
            request_body['EmailStatus'] = 'NotSet'
        if invoice.send_later == 'false':
            request_body['EmailStatus'] = 'NeedToSend'
            request_body["BillEmail"] = {"Address": invoice.email}

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_payment(self, context, payload):
        '''Creates a new payment, optionally linked to an invoice.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/payment"
        payload = QuickbooksonlinePayment(**payload)
        request_body = {
            "TotalAmt": payload.total_amount,
            "CustomerRef": {
                "value": payload.customer_id
            },
            "PrivateNote": payload.memo,
            "Line": [{
                "Amount": payload.line_amount,
                "LinkedTxn": [{
                    "TxnId": payload.line_linked_invoice_id,
                    "TxnType": "Invoice"
                }],
            }],

            "TxnDate": payload.transaction_date,
        }

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_vendor(self, context, payload):
        '''Adds a new vendor.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/vendor"
        vendor = QuickbooksonlineVendors(**payload)
        request_body = {
            "PrimaryEmailAddr": {
                "Address": vendor.email
            },
            "WebAddr": {
                "URI": vendor.website
            },
            "PrimaryPhone": {
                "FreeFormNumber": vendor.phone
            },
            "DisplayName": vendor.full_name,
            "BillAddr": {
                "City": vendor.address_city,
                "Line2": vendor.address_line2,
                "Line1": vendor.address_line1,
                "PostalCode": vendor.address_zip_code,
                "CountrySubDivisionCode": vendor.address_state_code
            }
        }
        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def send_invoice(self, context, payload):
        '''Send an existing invoice.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        invoice = QuickbooksonlineInvoice(**payload)
        url = f"v3/company/{headers['realm_id']}/invoice/{invoice.invoice_id}/send"
        response = util.rest("POST", url, access_token)
        return response.text, response.status_code

    def update_customer(self, context, payload):
        '''Updates an existing customer.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/customer"
        customer = QuickbooksonlineCustomer(**payload)
        request_body = {
            "Id": customer.customer_id,
            "FullyQualifiedName": customer.full_name,
            "PrimaryEmailAddr": {
                "Address": customer.email
            },
            "DisplayName": customer.display_name,
            "Title": customer.title,
            "FamilyName": customer.middle_name,
            "PrimaryPhone": {
                "FreeFormNumber": customer.phone
            },
            "CompanyName": customer.company,
            "BillAddr": {
                "CountrySubDivisionCode": customer.billing_address_state,
                "City": customer.billing_address_city,
                "PostalCode": customer.billing_address_zipcode,
                "Line1": customer.billing_address_street,
                "Country": customer.billing_address_country
            },
            "GivenName": customer.first_name,
            "Fax": {
                "FreeFormNumber": customer.fax
            },
            "WebAddr": {
                "URI": customer.website
            }, "Mobile": {
                "FreeFormNumber": customer.mobile
            },
            "SyncToken": random.randint(0, 10)

        }

        response = util.rest("POST", url, access_token, request_body)
        return response.text, response.status_code

    def update_invoice(self, context, payload):
        '''Updates an existing invoice (with line item support).'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/invoice"
        invoice = QuickbooksonlineInvoice(**payload)
        request_body = {
            "Id": invoice.invoice_id,
            "TxnDate": invoice.invoice_date,
            "Line": [
                {
                    "Description": invoice.product_description,
                    "DetailType": "SalesItemLineDetail",
                    "SalesItemLineDetail": {
                        "TaxCodeRef": {
                            "value": invoice.product_tax
                        },
                        "Qty": invoice.product_quantity,
                        "ItemRef": {
                            "value": invoice.product_id
                        },
                        "UnitPrice": invoice.product_rate,
                    },
                    "Amount": int(invoice.product_rate)*int(invoice.product_quantity),
                    "Id": "1",

                }
            ],
            "CustomerRef": {
                "value": invoice.customer_id
            },
            "DocNumber": invoice.invoice_id,
            "SalesTermRef": {
                "value": invoice.terms
            },
            "DueDate": invoice.due_date,
            "PrivateNote": invoice.message_displayed_on_statement,
            "CustomerMemo": {
                "value": invoice.message_displayed_on_invoice
            },
            "SyncToken": "0",
            # "Id": "238",
            "sparse": True,
        }
        if invoice.send_later == 'true':
            request_body['EmailStatus'] = 'NotSet'
        if invoice.send_later == 'false':
            request_body['EmailStatus'] = 'NeedToSend'
            request_body["BillEmail"] = {"Address": invoice.email}

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_bill_account(self, context, payload):
        '''Create a new bill, optionally tied to a customer (with line item support).'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        bill = QuickbooksonlineBill(**payload)
        url = f"v3/company/{headers['realm_id']}/bill"
        request_body = {
            "PrivateNote": bill.memo,
            "CurrencyRef": {
                "value": bill.currency
            },
            "DueDate": bill.due_date,
            "TxnDate": bill.transaction_date,
            "Line": [
                {
                    "Description": bill.line_item_description,
                    "DetailType": "AccountBasedExpenseLineDetail",
                    "AccountBasedExpenseLineDetail": {
                        "AccountRef": {
                            "value": bill.line_id
                        }
                    },
                    "Amount": int(bill.line_rate)*int(bill.line_quantity),
                    "Id": "1",

                }
            ],
            "VendorRef": {
                "value": bill.vendor_id
            },
            "DocNumber": bill.bill_number
        }
        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_bill_item(self, context, payload):
        '''Create a new bill, optionally tied to a customer.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        bill = QuickbooksonlineBillItem(**payload)
        url = f"v3/company/{headers['realm_id']}/bill"
        request_body = {
            "DueDate": bill.due_date,
            "TxnDate": bill.transaction_date,
            "Line": [
                {
                    "Description": bill.line_description,
                    "DetailType": "AccountBasedExpenseLineDetail",
                    "AccountBasedExpenseLineDetail": {
                        "AccountRef": {
                            "value": bill.line_item_id
                        },
                        "CustomerRef": {
                            "value": bill.customer_id
                        }
                    },
                    "Amount": int(bill.unit_price)*int(bill.quantity),
                    "Id": "1",

                }
            ],
            "VendorRef": {
                "value": bill.vendor_id
            },
            "DocNumber": bill.bill_number
        }

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_bill_line_item(self, context, payload):
        '''Create a new bill, optionally tied to a customer (with line item support).'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        bill_invoice = QuickbooksonlineInvoice(**payload)
        url = f"v3/company/{headers['realm_id']}/bill"
        request_body = {
            "PrivateNote": bill_invoice.memo,
            "CurrencyRef": {
                "value": bill_invoice.currency
            },
            "DueDate": bill_invoice.due_date,
            "TxnDate": bill_invoice.transaction_date,
            "Line": [
                {

                    "Description": bill_invoice.product_description,
                    "DetailType": "AccountBasedExpenseLineDetail",
                    "AccountBasedExpenseLineDetail": {
                        "AccountRef": {
                            "value": bill_invoice.product_id
                        },
                        "BillableStatus": bill_invoice.product_billable,
                        "CustomerRef": {
                            "value": bill_invoice.customer_id
                        }
                    },

                    "Amount": int(bill_invoice.product_rate)*int(bill_invoice.product_quantity),
                    "Id": "1",

                }
            ],
            "VendorRef": {
                "value": bill_invoice.vendor_id
            },
            "DocNumber": bill_invoice.bill_number
        }

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_credit_memo(self, context, payload):
        '''Creates a new credit memo.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        credit_memo = QuickbooksonlineCreditMemo(**payload)
        url = f"v3/company/{headers['realm_id']}/creditmemo"
        request_body = {
            "TxnDate": credit_memo.credit_memo_date,
            "Line": [
                {
                    "Description": credit_memo.product_description,
                    "DetailType": "SalesItemLineDetail",
                    "SalesItemLineDetail": {
                        "TaxCodeRef": {
                            "value": credit_memo.product_tax
                        },
                        "Qty": credit_memo.product_quantity,
                        "ItemRef": {
                            "value": credit_memo.product_id
                        },
                        "UnitPrice": credit_memo.product_rate,
                    },
                    "Amount": int(credit_memo.product_rate)*int(credit_memo.product_quantity),
                    "Id": "1",

                }
            ],
            "CustomerRef": {
                "value": credit_memo.customer_id
            },
            "DocNumber": credit_memo.invoice_id,
            "SalesTermRef": {
                "value": credit_memo.terms
            },
            "DueDate": credit_memo.due_date,
            # "PrivateNote": invoice.message_displayed_on_statement,
            "CustomerMemo": {
                "value": credit_memo.message_displayed_on_credit_memo
            },
            "ApplyTaxAfterDiscount": (credit_memo.apply_tax_after_discount == 'true')
        }
        if credit_memo.send_later == 'true':
            request_body['EmailStatus'] = 'NotSet'
        if credit_memo.send_later == 'false':
            request_body['EmailStatus'] = 'NeedToSend'
            request_body["BillEmail"] = {"Address": invoice.email}

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_journal_entry(self, context, payload):
        '''Creates a new journal entry.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/journalentry"
        journal = QuickbooksonlineJournal(**payload)
        request_body = {
            "TxnDate": journal.journal_date,
            "DocNumber": journal.journal_number,
            "PrivateNote": journal.memo,
            "Line": [{
                "JournalEntryLineDetail": {
                    "PostingType": "Debit",
                    "AccountRef": {
                        "value": journal.debit_account_type_id
                    },
                },
                "DetailType": "JournalEntryLineDetail",
                "Amount": journal.debit_amount,
                "Id": "1",
                "Description": journal.debit_description
            },
                {
                "JournalEntryLineDetail": {
                    "PostingType": "Credit",
                    "AccountRef": {
                        "value": journal.credit_account_type_id
                    }
                },
                "DetailType": "JournalEntryLineDetail",
                "Amount": journal.credit_amount,
                "Description": journal.credit_description
            }
            ]
        }

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_product_service(self, context, payload):
        '''Creates a new product or service.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/item"
        service = QuickbooksonlineProductService(**payload)
        request_body = {
            "Name": service.name,
            "Sku": service.sku,
            "Description": service.description_on_sales_forms,
            "Active": True,
            "SubItem": True,
            "ParentRef": {
                "value": service.category_id
            },
            "Level": 1,
            "Taxable": service.is_taxable,
            "SalesTaxIncluded": True,
            "UnitPrice": service.sales_price,
            "PurchaseCost": service.cost,
            "Type": service.product_type,
            "IncomeAccountRef": {
                "value": service.income_account_type_id,
                "name": "Sales"
            },
            "ExpenseAccountRef": {
                "value": service.expense_account_type_id
            },
            "PurchaseDesc": service.description_on_purchase_forms
        }
        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_purchase_order(self, context, payload):
        '''Creates a new purchase order.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        purchase = QuickbooksonlinePurchase(**payload)
        url = f"v3/company/{headers['realm_id']}/purchaseorder"
        request_body = {
            "DocNumber": purchase.purchase_order_number,
            "TxnDate": purchase.purchase_order_date,
            "Line": [
                {
                    "DetailType": "ItemBasedExpenseLineDetail",
                    "Amount": int(purchase.product_rate)*int(purchase.product_quantity),
                    "Id": "1",
                    "Description": purchase.product_description,
                    "ItemBasedExpenseLineDetail": {
                        "ItemRef": {
                            "value": purchase.product_id
                        },
                        "CustomerRef": {
                            "value": purchase.product_customer_id
                        },
                        "Qty": purchase.product_quantity,
                        "TaxCodeRef": {
                            "value": "NON"
                        },
                        "BillableStatus": "NotBillable",
                        "UnitPrice": purchase.product_rate
                    }
                }
            ],
            "APAccountRef": {
                "value": purchase.account_type_id
            },
            "VendorRef": {
                "value": purchase.vendor_id
            },
            "Memo": purchase.memo,
        }
        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_refund_receipt(self, context, payload):
        '''Creates a new refund receipt.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        refund = QuickbooksonlineRefund(**payload)
        url = f"v3/company/{headers['realm_id']}/refundreceipt"
        request_body = {
            "DocNumber": refund.refund_receipt_number,
            "TxnDate": refund.refund_receipt_date,
            "PrivateNote": refund.message_displayed_on_refund_receipt,
            "Line": [
                {
                    "Description": refund.product_description,
                    "DetailType": "SalesItemLineDetail",
                    "Amount": refund.product_amount,
                    "SalesItemLineDetail": {
                        "ItemRef": {
                            "value": refund.product_id
                        },
                        "TaxCodeRef": {
                            "value": refund.product_tax
                        }
                    }
                }
            ],
            "CustomerMemo": {
                "value": refund.memo
            },
            "CustomerRef": {
                "value": refund.customer_id,
                # "name": "Shajavali Shaik"
            },
            "PaymentMethodRef": {
                "value": refund.payment_method,
                # "name": "Cash"
            },
            "DepositToAccountRef": {
                # "name": "Checking",
                "value": refund.refund_from
            }
        }

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_time_activity(self, context, payload):
        '''Creates a new single time activity.'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        time_activity = QuickbooksOnlineTimeActivity(**payload)
        url = f"v3/company/{headers['realm_id']}/timeactivity"
        request_body = {
            "TxnDate": time_activity.date,
            "EndTime": time_activity.end_time,
            "HourlyRate": time_activity.hourly_rate,
            "StartTime": time_activity.start_time,
            "BreakHours": time_activity.break_hours,
            "BreakMinutes": time_activity.break_minutes,
            "Description": "this is description",
            "CustomerRef": {
                "value": time_activity.customer_id
            },
            "NameOf": time_activity.time_activity_type,
        }
        if time_activity.time_activity_type.lower() == 'employee':
            request_body["EmployeeRef"] = {"value": time_activity.employee_id}
        if time_activity.time_activity_type.lower() == 'vendor':
            request_body["VendorRef"] = {"value": time_activity.vendor_id}

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code

    def create_sales_receipt(self, context, payload):
        '''Adds a new sales receipt (with line item support)'''

        headers = context['headers']
        receipt = QuickbooksonlieSalesReceipt(**payload)
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/salesreceipt"
        request_body = {
            "CustomerRef": {
                # "name": "Dylan Sollfrank",
                "value": receipt.customer_id
            },
            "CustomerMemo": {
                "value": receipt.message
            },
            "DocNumber": receipt.sales_receipt_number,
            "TxnDate": receipt.service_date,
            "Line": [
                {
                    "Description": receipt.line_description,
                    "DetailType": "SalesItemLineDetail",
                    "SalesItemLineDetail": {
                        "TaxCodeRef": {
                            "value": receipt.line_item_tax_code
                        },
                        "Qty": receipt.line_item_quantity,
                        "UnitPrice": receipt.line_item_unit_price,
                        "ItemRef": {
                            # "name": "Pest Control",
                            "value": receipt.product_id
                        }
                    },
                    "LineNum": 1,
                    "Amount": int(receipt.line_item_quantity)*int(receipt.line_item_unit_price),
                    # "Id": "1"
                }
            ]
        }

        response = util.rest("post", url, access_token, request_body)
        return response.text, response.status_code
