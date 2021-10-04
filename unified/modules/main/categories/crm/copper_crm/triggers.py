from unified.core.triggers import Triggers
from crm.copper_crm.api import CoppercrmApi


class CoppercrmTriggers(Triggers):
    def new_contact(self, context, payload):
        '''Triggers when a new Contact is created in Copper.'''

        headers = context['headers']
        params = {
            "id": payload['ids'][0]

        }
        return CoppercrmApi().contact(context, params)

    def new_opportunity(self, context, payload):
        '''Triggers when a new Opportunity is created in Copper.'''

        return self.new_deal(context, payload)

    def new_deal(self, context, payload):
        '''Triggers when a new Deal is created in Copper.'''

        headers = context['headers']
        params = {
            "deal_id": payload['ids'][0]

        }

        return CoppercrmApi().deal(context, params)

    def new_account(self, context, payload):
        '''Triggers when a new Account is created in Copper.'''

        return self.new_company(context, payload)

    def new_company(self, context, payload):
        '''Triggers when a new company is created in Copper.'''

        headers = context['headers']
        params = {
            "account_id": payload['ids'][0]

        }

        return CoppercrmApi().account(context, params)

    def new_lead(self, context, payload):
        '''Triggers when a new Lead is created in Copper.'''

        headers = context['headers']
        params = {
            "id": payload['ids'][0]

        }
        return CoppercrmApi().lead(context, params)

    def contact_updated(self, context, payload):
        '''Triggers when a Contact is changed.'''

        headers = context['headers']
        params = {
            "id": payload['ids'][0]

        }

        return CoppercrmApi().contact(context, params)

    def opportunity_updated(self, context, payload):
        '''Triggers when a Opportunity is changed.'''

        return self.new_deal(context, payload)

    def deal_updated(self, context, payload):
        '''Triggers when a Deal is changed.'''

        headers = context['headers']
        params = {
            "deal_id": payload['ids'][0]

        }

        return CoppercrmApi().deal(context, params)

    def account_updated(self, context, payload):
        '''Triggers when a account is changed.'''

        return self.new_company(context, payload)

    def company_updated(self, context, payload):
        '''Triggers when a company is changed.'''

        headers = context['headers']
        params = {
            "id": payload['ids'][0]

        }
        return CoppercrmApi().account(context, params)

    def opportunity_stage_updated(self, context, payload):
        '''Triggers when a opportunity stage is changed.'''

        return self.new_deal(context, payload)

    def deal_stage_updated(self, context, payload):
        '''Triggers when a Deal stage is changed.'''

        headers = context['headers']
        params = {
            "deal_id": payload['ids'][0]

        }
        return CoppercrmApi().deal(context, params)

    def new_task(self, context, payload):
        '''triggers when new task is created'''

        headers = context['headers']
        params = {
            "id": payload['ids'][0]

        }
        return CoppercrmApi().task(context, params)

    def task_updated(self, context, payload):
        '''Triggers when a Task is changed.'''

        headers = context['headers']
        params = {
            "id": payload['ids'][0]

        }
        return CoppercrmApi().task(context, params)

    def lead_updated(self, context, payload):
        '''Triggers when a Lead is changed.'''

        headers = context['headers']
        params = {
            "id": payload['ids'][0]

        }
        return CoppercrmApi().lead(context, params)

    def lead_status_updated(self, context, payload):
        '''Triggers when a Lead is changed.'''

        headers = context['headers']
        params = {
            "id": payload['ids'][0]

        }

        return CoppercrmApi().lead(context, params)
