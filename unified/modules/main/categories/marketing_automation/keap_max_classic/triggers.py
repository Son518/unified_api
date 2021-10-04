from flask import request, Response
from marketing_automation.keap_max_classic import util
from unified.core.triggers import Triggers
import requests


class KeapMaxClassicTriggers(Triggers):
    def new_action_sequence(self, context, payload):
        '''Triggers when new action sequence is created'''

        pass

    def new_affiliate(self, context, payload):
        '''Triggers when new affiliate is created'''

        pass

    def new_company(self, context, payload):
        '''Triggers when new company is created'''

        pass

    def new_contact(self, context, payload):
        '''Triggers when new contact is created'''

        return {}

    def new_contact_action(self, context, payload):
        '''Triggers when new contact action is created'''

        pass

    def tag_added_to_contact(self, context, payload):
        '''Triggers when new tag is added to a contact'''

        pass

    def credit_card_change(self, context, payload):
        '''Triggers when credit card is changed'''

        pass

    def new_expense(self, context, payload):
        '''Triggers when new expense is created'''

        pass

    def new_invoice(self, context, payload):
        '''Triggers when new invoice is created'''

        pass

    def new_opportunity(self, context, payload):
        '''Triggers when new opportunity is created'''

        pass

    def new_payment(self, context, payload):
        '''Triggers when new payment is created'''

        pass

    def new_product(self, context, payload):
        '''Triggers when new product is created'''

        pass

    def new_subscription(self, context, payload):
        '''Triggers when new subscription is created'''

        pass

    def cancelled_subscription(self, context, payload):
        '''Triggers when subscription is cancelled'''

        pass

    def new_subscription_plan(self, context, payload):
        '''Triggers when new subscription plan is created'''

        pass

    def new_tag(self, context, payload):
        '''Triggers when new tag is created'''

        pass
