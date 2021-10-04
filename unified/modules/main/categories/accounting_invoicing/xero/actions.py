from unified.core.actions import Actions
from accounting_invoicing.xero import util
from accounting_invoicing.xero.entities.xero_contact import XeroContact
from accounting_invoicing.xero.entities.xero_invoice import XeroInvoice
from accounting_invoicing.xero.entities.xero_credit_note import XeroCreditNote
from accounting_invoicing.xero.entities.xero_payment import XeroPayment
from accounting_invoicing.xero.entities.xero_draft import XeroDraft
from accounting_invoicing.xero.entities.xero_purchase_order import XeroPurchaseOrder
from accounting_invoicing.xero.api import XeroApi
import json
import requests

class XeroActions(Actions):

    base_url = "https://api.xero.com/api.xro/2.0/"

    def create_contact(self, context, payload):
        """ Create a contact"""

        accesstoken = util.get_xero_client(context["headers"])
        contact = XeroContact(**payload)
        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : contact.organization_id,
            "Authorization" : f"Bearer {accesstoken}"
        }
        data = {
            "name" : contact.name
        }

        if contact.account_number is not None:
            data["AccountNumber"] = contact.account_number
        
        if contact.first_name is not None:
            data["FirstName"] = contact.first_name

        if contact.last_name is not None:
            data["LastName"] = contact.last_name

        if contact.email is not None:
            data["EmailAddress"] = contact.email

        # if contact.phone is not None:
        #     data["Phones"] = contact.phone

        if contact.address_city is not None:
            data["Addresses"] = [{
                "AttentionTo" : contact.address_attention,
                "City" : contact.address_city,
                "Country" : contact.address_country,
                "PostalCode" : contact.address_postal
            }]
        
        response = requests.request("POST", f"{self.base_url}Contacts", headers=headers, json= data).text
        return json.loads(response)

    def create_bill_invoice(self, context, payload):
        """ Create bill Invoice"""

        accesstoken = util.get_xero_client(context["headers"])
        invoice_data = XeroInvoice(**payload)

        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : invoice_data.organization_id,
            "Authorization" : f"Bearer {accesstoken}"
        }

        # Create contact if contact is not exists create contact else get contact_Id
        contact_data = XeroApi.contact_by_name(self, context, payload)
        
        if "message" in contact_data:
            data = {
                "name": invoice_data.name,
                "organization_id": invoice_data.organization_id
            }
            contact_data = self.create_contact(context, data)
            contact_id = contact_data["Contacts"][0]["ContactID"]            
        else:
            contact_id = contact_data.get("contact_id")
            
        data = {
            "Type" : "ACCREC",
            "Contact":{
                "ContactID": contact_id
            }
        }
        lineItems = [{}]

        if invoice_data.description is not None:
            lineItems[0]["Description"] = invoice_data.description

        if invoice_data.quantity is not None:
            lineItems[0]["Quantity"] = invoice_data.quantity

        if invoice_data.unit_price is not None:
            lineItems[0]["UnitAmount"] = invoice_data.unit_price

        if invoice_data.account is not None:
            lineItems[0]["AccountCode"] = invoice_data.account

        if invoice_data.discount is not None:
            lineItems[0]["DiscountRate"] = invoice_data.discount
        
        if invoice_data.tax_rate is not None:
            lineItems[0]["TaxType"] = invoice_data.tax_rate

        if invoice_data.item_code is not None:
            lineItems[0]["ItemCode"] = invoice_data.item_code

        data["LineItems"] = lineItems

        if invoice_data.line_items_type is not None:
            data["LineAmountTypes"] = invoice_data.line_items_type

        if invoice_data.due_date is not None:
            data["DueDateString"] = invoice_data.due_date

        if  invoice_data.creation_date is not None:
            data["DateString"] = invoice_data.creation_date

        if invoice_data.status is not None:
            data["Status"] = invoice_data.status

        if invoice_data.reference is not None:
            data["Reference"] = invoice_data.reference

        if invoice_data.branding_theme is not None:
            data["BrandingThemeID"] = invoice_data.branding_theme
        
        if invoice_data.currency is not None:
            data["CurrencyCode"] = invoice_data.currency
        
        if invoice_data.number is not None:
            data["InvoiceNumber"] = invoice_data.number
        
        if invoice_data.send_to_contact is not None:
            data["SentToContact"] = invoice_data.send_to_contact        

        # TODO: Need to work for attachments
        invoice = {"Invoices": [data]}
        response = requests.request("POST", f"{self.base_url}Invoices", headers=headers, json=invoice).text
        return json.loads(response)

    def add_items_to_existing_sales_invoice(self, context, payload):
        """ Adds line items to an existing sales invoice."""

        accesstoken = util.get_xero_client(context["headers"])
        invoice_data = XeroInvoice(**payload)

        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : invoice_data.organization_id,
            "Authorization" : f"Bearer {accesstoken}"
        }

        data = {}
        lineItems = [{}]

        if invoice_data.description is not None:
            lineItems[0]["Description"] = invoice_data.description

        if invoice_data.quantity is not None:
            lineItems[0]["Quantity"] = invoice_data.quantity

        if invoice_data.unit_price is not None:
            lineItems[0]["UnitAmount"] = invoice_data.unit_price

        if invoice_data.account is not None:
            lineItems[0]["AccountCode"] = invoice_data.account

        if invoice_data.discount is not None:
            lineItems[0]["DiscountRate"] = invoice_data.discount
        
        if invoice_data.tax_rate is not None:
            lineItems[0]["TaxType"] = invoice_data.tax_rate

        if invoice_data.item_code is not None:
            lineItems[0]["ItemCode"] = invoice_data.item_code

        data["LineItems"] = lineItems

        if invoice_data.line_items_type is not None:
            data["LineAmountTypes"] = invoice_data.line_items_type

        if invoice_data.due_date is not None:
            data["DueDateString"] = invoice_data.due_date

        if  invoice_data.creation_date is not None:
            data["DateString"] = invoice_data.creation_date

        if invoice_data.status is not None:
            data["Status"] = invoice_data.status

        if invoice_data.reference is not None:
            data["Reference"] = invoice_data.reference

        if invoice_data.branding_theme is not None:
            data["BrandingThemeID"] = invoice_data.branding_theme
        
        if invoice_data.currency is not None:
            data["CurrencyCode"] = invoice_data.currency
        
        if invoice_data.number is not None:
            data["InvoiceNumber"] = invoice_data.number
        
        if invoice_data.send_to_contact is not None:
            data["SentToContact"] = invoice_data.send_to_contact

        invoice = {"Invoices": [data]}
        response = requests.request("POST", f"{self.base_url}Invoices/{invoice_data.invoice_id}", headers=headers, json=invoice).text
        return json.loads(response)

    def  create_credit_note(self, context, payload):
        """ Creates a new credit note for a contact."""

        accesstoken = util.get_xero_client(context["headers"])
        credit_note_data = XeroCreditNote(**payload)

        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : credit_note_data.organization_id,
            "Authorization" : f"Bearer {accesstoken}"
        }

        data= {
          "Type": credit_note_data.type,
          "Contact": {
            "ContactID": credit_note_data.contact_id 
          }
        }
        lineItems = [{}]

        if credit_note_data.description is not None:
            lineItems[0]["Description"] = credit_note_data.description

        if credit_note_data.quantity is not None:
            lineItems[0]["Quantity"] = credit_note_data.quantity

        if credit_note_data.unit_price is not None:
            lineItems[0]["UnitAmount"] = credit_note_data.unit_price

        if credit_note_data.account is not None:
            lineItems[0]["AccountCode"] = credit_note_data.account

        if credit_note_data.discount is not None:
            lineItems[0]["DiscountRate"] = credit_note_data.discount
        
        if credit_note_data.tax_rate is not None and credit_note_data.tax_rate != "NONE":
            lineItems[0]["TaxAmount"] = credit_note_data.tax_rate

        if credit_note_data.item_code is not None:
            lineItems[0]["ItemCode"] = credit_note_data.item_code

        if credit_note_data.tax_type is not None:
            lineItems[0]["TaxType"] = credit_note_data.tax_type

        data["LineItems"] = lineItems

        if credit_note_data.account is not None:
            data["AccountCode"] = credit_note_data.account
        
        if credit_note_data.due_date is not None:
            data["DueDate"] = credit_note_data.due_date
        
        if credit_note_data.credit_note_number is not None:
            data["CreditNoteNumber"] = credit_note_data.credit_note_number

        if credit_note_data.currency is not  None:
            data["CurrencyCode"] = credit_note_data.currency

        if credit_note_data.credit_note_status is not None:
            data["Status"] = credit_note_data.credit_note_status

        # TODO:  Need to add attachment functionality

        credit_note = {"CreditNotes":[data]}
        response = requests.request("POST", f"{self.base_url}CreditNotes", headers=headers, json=credit_note).text
        return json.loads(response)

    def create_new_quote_draft(self, context, payload):
        """ Creates a new quote draft"""

        accesstoken = util.get_xero_client(context["headers"])
        draft_data = XeroDraft(**payload)

        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : draft_data.organization_id,
            "Authorization" : f"Bearer {accesstoken}"
        }

        data = {
            "Contact": { 
              "ContactID": draft_data.contact_id 
            },
            "Date": draft_data.date
        }
        lineItems = [{}]

        if draft_data.description is not None:
            lineItems[0]["Description"] = draft_data.description

        if draft_data.quantity is not None:
            lineItems[0]["Quantity"] = draft_data.quantity

        if draft_data.unit_price is not None:
            lineItems[0]["UnitAmount"] = draft_data.unit_price

        if draft_data.account is not None:
            lineItems[0]["AccountCode"] = draft_data.account

        if draft_data.discount is not None:
            lineItems[0]["DiscountRate"] = draft_data.discount
        
        if draft_data.tax_rate is not None and draft_data.tax_rate != "NONE":
            lineItems[0]["TaxAmount"] = draft_data.tax_rate

        if draft_data.item_code is not None:
            lineItems[0]["ItemCode"] = draft_data.item_code

        data["LineItems"] = lineItems

        if draft_data.expiry is not None:
            data["ExpiryDate"] = draft_data.expiry
        
        if draft_data.quote_number is not None:
            data["QuoteNumber"] = draft_data.quote_number

        if draft_data.reference is not None:
            data["Reference"] = draft_data.reference

        if draft_data.theme is not None:
            data["BrandingThemeID"] = draft_data.theme

        if draft_data.title is not None:
            data["Title"] = draft_data.title

        if draft_data.summary is not None:
            data["Summary"] = draft_data.summary

        if draft_data.currency is not None:
            data["CurrencyCode"] = draft_data.currency

        if draft_data.amounts_are is not None:
            data["LineAmountTypes"] = draft_data.amounts_are 

        if draft_data.terms is not None:
            data["Terms"] = draft_data.terms

        quotes_data = data
        response = requests.request("POST", f"{self.base_url}Quotes", headers=headers, json=quotes_data).text
        return json.loads(response)

    def create_payment(self, context, payload):
        """ Create a payment to an invoice"""

        accesstoken = util.get_xero_client(context["headers"])
        payment_data = XeroPayment(**payload)

        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : payment_data.organization_id,
            "Authorization" : f"Bearer {accesstoken}"
        }
        data = {
        	"Payments": [{
        		"Invoice": {
        			"InvoiceID": payment_data.document_id
        		},
        		"Account": {
        			"Code": payment_data.paid_to
        		},
        		"Date": payment_data.due_date,
        		"Amount": payment_data.amount,
                "Reference": payment_data.reference
        	}]
        }
        
        response = requests.request("POST", f"{self.base_url}Payments", headers= headers, json= data).text
        return json.loads(response)

    def create_purchase_order(self, context, payload):
        """ Creates a new purchase order for a contact"""

        accesstoken = util.get_xero_client(context["headers"])
        purchase_data = XeroPurchaseOrder(**payload)

        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : purchase_data.organization_id,
            "Authorization" : f"Bearer {accesstoken}"
        }

        data = {
            "Contact": { 
              "ContactID": purchase_data.contact_id 
            }
        }
        lineItems = [{}]

        if purchase_data.description is not None:
            lineItems[0]["Description"] = purchase_data.description

        if purchase_data.quantity is not None:
            lineItems[0]["Quantity"] = purchase_data.quantity

        if purchase_data.unit_price is not None:
            lineItems[0]["UnitAmount"] = purchase_data.unit_price

        if purchase_data.account is not None:
            lineItems[0]["AccountCode"] = purchase_data.account

        if purchase_data.discount is not None:
            lineItems[0]["DiscountRate"] = purchase_data.discount
        
        if purchase_data.tax_rate is not None and purchase_data.tax_rate != "NONE":
            lineItems[0]["TaxAmount"] = purchase_data.tax_rate

        if purchase_data.item_code is not None:
            lineItems[0]["ItemCode"] = purchase_data.item_code

        if purchase_data.tax_type is not None:
            lineItems[0]["TaxType"] = purchase_data.tax_type

        data["LineItems"] = lineItems

        if purchase_data.date is not None:
            data["Date"] = purchase_data.date

        if purchase_data.delivery_date is not None:
            data["DeliveryDate"] = purchase_data.delivery_date
        
        if purchase_data.order_number is not None:
            data["PurchaseOrderNumber"] = purchase_data.order_number

        if purchase_data.reference is not None:
            data["Reference"] = purchase_data.reference

        if purchase_data.theme is not None:
            data["BrandingThemeID"] = purchase_data.theme

        if purchase_data.currency is not None:
            data["CurrencyCode"] = purchase_data.currency

        if purchase_data.delivery_address is not None:
            data["DeliveryAddress"] = purchase_data.delivery_address

        if purchase_data.currency is not None:
            data["CurrencyCode"] = purchase_data.currency

        if purchase_data.telephone is not None:
            data["Telephone"] = purchase_data.telephone 

        if purchase_data.purchase_order_status is not None:
            data["Status"] = purchase_data.purchase_order_status

        #  TODO: Need to implement attachment
        purchase_info = {"PurchaseOrders":[data]}
        response = requests.request("POST", f"{self.base_url}PurchaseOrders", headers=headers, json=purchase_info).text
        return json.loads(response)

    def create_sales_invoice(self, context, payload):
        """ Creates a new sales invoice (Accounts Receivable)"""

        return self.create_bill_invoice(context, payload)

    def update_contact(self, context, payload):
        """ Update contact by Id"""

        accesstoken = util.get_xero_client(context["headers"])
        contact = XeroContact(**payload)
        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : contact.organization_id,
            "Authorization" : f"Bearer {accesstoken}"
        }
        data = {
            "name" : contact.name
        }

        if contact.account_number is not None:
            data["AccountNumber"] = contact.account_number
        
        if contact.first_name is not None:
            data["FirstName"] = contact.first_name

        if contact.last_name is not None:
            data["LastName"] = contact.last_name

        if contact.email is not None:
            data["EmailAddress"] = contact.email

        # if contact.phone is not None:
        #     data["Phones"] = contact.phone

        if contact.address_city is not None:
            data["Addresses"] = [{
                "AttentionTo" : contact.address_attention,
                "City" : contact.address_city,
                "Country" : contact.address_country,
                "PostalCode" : contact.address_postal
            }]
        
        response = requests.request("POST", f"{self.base_url}Contacts/{contact.contact_id}", headers=headers, json=data).text
        return json.loads(response)

    def send_sales_invoice_by_email(self, context, payload):
        """ Sends an invoice via email"""

        # Note:
        # The invoice must be of Type ACCREC and a valid Status for sending (SUMBITTED,AUTHORISED or PAID)
        # The email will be sent to the primary email address of the contact on the invoice and any additional contact persons that have IncludeInEmails flag set to true. The sender will be the user who authorised the app connection.
        accesstoken = util.get_xero_client(context["headers"])
        invoice_data = XeroInvoice(**payload)

        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : invoice_data.organization_id,
            "Authorization" : f"Bearer {accesstoken}"
        }
        response = requests.request("POST", f"{self.base_url}Invoices/{invoice_data.invoice_id}/Email", headers=headers, json={}).text
        if response == "":
            return {"message":"Mail sent"}
        return response