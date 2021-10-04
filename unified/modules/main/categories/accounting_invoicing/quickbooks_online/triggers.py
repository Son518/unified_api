from unified.core.triggers import Triggers
from accounting_invoicing.quickbooks_online.api import QuickbooksonlineApi


class QuickbooksonlineTriggers(Triggers):
    def new_customer(self, context, payload):
        '''Triggered when you add a new customer.'''

        params = {
            'id': payload.get('eventNotifications')[0]['dataChangeEvent']['entities'][0]['id']
        }
        return QuickbooksonlineApi().customer(context, params)

    def updated_customer(self, context, payload):
        '''Triggered when an existing customer is updated.'''
        
        return self.new_customer(context, payload)

    def new_invoice(self, context, payload):
        '''Triggered when you add a new invoice.'''

        params = {
            'id': payload.get('eventNotifications')[0]['dataChangeEvent']['entities'][0]['id']
        }
        return QuickbooksonlineApi().invoice(context, params)

    def new_vendor(self, context, payload):
        '''Triggered when you add a new vendor.'''

        params = {
            'id': payload.get('eventNotifications')[0]['dataChangeEvent']['entities'][0]['id']
        }
        return QuickbooksonlineApi().vendor(context, params)

    def new_bill(self, context, payload):
        '''Triggered when you add a new bill.'''

        params = {
            'id': payload.get('eventNotifications')[0]['dataChangeEvent']['entities'][0]['id']
        }
        return QuickbooksonlineApi().bill(context, params)

    def new_estimate(self, context, payload):
        '''Triggered when you add a new estimate.'''

        params = {
            'id': payload.get('eventNotifications')[0]['dataChangeEvent']['entities'][0]['id']
        }
        return QuickbooksonlineApi().estimate(context, params)

    def new_payment(self, context, payload):
        '''Triggered when you add a new payment.'''

        params = {
            'id': payload.get('eventNotifications')[0]['dataChangeEvent']['entities'][0]['id']
        }
        return QuickbooksonlineApi().payment(context, params)

    def new_purchase_order(self, context, payload):
        '''Triggered when you add a new purchase order.'''

        params = {
            'id': payload.get('eventNotifications')[0]['dataChangeEvent']['entities'][0]['id']
        }
        return QuickbooksonlineApi().purchase_order(context, params)

    def new_sales_receipt(self, context, payload):
        '''Triggered when you add a new sales receipt.'''

        params = {
            'id': payload.get('eventNotifications')[0]['dataChangeEvent']['entities'][0]['id']
        }
        return QuickbooksonlineApi().purchase_order(context, params)
