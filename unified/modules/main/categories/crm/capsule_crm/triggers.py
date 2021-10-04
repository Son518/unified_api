from unified.core.triggers import Triggers
from crm.capsule_crm.api import CapsulecrmApi
import json


class CapsulecrmTriggers(Triggers):

    def new_contact(self, context, payload):
        '''Triggers when new contact is added '''

        webhook_response = payload['payload']

        return json.loads(CapsulecrmApi().party_mappings(webhook_response))[0]

    def new_opportunity(self, context, payload):
        '''Triggers when new opportunity is added '''

        return self.new_deal(context, payload)

    def new_deal(self, context, payload):
        '''Triggers when new Deal is added '''

        webhook_response = payload['payload']

        return json.loads(CapsulecrmApi().opportunity_mappings(webhook_response))[0]

    def new_case(self, context, payload):
        '''Triggers when new Case is added '''

        webhook_response = payload['payload']

        return json.loads(CapsulecrmApi().case_mapping(webhook_response))[0]

    def contact_updated(self, context, payload):
        '''Triggers when Contact is Updated added '''

        return self.new_contact(context, payload)

    def case_updated(self, context, payload):
        '''Triggers when case is Updated added '''

        return self.new_case(context, payload)

    def opportunity_updated(self, context, payload):
        '''Triggers when opportunity is Updated added '''

        return self.new_opportunity(context, payload)

    def new_task(self, context, payload):
        '''Triggers when new task added '''

        webhook_response = payload['payload']
        
        return json.loads(CapsulecrmApi().task_mapping(webhook_response))[0]

    def task_updated(self, context, payload):
        '''Triggers when task is Updated added '''

        return self.new_task(context, payload)
