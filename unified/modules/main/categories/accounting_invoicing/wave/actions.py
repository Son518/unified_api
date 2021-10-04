import json

from unified.core.actions import Actions
from accounting_invoicing.wave.entities.wave_invoice import WaveInvoice
from accounting_invoicing.wave.entities.wave_customer import WaveCustomer
from accounting_invoicing.wave.entities.wave_product import WaveProduct
from accounting_invoicing.wave import util

class WaveActions(Actions):

    def create_customer(self, context, task_entity):
        '''Creates a new customer'''

        task_schema = WaveCustomer(**task_entity)

        query = '''mutation ($input: CustomerCreateInput!) {
          customerCreate(input: $input) {
            didSucceed
            inputErrors {
              code
              message
              path
            }
            customer {
              id
              name
              firstName
              lastName
              email
              phone
              tollFree
              mobile
              fax
              website
              displayId
              address {
                addressLine1
                addressLine2
                city
                province {
                  code
                  name
                }
                country {
                  code
                  name
                }
                postalCode
              }
              shippingDetails {
              name
              instructions
              phone
              address {
                addressLine1
                addressLine2
                city
                province {
                  code
                  name
                }
                country {
                  code
                  name
                }
                postalCode
              }
              }
              currency {
                code
              }
            }
          }
        }'''
        task_data = {
            "businessId": task_schema.business_id,
            "name": task_schema.customer_name,
            "displayId": task_schema.account_number,
            "currency": task_schema.currency,
            "firstName": task_schema.first_name,
            "lastName": task_schema.last_name,
            "email": task_schema.email,
            "phone": task_schema.phone_number,
            "tollFree": task_schema.toll_free_number,
            "mobile": task_schema.mobile_number,
            "fax": task_schema.fax_number,
            "website": task_schema.website,
            "address": {
                    "addressLine1": task_schema.address1,
                    "addressLine2": task_schema.address2,
                    "city": task_schema.city,
                    "countryCode": task_schema.country,
                    "provinceCode": task_schema.province,
                    "postalCode": task_schema.postal_code,
                  },
            "shippingDetails":{
                "name": task_schema.shipping_contact,
                "instructions": task_schema.shipping_delivery_instructions,
                "phone": task_schema.shipping_phone_number,
                "address": {
                        "addressLine1": task_schema.shipping_address1,
                        "addressLine2": task_schema.shipping_address2,
                        "city": task_schema.shipping_city,
                        "countryCode": task_schema.shipping_country,
                        "provinceCode": task_schema.shipping_province,
                        "postalCode": task_schema.shipping_pin_code,
                      },
                }
        }
        variables = {"input": task_data}
        headers = context["headers"]

        response = util.get_wave_request("POST", wave_headers=headers, body=query, variables=variables)
        return json.loads(response.text)


    def create_invoice(self, context, task_entity):
        '''Creates a new invoice'''

        task_schema = WaveInvoice(**task_entity)

        query = '''mutation ($input: InvoiceCreateInput!) {
            invoiceCreate(input: $input) {
            didSucceed
            inputErrors {
              message
              code
              path
            }
            invoice {
              id
              createdAt
              modifiedAt
              pdfUrl
              viewUrl
              status
              title
              subhead
              invoiceNumber
              invoiceDate
              poNumber
              customer {
                id
                name
              }
              currency {
                code
              }
              dueDate
              amountDue {
                value
                currency {
                  symbol
                }
              }
              amountPaid {
                value
                currency {
                  symbol
                }
              }
              taxTotal {
                value
                currency {
                  symbol
                }
              }
              total {
                value
                currency {
                  symbol
                }
              }
              exchangeRate
              footer
              memo
              disableCreditCardPayments
              disableBankPayments
              itemTitle
              unitTitle
              priceTitle
              amountTitle
              hideName
              hideDescription
              hideUnit
              hidePrice
              hideAmount
              items {
                product {
                  id
                  name
                }
                description
                quantity
                price
                subtotal {
                  value
                  currency {
                    symbol
                  }
                }
                total {
                  value
                  currency {
                    symbol
                  }
                }
                account {
                  id
                  name
                  subtype {
                    name
                    value
                  }
                }
                taxes {
                  amount {
                    value
                  }
                  salesTax {
                    id
                    name
                  }
                }
              }
              lastSentAt
              lastSentVia
              lastViewedAt
            }
            }
            }'''
        task_data = {
            "businessId": task_schema.business_id,
            "customerId": task_schema.customer_id,
            "currency": task_schema.invoice_currency,
            "invoiceDate": task_schema.invoice_date,
            "invoiceNumber": task_schema.invoice_number,
            "title": task_schema.invoice_title,
            "status": task_schema.status,
            "subhead": task_schema.subhead,
            "footer": task_schema.footer,
            "poNumber": task_schema.so_or_po_number,
            "dueDate": task_schema.end_date,
            "exchangeRate": task_schema.exchange_rate,
            "disableCreditCardPayments": task_schema.disable_credit_card_payments,
            "amountTitle": task_schema.ammount_title,
            "itemTitle": task_schema.item_title,
            "priceTitle": task_schema.price_title,
            "hideAmount": task_schema.hide_amount,
            "hideDescription": task_schema.hide_description,
            "hideUnit": task_schema.hide_item,
            "hidePrice": task_schema.hide_price,
            "items": [{
                    "description": task_schema.item_description,
                    "unitPrice": task_schema.item_price,
                    "productId": task_schema.item_product,
                    "quantity": task_schema.item_quantity,
                    'taxes': {
                        "salesTaxId": task_schema.item_tax}
                  }]
            }
        variables = {"input": task_data}
        headers = context["headers"]

        response = util.get_wave_request("POST", wave_headers=headers, body=query, variables=variables)
        return json.loads(response.text)

    def create_product_or_service(self, context, task_entity):
        '''Creates a new product'''

        task_schema = WaveProduct(**task_entity)

        query = '''mutation ($input: ProductCreateInput!) {
              productCreate(input: $input) {
                didSucceed
                inputErrors {
                  code
                  message
                  path
                }
                product {
                  id
                  name
                  description
                  unitPrice
                  incomeAccount {
                    id
                    name
                  }
                  expenseAccount {
                    id
                    name
                  }
                  isSold
                  isBought
                  isArchived
                  createdAt
                  modifiedAt
                }
              }
            }'''
        task_data = {
            "businessId": task_schema.business_id,
            "name": task_schema.name,
            "description": task_schema.description,
            "unitPrice": task_schema.price,
            "incomeAccountId": task_schema.income_account,
            "expenseAccountId": task_schema.expence_account,
        }
        variables = {"input": task_data}
        headers = context["headers"]

        response = util.get_wave_request("POST", wave_headers=headers, body=query, variables=variables)
        return json.loads(response.text)

    def record_sale(self, context, task_entity):
        '''Records a new income transaction'''

        pass
