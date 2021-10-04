import json

from accounting_invoicing.wave.entities.wave_customer import WaveCustomer
from accounting_invoicing.wave.entities.wave_account import WaveAccount
from accounting_invoicing.wave.entities.wave_business import WaveBusiness
from accounting_invoicing.wave import util

class WaveApi():

    def customer_by_email(self, context, params):
        '''Finds customer by email'''
        headers = context["headers"]
        query = '''query ($businessId: ID!, $email: String) {
              business(id: $businessId) {
                id
                customers(email: $email) {
                  edges {
                    node{
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
              }
              }}'''

        customers = []
        variables = {"businessId": params["business_id"],
                     "email": params["email"]}
        result = json.loads(util.get_wave_request("POST", wave_headers=headers, body=query, variables=variables).text)["data"]["business"]["customers"]["edges"]

        for customer in result:
            if customer["node"]["shippingDetails"] is None:
                return "Shipping details are not provided"
            wave_customer = WaveCustomer(
                customer_id=customer["node"]["id"],
                customer_name=customer["node"]["name"],
                account_number=customer["node"]["displayId"],
                currency=customer["node"]["currency"],
                first_name=customer["node"]["firstName"],
                last_name=customer["node"]["lastName"],
                email=customer["node"]["email"],
                phone_number=customer["node"]["phone"],
                toll_free_number=customer["node"]["tollFree"],
                mobile_number=customer["node"]["mobile"],
                fax_number=customer["node"]["fax"],
                website=customer["node"]["website"],
                address1=customer["node"]["address"]["addressLine1"],
                address2=customer["node"]["address"]["addressLine2"],
                city=customer["node"]["address"]["city"],
                country=customer["node"]["address"]["country"],
                province=customer["node"]["address"]["province"],
                postal_code=customer["node"]["address"]["postalCode"],
                shipping_contact=customer["node"]["shippingDetails"]["name"],
                shipping_delivery_instructions=customer["node"]["shippingDetails"]["instructions"],
                shipping_phone_number=customer["node"]["shippingDetails"]["phone"],
                shipping_address1=customer["node"]["shippingDetails"]["address"]["addressLine1"],
                shipping_address2=customer["node"]["shippingDetails"]["address"]["addressLine2"],
                shipping_city=customer["node"]["shippingDetails"]["address"]["city"],
                shipping_country=customer["node"]["shippingDetails"]["address"]["country"],
                shipping_province=customer["node"]["shippingDetails"]["address"]["province"],
                shipping_pin_code=customer["node"]["shippingDetails"]["address"]["postalCode"],
            )
            customers.append(wave_customer.__dict__)
        return json.dumps(customers)

    def accounts(self, context, params):
        '''Gets a list of accounts'''
        headers = context["headers"]
        query = '''query ($businessId: ID!) {
              business(id: $businessId) {
                id
                accounts(page: 1, pageSize: 20) {
                  pageInfo {
                    currentPage
                    totalPages
                    totalCount
                  }
                  edges {
                    node {
                      id
                      name
                      type {
                      value
                      }
                    }
                  }
                }
              }
            }'''
        variables = {"businessId": params["business_id"]}
        result = json.loads(util.get_wave_request("POST", wave_headers=headers, body=query, variables=variables).text)["data"]["business"]["accounts"]["edges"]

        accounts = []
        for account in result:
            wave_account = WaveAccount(
                account_id=account["node"]["id"],
                name=account["node"]["name"],
                type=account["node"]["type"]["value"]
                )
            accounts.append(wave_account.__dict__)
        return json.dumps(accounts)

    def businesses(self, context, params):
        headers = context["headers"]
        query = '''query {
              businesses {
                edges {
                  node {
                    id
                    name
                    salesTaxes {
                    edges {
                    node {
                    id
                    name
                    }
                    }
                    }
                  }
                }
              }
            }
            '''
        result = json.loads(util.get_wave_request("POST", wave_headers=headers, body=query).text)["data"]["businesses"]["edges"]
        businesses = []
        for business in result:
            wave_business = WaveBusiness(
                business_id=business["node"]["id"],
                name=business["node"]["name"],
                taxes=business["node"]["salesTaxes"]["edges"],
                )
            businesses.append(wave_business.__dict__)
        return json.dumps(businesses)
