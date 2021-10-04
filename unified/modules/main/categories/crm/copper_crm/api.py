import json
from crm.copper_crm import util
from crm.copper_crm.entities.copper_task import CoppercrmTask
from crm.entities.contact import Contact
from crm.entities.lead import Lead
from crm.entities.deal import Deal
from crm.copper_crm.entities.copper_account import CoppercrmAccount


class CoppercrmApi:

    def task(self, context, params):
        '''Get task by specific task id'''

        headers = context['headers']
        url = f'tasks/{params["id"]}'

        task = json.loads(
            util.rest("GET", url, headers).text)

        task_obj = CoppercrmTask(
            task_id=task.get('id'),
            due_date=task.get('due_date'),
            description=task.get('details'),
            status=task.get('status'),
            project_id=task.get('related_resource').get(
                'id') if task.get('related_resource') else None,
            owner_id=task.get('assignee_id'),
            priority_id=task.get('priority'),
            name=task.get('name')
        )

        return task_obj.__dict__

    def tasks(self, context, params):
        '''Get list of tasks'''

        headers = context['headers']
        url = 'tasks/search'
        list_task_body = {
            "page_size": 25,
            "sort_by": "name"
        }
        task_list = json.loads(
            util.rest("POST", url, headers, list_task_body).text)
        tasks = []
        for task in task_list:
            task_obj = CoppercrmTask(
                task_id=task.get('id'),
                due_date=task.get('due_date'),
                description=task.get('details'),
                status=task.get('status'),
                project_id=task.get('related_resource').get(
                    'id') if task.get('related_resource') else None,
                owner_id=task.get('assignee_id'),
                priority_id=task.get('priority'),
                name=task.get('name')
            )
            tasks.append(task_obj.__dict__)

        return json.dumps(tasks)

    def contacts(self, context, params):
        '''Get list of tasks'''

        headers = context['headers']
        url = 'people/search'
        list_contact_body = {
            "page_size": 25,
            "sort_by": "name"
        }
        contact_list = json.loads(
            util.rest("POST", url, headers, list_contact_body).text)
        contacts = []
        for contact in contact_list:
            contact_obj = Contact(
                contact_id=contact.get('id'),
                first_name=contact.get('first_name'),
                last_name=contact.get('last_name'),
                email=contact.get('emails')[0].get(
                    'email') if contact.get('emails') else None,
                business_phone=contact.get('phone_numbers')[0].get(
                    'number') if contact.get('phone_numbers') else None,
                mailing_city=contact.get('address').get(
                    'city') if contact.get('address') else None,
                mailing_country=contact.get('address').get(
                    'country') if contact.get('address') else None,
                mailing_state=contact.get('address').get(
                    'state') if contact.get('address') else None,
                mailing_zip=contact.get('address').get(
                    'postal_code') if contact.get('address') else None,
                description=contact.get(
                    'details') if contact.get('details') else None
            )
            contacts.append(contact_obj.__dict__)

        return json.dumps(contacts)

    def contact(self, context, params):
        '''Get contact by contact Id'''

        headers = context['headers']
        url = f'people/{params["id"]}'
        contact = json.loads(
            util.rest("GET", url, headers).text)

        contact_obj = Contact(
            contact_id=contact.get('id'),
            first_name=contact.get('first_name'),
            last_name=contact.get('last_name'),
            email=contact.get('emails')[0].get(
                'email') if contact.get('emails') else None,
            business_phone=contact.get('phone_numbers')[0].get(
                'number') if contact.get('phone_numbers') else None,
            mailing_city=contact.get('address').get(
                'city') if contact.get('address') else None,
            mailing_country=contact.get('address').get(
                'country') if contact.get('address') else None,
            mailing_state=contact.get('address').get(
                'state') if contact.get('address') else None,
            mailing_zip=contact.get('address').get(
                'postal_code') if contact.get('address') else None,
            description=contact.get(
                'details') if contact.get('details') else None
        )
        return contact_obj.__dict__

    def contact_by_email(self, context, params):
        '''Get contact by email '''

        headers = context['headers']
        url = 'people/fetch_by_email'
        body = {
            "email": params['email']
        }
        contact = json.loads(
            util.rest("POST", url, headers, body).text)

        contact_obj = Contact(
            contact_id=contact.get('id'),
            first_name=contact.get('first_name'),
            last_name=contact.get('last_name'),
            email=contact.get('emails')[0].get(
                'email') if contact.get('emails') else None,
            business_phone=contact.get('phone_numbers')[0].get(
                'number') if contact.get('phone_numbers') else None,
            mailing_city=contact.get('address').get(
                'city') if contact.get('address') else None,
            mailing_country=contact.get('address').get(
                'country') if contact.get('address') else None,
            mailing_state=contact.get('address').get(
                'state') if contact.get('address') else None,
            mailing_zip=contact.get('address').get(
                'postal_code') if contact.get('address') else None,
            description=contact.get(
                'details') if contact.get('details') else None
        )
        return contact_obj.__dict__

    def contact_by_name(self, context, params):
        '''Get contact by Name '''

        headers = context['headers']
        url = 'people/search'
        list_contact_body = {
            "page_size": 25,
            "sort_by": "name",
            "name": params['name']
        }
        contact_list = json.loads(
            util.rest("POST", url, headers, list_contact_body).text)

        contacts = []

        for contact in contact_list:
            contact_obj = Contact(
                contact_id=contact.get('id'),
                first_name=contact.get('first_name'),
                last_name=contact.get('last_name'),
                email=contact.get('emails')[0].get(
                    'email') if contact.get('emails') else None,
                business_phone=contact.get('phone_numbers')[0].get(
                    'number') if contact.get('phone_numbers') else None,
                mailing_city=contact.get('address').get(
                    'city') if contact.get('address') else None,
                mailing_country=contact.get('address').get(
                    'country') if contact.get('address') else None,
                mailing_state=contact.get('address').get(
                    'state') if contact.get('address') else None,
                mailing_zip=contact.get('address').get(
                    'postal_code') if contact.get('address') else None,
                description=contact.get(
                    'details') if contact.get('details') else None
            )
            contacts.append(contact_obj.__dict__)
        return json.dumps(contacts)

    def contacts_by_phone(self, context, params):
        '''Get contact by Phone Number'''

        headers = context['headers']
        url = 'people/search'
        list_contact_body = {
            "page_size": 25,
            "sort_by": "name",
            "phone_number": params['phone_number']
        }
        contact_list = json.loads(
            util.rest("POST", url, headers, list_contact_body).text)

        contacts = []

        for contact in contact_list:
            contact_obj = Contact(
                contact_id=contact.get('id'),
                first_name=contact.get('first_name'),
                last_name=contact.get('last_name'),
                email=contact.get('emails')[0].get(
                    'email') if contact.get('emails') else None,
                business_phone=contact.get('phone_numbers')[0].get(
                    'number') if contact.get('phone_numbers') else None,
                mailing_city=contact.get('address').get(
                    'city') if contact.get('address') else None,
                mailing_country=contact.get('address').get(
                    'country') if contact.get('address') else None,
                mailing_state=contact.get('address').get(
                    'state') if contact.get('address') else None,
                mailing_zip=contact.get('address').get(
                    'postal_code') if contact.get('address') else None,
                description=contact.get(
                    'details') if contact.get('details') else None
            )
            contacts.append(contact_obj.__dict__)
        return json.dumps(contacts)

    def lead(self, context, params):
        '''Get specific lead by id'''

        headers = context['headers']
        url = f'leads/{params["id"]}'

        lead = json.loads(util.rest("GET", url, headers).text)

        lead_obj = Lead(
            lead_id=lead.get('id'),
            first_name=lead.get('first_name'),
            last_name=lead.get('last_name'),
            email=lead.get('email'),
            phone=lead.get('phone_numbers')[0].get(
                'number') if lead.get('phone_numbers') else None,
            city=lead.get('address').get(
                'city') if lead.get('address') else None,
            country_id=lead.get('address').get(
                'country') if lead.get('address') else None,
            state=lead.get('address').get(
                'state') if lead.get('address') else None,
            zip=lead.get('address').get(
                'postal_code') if lead.get('address') else None,
            description=lead.get('details') if lead.get('details') else None,
            title=lead.get('title')
        )

        return lead_obj.__dict__

    def leads(self, context, params):
        ''' Get list of leads'''

        headers = context['headers']
        url = 'leads/search'
        list_lead_body = {
            "page_size": 25,
            "sort_by": "name"
        }
        lead_list = json.loads(
            util.rest("POST", url, headers, list_lead_body).text)
        leads = []

        for lead in lead_list:
            lead_obj = Lead(
                lead_id=lead.get('id'),
                first_name=lead.get('first_name'),
                last_name=lead.get('last_name'),
                email=lead.get('email'),
                phone=lead.get('phone_numbers')[0].get(
                    'number') if lead.get('phone_numbers') else None,
                city=lead.get('address').get(
                    'city') if lead.get('address') else None,
                country_id=lead.get('address').get(
                    'country') if lead.get('address') else None,
                state=lead.get('address').get(
                    'state') if lead.get('address') else None,
                zip=lead.get('address').get(
                    'postal_code') if lead.get('address') else None,
                description=lead.get('details') if lead.get(
                    'details') else None,
                title=lead.get('title')
            )
            leads.append(lead_obj.__dict__)

        return json.dumps(leads)

    def deals(self, context, params):
        '''get list of deals'''

        headers = context['headers']
        url = 'opportunities/search'
        list_contact_body = {
            "page_size": 25,
            "sort_by": "name"
        }
        deal_list = json.loads(
            util.rest("POST", url, headers, list_contact_body).text)
        deals = []

        for deal in deal_list:
            deal_obj = Deal(
                deal_id=deal.get('id'),
                name=deal.get('name'),
                close_date=deal.get('close_date'),
                description=deal.get('details'),
                stage_id=deal.get('pipeline_id'),
                value=deal.get('monetary_value'),
                probability=deal.get('win_probability'),
                contact_id=deal.get('customer_source_id')
            )
            deals.append(deal_obj.__dict__)
        return json.dumps(deals)

    def deal(self, context, params):
        '''get deal by id'''

        headers = context['headers']
        url = f'opportunities/{params["deal_id"]}'
        deal = json.loads(util.rest("GET", url, headers).text)
        deal_obj = Deal(
            deal_id=deal.get('id'),
            name=deal.get('name'),
            close_date=deal.get('close_date'),
            description=deal.get('details'),
            stage_id=deal.get('pipeline_id'),
            value=deal.get('monetary_value'),
            probability=deal.get('win_probability'),
            contact_id=deal.get('customer_source_id')
        )
        return deal_obj.__dict__

    def deal_by_name(self, context, params):
        '''get deal by name'''

        headers = context['headers']
        url = 'opportunities/search'
        list_contact_body = {
            "name": params['name']
        }
        deal_list = json.loads(
            util.rest("POST", url, headers, list_contact_body).text)
        deals = []

        for deal in deal_list:
            deal_obj = Deal(
                deal_id=deal.get('id'),
                name=deal.get('name'),
                close_date=deal.get('close_date'),
                description=deal.get('details'),
                stage_id=deal.get('pipeline_id'),
                value=deal.get('monetary_value'),
                probability=deal.get('win_probability'),
                contact_id=deal.get('customer_source_id')
            )
            deals.append(deal_obj.__dict__)
        return json.dumps(deals)

    def companies(self, context, params):
        '''Get list of compines '''

        return self.accounts(context, params)

    def accounts(self, context, params):
        '''Get list of accounts'''

        headers = context['headers']
        url = 'companies/search'
        list_account_body = {
            "page_size": 25,
            "sort_by": "name"
        }
        account_list = json.loads(
            util.rest("POST", url, headers, list_account_body).text)
        accounts = []
        for account in account_list:
            account_obj = CoppercrmAccount(
                account_id=account.get('id'),
                name=account.get('name'),
                mailing_city=account.get('address').get(
                    'city') if account.get('address') else None,
                mailing_country=account.get('address').get(
                    'country') if account.get('address') else None,
                mailing_state=account.get('address').get(
                    'state') if account.get('address') else None,
                mailing_zip=account.get('address').get(
                    'postal_code') if account.get('address') else None,
                mailing_street=account.get('address').get(
                    'street') if account.get('address') else None,
                description=account.get('details'),
                email_domain=account.get('email_domain'),
                owner_id=account.get('assignee_id'),
                phone=account.get('phone_numbers')[0].get(
                    'number') if account.get('phone_numbers') else None
            )
            accounts.append(account_obj.__dict__)

        return json.dumps(accounts)

    def company(self, context, params):
        '''Get company by id'''

        return self.account(context, params)

    def account(self, context, params):
        '''get account by id'''

        headers = context['headers']
        url = f'companies/{params["account_id"]}'

        account = json.loads(util.rest("GET", url, headers).text)
        account_obj = CoppercrmAccount(
            account_id=account.get('id'),
            name=account.get('name'),
            mailing_city=account.get('address').get(
                'city') if account.get('address') else None,
            mailing_country=account.get('address').get(
                'country') if account.get('address') else None,
            mailing_state=account.get('address').get(
                'state') if account.get('address') else None,
            mailing_zip=account.get('address').get(
                'postal_code') if account.get('address') else None,
            mailing_street=account.get('address').get(
                'street') if account.get('address') else None,
            description=account.get('details'),
            email_domain=account.get('email_domain'),
            owner_id=account.get('assignee_id'),
            phone=account.get('phone_numbers')[0].get(
                'number') if account.get('phone_numbers') else None
        )

        return account_obj.__dict__

    def company_by_name(self, context, params):
        '''Get company by name'''
        return self.account_by_name(context, params)

    def account_by_name(self, context, params):
        '''Get account by name'''
        headers = context['headers']
        url = f'companies/search'
        body = {
            "page_size": 25,
            "sort_by": "name",
            "name": params['account_by_name']
        }
        account_list = json.loads(
            util.rest("POST", url, headers, body).text)
        accounts = []
        for account in account_list:
            account_obj = CoppercrmAccount(
                account_id=account.get('id'),
                name=account.get('name'),
                mailing_city=account.get('address').get(
                    'city') if account.get('address') else None,
                mailing_country=account.get('address').get(
                    'country') if account.get('address') else None,
                mailing_state=account.get('address').get(
                    'state') if account.get('address') else None,
                mailing_zip=account.get('address').get(
                    'postal_code') if account.get('address') else None,
                mailing_street=account.get('address').get(
                    'street') if account.get('address') else None,
                description=account.get('details'),
                email_domain=account.get('email_domain'),
                owner_id=account.get('assignee_id'),
                phone=account.get('phone_numbers')[0].get(
                    'number') if account.get('phone_numbers') else None
            )
            accounts.append(account_obj.__dict__)

        return json.dumps(accounts)

    def verify(self, context, params):
        """Verify Authentication information."""

        headers = context['headers']
        url = f'account'

        response = util.rest("GET", url, headers)
        result = json.loads(response.text)

        if 'error' in result:
            return '', response.status_code
        else:
            return json.dumps(result)
    
    def profile(self, context, params):
        '''Details of authenticated user'''

        headers = context['headers']
        url = 'account'
        response = util.rest("GET", url, headers)
        if not response.ok:
            return {'status':'invalid details'}, response.status_code
        else:
            result = response.json()
            result['email'] = headers['email']
            return result