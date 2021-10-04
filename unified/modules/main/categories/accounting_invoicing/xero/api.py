import json
import requests
from datetime import datetime, timezone
from accounting_invoicing.xero import util
from accounting_invoicing.xero.entities.xero_contact import XeroContact
from accounting_invoicing.xero.entities.xero_invoice import XeroInvoice


class XeroApi():

    base_url = "https://api.xero.com/api.xro/2.0/"

    def contact_by_name(self, context, params):
        """ Get contact by name"""

        accesstoken = util.get_xero_client(context["headers"])
        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : params.get("organization_id"),
            "Authorization" : f"Bearer {accesstoken}"
        }
        name = params.get('name')
        response = requests.request("GET", f'{self.base_url}Contacts?where=Name="{name}"', headers=headers).text
        response = json.loads(response)

        if len(response["Contacts"]) == 0:
            response["message"] = "Contact not exist"
            return response

        data = XeroContact(
            contact_id= response["Contacts"][0]["ContactID"],
            email= response["Contacts"][0]["EmailAddress"],
            name= response["Contacts"][0]["Name"],
            phone= response["Contacts"][0]["Phones"][0]["PhoneNumber"],
            mobile= response["Contacts"][0]["Phones"][0]["PhoneNumber"],
            address_city= response["Contacts"][0]["Addresses"][0]["City"],
            address_postal= response["Contacts"][0]["Addresses"][0]["PostalCode"],
            address_country= response["Contacts"][0]["Addresses"][0]["Country"],
            organization_id= params.get("organization_id")
        )
        return data.__dict__

    def invoice_by_number(self, context, params):
        """ Get invoice by number"""

        accesstoken = util.get_xero_client(context["headers"])
        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : params.get("organization_id"),
            "Authorization" : f"Bearer {accesstoken}"
        }
        number = params.get('number')
        response = requests.request("GET", f'{self.base_url}Invoices?InvoiceNumbers={number}', headers=headers).text
        response = json.loads(response)

        data = XeroInvoice(
            organization_id= params.get("organization_id"),
            item_code= response["Invoices"][0]["LineItems"][0]["Item"]["Code"],
            invoice_id= response["Invoices"][0]["InvoiceID"],
            description= response["Invoices"][0]["LineItems"][0]["Description"],
            name= response["Invoices"][0]["Contact"]["Name"],
            status= response["Invoices"][0]["Status"],
            currency= response["Invoices"][0]["CurrencyCode"],           
            creation_date= response["Invoices"][0]["DateString"],
            due_date= response["Invoices"][0]["DueDateString"],
            branding_theme= response["Invoices"][0]["BrandingThemeID"],
            number= response["Invoices"][0]["InvoiceNumber"],
            reference= response["Invoices"][0]["Reference"],
            line_items_type= response["Invoices"][0]["LineAmountTypes"],
            quantity= response["Invoices"][0]["LineItems"][0]["Quantity"],
            unit_price= response["Invoices"][0]["LineItems"][0]["UnitAmount"],
            discount= response["Invoices"][0]["LineItems"][0]["DiscountRate"],
            account= response["Invoices"][0]["LineItems"][0]["AccountCode"],
            tax_rate= response["Invoices"][0]["LineItems"][0]["TaxAmount"]
        )
        return data.__dict__

    def profile(self, context, params):
        """ Get Profile details"""

        accesstoken = util.get_xero_client(context["headers"])
        headers = {
            "Accept" : "application/json",
            "xero-tenant-id" : params.get("organization_id"),
            "Authorization" : f"Bearer {accesstoken}"
        }
        response = requests.request("GET", f'{self.base_url}Users', headers=headers)
        if response.ok:
            response = json.loads(response.text)["Users"][0]
            data = {
                "id": response["UserID"],
                "name": response["FirstName"]+" "+response["LastName"],
                "email": response["EmailAddress"]
            }        
            return data
        return response.json()