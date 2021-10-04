import json
from requests.models import Response
from accounting_invoicing.zoho_books.entities.zoho_books_estimate import ZohobooksEstimate
from core.actions import Actions
from accounting_invoicing.zoho_books.entities.zoho_books_customer import ZohobooksCustomer
from accounting_invoicing.zoho_books.entities.zoho_books_item import ZohobooksItem
from accounting_invoicing.zoho_books.entities.zoho_books_sales_invoice import ZohobooksSalesinvoice
from accounting_invoicing.zoho_books import util


class ZohobooksActions(Actions):

    def create_estimate(self, context, estimate_payload):
        """
        creates a new estimate
        context holds the headers 
        estimate_payload holds the request.body
        """
        access_token = util.get_access_token(context["headers"])
        estimate_entity = ZohobooksEstimate(**estimate_payload)
        entity_data={
            "customer_id": estimate_entity.customer_id,
            "date": estimate_entity.start_date,
            "expiry_date": estimate_entity.end_date,
            "exchange_rate": estimate_entity.exchange_rate,
            "discount": estimate_entity.discount,
            "line_items": [{
                    "item_id": estimate_entity.item_id,
                    "rate": estimate_entity.rate,
                    "quantity": estimate_entity.quantity,
                        }],
            "notes": estimate_entity.estimate_notes,
            "terms": estimate_entity.estimate_terms
                    }
        response = util.rest("POST","estimates",entity_data,access_token,estimate_entity.organization_id)
        return json.loads(response.text)

    def create_customer(self, context, customer_payload):
        """
        creates a new customer
        context holds the headers 
        customer_payload holds the request.body
        """
        access_token = util.get_access_token(context["headers"])
        customer_entity = ZohobooksCustomer(**customer_payload)
        customer_data = {
                    "contact_name": customer_entity.contact_name,
                    "company_name": customer_entity.company_name,
                    "website": customer_entity.website,
                    "payment_terms": customer_entity.payment_terms,
                    "notes": customer_entity.notes,
                    "billing_address": {  
                                         "address": customer_entity.billing_address,
                                         "city": customer_entity.billing_address_city,
                                         "state": customer_entity.billing_address_state,
                                         "zip": customer_entity.billing_address_zip,
                                         "country": customer_entity.billing_address_country,
                                         "fax": customer_entity.billing_address_fax,
                                       },
                    "shipping_address": {
                                         "address": customer_entity.shipping_address,
                                         "city": customer_entity.shipping_address_city,
                                         "state": customer_entity.shipping_address_state,
                                         "zip": customer_entity.shipping_address_zip,
                                         "country": customer_entity.shipping_address_country,
                                         "fax": customer_entity.shipping_address_fax,
                                         },
                    "contact_persons": 
                        [{
                            "first_name": customer_entity.first_name,
                            "last_name": customer_entity.last_name,
                            "email": customer_entity.email,
                            "phone": customer_entity.phone,
                            "mobile": customer_entity.mobile,
                        }] 
                   }
        response = util.rest("POST",'customers',customer_data,access_token,customer_entity.organization_id)
        return response.text, response.status_code                                  
                  
    def create_item(self, context, item_payload):
        """
        creates a new item
        context holds the headers 
        item_payload holds the request.body
        """
        access_token = util.get_access_token(context["headers"])
        item_entity = ZohobooksItem(**item_payload)
        entity_data = { "name": item_entity.item_name,
                        "description": item_entity.description,
                        "rate": item_entity.rate,
                        "tax_percentage": item_entity.tax_percentage
                      }                           
        response = util.rest("POST",'items',entity_data,access_token,item_entity.organization_id)
        return response.text, response.status_code

           