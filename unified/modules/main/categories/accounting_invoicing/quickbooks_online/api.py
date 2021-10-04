import json
from accounting_invoicing.quickbooks_online import util
from accounting_invoicing.quickbooks_online.entities.quickbooks_bill import QuickbooksonlineBill
from accounting_invoicing.quickbooks_online.entities.quickbooks_vendor import QuickbooksonlineVendors
from accounting_invoicing.quickbooks_online.entities.quickbooks_invoice import QuickbooksonlineInvoice
from accounting_invoicing.quickbooks_online.entities.quickbooks_account import QuickbooksonlineAccount
from accounting_invoicing.quickbooks_online.entities.quickbooks_payment import QuickbooksonlinePayment
from accounting_invoicing.quickbooks_online.entities.quickbooks_purchase import QuickbooksonlinePurchase
from accounting_invoicing.quickbooks_online.entities.quickbooks_estimate import QuickbooksonlineEstimate
from accounting_invoicing.quickbooks_online.entities.quickbooks_customer import QuickbooksonlineCustomer
from accounting_invoicing.quickbooks_online.entities.quickbooks_sales_receipt import QuickbooksonlieSalesReceipt
from accounting_invoicing.quickbooks_online.entities.quickbooks_product_service import QuickbooksonlineProductService


