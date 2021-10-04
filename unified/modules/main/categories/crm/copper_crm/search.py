from crm.entities.contact import Contact
from crm.copper_crm import util
import json
from crm.copper_crm.entities.copper_task import CoppercrmTask
from crm.copper_crm.entities.copper_account import CoppercrmAccount
from crm.entities.lead import Lead
from crm.entities.deal import Deal


class CoppercrmSearch:

    def new_contacts_by_date_range(self, context, params):
        '''Get list of contact between date ranges '''

        headers = context['headers']
        url = 'people/search'
        list_contact_body = {
            "page_size": 25,
            "sort_by": "name",
            "minimum_created_date": params['contacts_created_by_start_date_time'],
            "maximum_created_date": params['contacts_created_by_end_date_time']
        }
        contact_list = json.loads(
            util.rest("POST", url, headers, list_contact_body).text)

        if type(contact_list) is dict:
            return contact_list

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

    def new_tasks_by_date_range(self, context, params):
        '''Get list of tasks between date ranges '''

        headers = context['headers']
        url = 'tasks/search'
        list_task_body = {
            "page_size": 25,
            "sort_by": "name",
            "minimum_created_date": params['tasks_created_by_start_date_time'],
            "maximum_created_date": params['tasks_created_by_end_date_time']
        }
        task_list = json.loads(
            util.rest("POST", url, headers, list_task_body).text)

        if type(task_list) is dict:
            return task_list

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

    def new_leads_by_date_range(self, context, params):
        '''Get list of leads between date ranges '''

        headers = context['headers']
        url = 'leads/search'
        list_lead_body = {
            "page_size": 25,
            "sort_by": "name",
            "minimum_created_date": params['leads_created_by_start_date_time'],
            "maximum_created_date": params['leads_created_by_end_date_time']
        }
        lead_list = json.loads(
            util.rest("POST", url, headers, list_lead_body).text)

        if type(lead_list) is dict:
            return lead_list

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

    def new_deals_by_date_range(self, context, params):
        '''Get list of Deals between date ranges '''

        headers = context['headers']
        url = 'opportunities/search'
        list_contact_body = {
            "page_size": 25,
            "sort_by": "name",
            "minimum_created_date": params['deals_created_by_start_date_time'],
            "maximum_created_date": params['deals_created_by_end_date_time']
        }
        deal_list = json.loads(
            util.rest("POST", url, headers, list_contact_body).text)

        if type(deal_list) is dict:
            return deal_list

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

    def new_accounts_by_date_range(self, context, params):
        '''Get list of accounts between date ranges '''

        headers = context['headers']
        url = 'companies/search'
        list_account_body = {
            "page_size": 25,
            "sort_by": "name",
            "minimum_created_date": params['accounts_created_by_start_date_time'],
            "maximum_created_date": params['accounts_created_by_end_date_time']
        }
        account_list = json.loads(
            util.rest("POST", url, headers, list_account_body).text)

        if type(account_list) is dict:
            return account_list

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