class QuickbooksonlineApi:
    def accounts_mappings(self, accounts_data):
        accounts = []
        for account in accounts_data:
            account_obj = QuickbooksonlineAccount(
                account_id=account['Id'],
                name=account.get('Name'),
                full_qualified_name=account.get('FullyQualifiedName'),
                account_type=account.get('AccountType'),
                current_balance=account.get('CurrentBalance'),
                current_balance_with_sub_accounts=account.get(
                    'CurrentBalanceWithSubAccounts'),
                account_sub_type=account.get('AccountSubType'),
                currency=account.get('CurrencyRef').get('value'),
                is_active=account.get('Active')
            )
            accounts.append(account_obj.__dict__)
        return json.dumps(accounts)

    def account_by_name(self, context, payload):
        '''Get account by name'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/query?query=select * from Account where Name = '{payload['name']}' &minorversion=59"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['QueryResponse'].get('Account')
        return self.accounts_mappings(result)

    def customer_mappings(self, customer_date):
        customers = []
        for customer in customer_date:
            customer_obj = QuickbooksonlineCustomer(
                customer_id=customer['Id'],
                middle_name=customer.get('MiddleName'),
                full_name=customer.get('FullyQualifiedName'),
                display_name=customer.get('DisplayName'),
                title=customer.get('Title'),
                company=customer.get('CompanyName'),
                fax=customer.get('Fax').get(
                    'FreeFormNumber') if customer.get('Fax') else None,
                website=customer.get('WebAddr').get(
                    'URI') if customer.get('WebAddr') else None,
                billing_address_street=customer.get('BillAddr').get(
                    'Line1') if customer.get('BillAddr') else None,
                billing_address_zipcode=customer.get('BillAddr').get(
                    'PostalCode') if customer.get('BillAddr') else None,
                billing_address_country=customer.get('BillAddr').get(
                    'CountrySubDivisionCode') if customer.get('BillAddr') else None,
                mobile=customer.get('PrimaryPhone').get(
                    'FreeFormNumber') if customer.get('PrimaryPhone') else None,
                address_line1=customer.get('ShipAddr').get(
                    'Line1') if customer.get('ShipAddr') else None,
                address_zip_code=customer.get('ShipAddr').get(
                    'PostalCode') if customer.get('ShipAddr') else None,
                address_state_code=customer.get('ShipAddr').get(
                    'CountrySubDivisionCode') if customer.get('ShipAddr') else None,
                email=customer.get('PrimaryEmailAddr').get(
                    'Address') if customer.get('PrimaryEmailAddr') else None
            )
            customers.append(customer_obj.__dict__)
        return json.dumps(customers)

    def customer_by_email(self, context, payload):
        '''Get customer by email'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/query?query=select * from Customer where PrimaryEmailAddr = '{payload['email']}' &minorversion=59"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['QueryResponse'].get('Customer')
        return self.customer_mappings(result)

    def customer_by_name(self, context, payload):
        '''Get customer by name'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/query?query=select * from Customer where FullyQualifiedName = '{payload['name']}' &minorversion=59"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['QueryResponse'].get('Customer')
        return self.customer_mappings(result)

    def invoice(self, context, payload):
        '''get invoice by id'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/invoice/{payload['id']}"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['Invoice']
        invoice_data = QuickbooksonlineInvoice(
            invoice_id=result.get('Id'),
            customer_id=result.get('CustomerRef').get('value'),
            terms=result.get('SalesTermRef'),
            due_date=result.get('DueDate'),
            message_displayed_on_invoice=result.get("CustomerMemo").get(
                "value") if result.get("CustomerMemo") else None,
            message_displayed_on_statement=result.get('PrivateNote'),
            invoice_date=result.get('TxnDate'),
            bill_number=result.get('DocNumber')
        ).__dict__
        lines = []
        for line in result.get('Line'):
            if line.get('DetailType') == 'SalesItemLineDetail':
                line_details = {
                    'product_id': line['SalesItemLineDetail']['ItemRef']['value'] if line.get('SalesItemLineDetail') else None,
                    'product_description': line.get('Description'),
                    'product_amount': line.get('Amount'),
                    'product_tax': line.get('TaxCodeRef').get('value') if line.get('TaxCodeRef') else None
                }
                lines.append(line_details)
        invoice_data['products'] = lines
        return invoice_data

    def product_by_name(self, context, payload):
        '''get product by name'''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/query?query=select * from Item where Name = '{payload['name']}'&minorversion=59"
        response = util.rest("get", url, access_token)
        products_list = json.loads(response.text)['QueryResponse'].get('Item')
        products = []
        for product in products_list:
            product_obj = QuickbooksonlineProductService(
                product_id=product.get('Id'),
                sku=product.get('Sku'),
                product_type=product.get('Type'),
                name=product.get('Name'),
                income_account_type_id=product.get('IncomeAccountRef').get(
                    'value') if product.get('IncomeAccountRef') else None,
                expense_account_type_id=product.get('ExpenseAccountRef').get(
                    'value') if product.get('ExpenseAccountRef') else None,
                description_on_purchase_forms=product.get('PurchaseDesc'),
                cost=product.get('UnitPrice'),
                category_id=product.get('ParentRef').get(
                    'value') if product.get('ParentRef')else None,
                is_taxable=product.get('Taxable'),
                unit_price=product.get('UnitPrice')
            )
            products.append(product_obj.__dict__)
        return json.dumps(products)

    def vendor_by_name(self, context, payload):
        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/query?query=select * from vendor where DisplayName = '{payload['name']}'&minorversion=59"
        response = util.rest("get", url, access_token)
        vendor_list = json.loads(response.text)['QueryResponse'].get('Vendor')
        return self.vendor_mappings(vendor_list)

    def vendor_mappings(self, vendor_list):
        vendors = []
        for vendor in vendor_list:
            vendor_obj = QuickbooksonlineVendors(
                vendor_id=vendor.get('Id'),
                full_name=vendor.get('DisplayName'),
                phone=vendor.get('PrimaryPhone').get(
                    'FreeFormNumber') if vendor.get('PrimaryPhone') else None,
                email=vendor.get('PrimaryEmailAddr').get(
                    'Address') if vendor.get('PrimaryEmailAddr') else None,
                website=vendor.get('WebAddr').get(
                    'URI') if vendor.get('WebAddr')else None,
                address_line1=vendor.get('BillAddr').get(
                    'Line1') if vendor.get('BillAddr') else None,
                address_line2=vendor.get('BillAddr').get(
                    'Line2') if vendor.get('BillAddr') else None,
                address_city=vendor.get('BillAddr').get(
                    'City') if vendor.get('BillAddr') else None,
                address_state_code=vendor.get('BillAddr').get(
                    'PostalCode') if vendor.get('BillAddr') else None,
                address_zip_code=vendor.get('BillAddr').get(
                    'PostalCode') if vendor.get('BillAddr') else None,
            )
            vendors.append(vendor_obj.__dict__)
        return json.dumps(vendors)

    def customer(self, context, payload):
        '''get customer by id '''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/query?query=select * from Customer where Id = '{payload['id']}' &minorversion=59"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['QueryResponse'].get('Customer')
        return self.customer_mappings(result)

    def vendor(self, context, payload):
        '''get vendor by id '''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/query?query=select * from vendor where Id = '{payload['id']}'&minorversion=59"
        response = util.rest("get", url, access_token)
        vendor_list = json.loads(response.text)['QueryResponse'].get('Vendor')
        return self.vendor_mappings(vendor_list)

    def bill(self, context, payload):
        '''get bill by id '''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/bill/{payload['id']}"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['Bill']
        bill = QuickbooksonlineBill(
            bill_id=result['Id'],
            vendor_id=result['VendorRef']['value'] if result.get(
                'VendorRef') else None,
            transaction_date=result.get('TxnDate'),
            due_date=result.get('DueDate'),
            bill_number=result.get('DocNumber'),
            currency=result.get('CurrencyRef').get('value'),
            global_tax_calculation=result.get('GlobalTaxCalculation'),
            ap_account_id=result.get('APAccountRef').get(
                'value')if result.get('APAccountRef') else None,
            memo=result.get('PrivateNote')
        ).__dict__
        lines = []
        for line in result.get('Line'):
            if line.get('DetailType') == 'AccountBasedExpenseLineDetail':
                data = {
                    "line_item_description": line.get('Description'),
                    "line_item_amount": line.get('Amount'),
                    "line_tax": line.get('TaxCodeRef').get('value') if line.get('TaxCodeRef') else None,
                    "line_item_billable": line.get('BillableStatus'),
                    "line_item_customer_id": line.get('CustomerRef').get('value') if line.get('CustomerRef') else None,
                    "line_id": line.get('Id')
                }
                lines.append(data)
        bill['lines'] = lines
        return bill

    def estimate(self, context, payload):
        '''get estimate by id '''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/estimate/{payload['id']}"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['Estimate']
        estimate = QuickbooksonlineEstimate(
            customer_id=result.get('CustomerRef').get(
                'value') if result.get('CustomerRef') else None,
            expiration_date=result.get('ExpirationDate'),
            message_displayed_on_estimate=result.get('CustomerMemo').get(
                'value') if result.get('CustomerMemo') else None
        ).__dict__
        lines = []
        for line in result.get('Line'):
            if line.get('DetailType') == 'SalesItemLineDetail':
                data = {
                    'line_amount': line.get('Amount'),
                    'line_decription': line.get('Description'),
                    'line_item': line.get('ItemRef').get('value') if line.get('ItemRef') else None,
                    'Payment': line.get('TaxCodeRef').get('value') if line.get('TaxCodeRef') else None
                }
                lines.append(data)
        estimate['lines'] = lines
        return estimate

    def payment(self, context, payload):
        '''get payment by id '''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/payment/{payload['id']}"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['Payment']
        payment = QuickbooksonlinePayment(
            customer_id=result.get('CustomerRef').get('value'),
            total_amount=result.get('TotalAmt'),
            memo=result.get('PrivateNote'),
            unapplied_amount=result.get('UnappliedAmt'),
            transaction_date=result.get('TxnDate'),
            line_amount=result.get('Line')[0]['Amount'],
            line_linked_invoice_id=result.get(
                'Line')[0]['LinkedTxn'][0]['TxnId']
        ).__dict__
        return payment

    def purchase_order(self, context, payload):
        '''get purchase order by id '''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/purchaseorder/{payload['id']}"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['PurchaseOrder']
        purchase = QuickbooksonlinePurchase(
            purchase_id=result.get('Id'),
            vendor_id=result.get('VendorRef').get('value'),
            purchase_order_date=result.get('TxnDate'),
            purchase_order_number=result.get('DocNumber'),
            product_id=result.get(
                'Line')[0]['ItemBasedExpenseLineDetail']['ItemRef']['value'],
            product_description=result.get(
                'Line')[0]['ItemBasedExpenseLineDetail'].get('Description'),
            product_quantity=result.get(
                'Line')[0]['ItemBasedExpenseLineDetail'].get('Qty'),
            product_rate=result.get(
                'Line')[0]['ItemBasedExpenseLineDetail'].get('UnitPrice'),
            product_amount=result.get(
                'Line')[0]['ItemBasedExpenseLineDetail'].get('Amount'),
            your_message_to_vendor=result.get('PrivateNote'),
            memo=result.get('Memo'),
        ).__dict__
        return purchase

    def sales_receipt(self, context, payload):
        '''get sales receipt by id '''

        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}/salesreceipt/{payload['id']}"
        response = util.rest("get", url, access_token)
        result = json.loads(response.text)['SalesReceipt']
        receipt = QuickbooksonlieSalesReceipt(
            sale_receipt_id=result.get('Id'),
            transaction_date=result.get('TxnDate'),
            sales_receipt_number=result.get('DocNumber')
        ).__dict__
        lines = []
        for line in result.get('Line'):
            if line.get('DetailType') == 'SalesItemLineDetail':
                data = {
                    'line_item_quantity': line.get('Qty'),
                    'line_item_unit_price': line.get('UnitPrice'),
                    'line_item_tax_code': line.get('TaxCodeRef').get('value') if line.get('TaxCodeRef') else None,
                    'line_amount': line.get('Amount'),
                    'line_decription': line.get('Description'),
                    'product_id': line.get('ItemRef').get('value') if line.get('ItemRef') else None,
                }
                lines.append(data)
        receipt['lines'] = lines
        return receipt
    
    def profile(self, context, payload):
        headers = context['headers']
        access_token = util.get_access_token(headers)
        url = f"v3/company/{headers['realm_id']}query?query=select * from CompanyInfo"
        response_data = util.rest("get", url, access_token)
        response = response_data.json()['QueryResponse'].get('CompanyInfo')[0]
        profile = {
            'id':response['Id'],
            'email':response['Email'].get('Address'),
            'name':response['LegalName']
        }

        return profile