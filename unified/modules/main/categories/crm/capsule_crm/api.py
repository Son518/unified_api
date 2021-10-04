from crm.capsule_crm import util
from crm.capsule_crm.entities.capsulecrm_contact import CapsulecrmContact
from crm.capsule_crm.entities.capsulecrm_deal import CapsulecrmDeal
from crm.capsule_crm.entities.capsulecrm_case import CapsulecrmCase
from crm.capsule_crm.entities.capsulecrm_tag import CapsulecrmTag
from crm.capsule_crm.entities.capsulecrm_task import CapsulecrmTask
import json


class CapsulecrmApi:
    def contacts(self, context, params):
        '''List of contacts'''
        
        return self.parties(context, params)

    def parties(self, context, params):
        '''List of parties'''

        access_token = util.get_access_token(context['headers'])
        url = "parties"
        respose_obj = util.rest("GET", url, access_token)
        parties_list = json.loads(respose_obj.text)['parties']
        return self.party_mappings(parties_list), respose_obj.status_code

    def party_mappings(self, parties_list):
        # Unifies party response

        parties = []
        for party in parties_list:
            party_obj = CapsulecrmContact(
                party_id=party['id'],
                account_id=party.get('organisation').get(
                    'id') if party.get('organisation') else None,
                first_name=party.get('firstName'),
                last_name=party.get('lastName'),
                email=party.get('emailAddresses')[0].get(
                    'address') if party.get('emailAddresses') else None,
                business_phone=party.get('phoneNumbers')[0].get(
                    'phoneNumbers') if party.get('phoneNumbers') else None,
                owner_id=party.get('owner'),
                mailing_city=party.get('addresses')[0].get(
                    'city') if party.get('addresses') else None,
                mailing_country=party.get('addresses')[0].get(
                    'country') if party.get('addresses') else None,
                mailing_state=party.get('addresses')[0].get(
                    'state') if party.get('addresses') else None,
                mailing_street=party.get('addresses')[0].get(
                    'street') if party.get('addresses') else None,
                mailing_zip=party.get('addresses')[0].get(
                    'zip') if party.get('addresses') else None,
                title=party.get('title'),
                job_title=party.get('jobTitle'),
                website=party.get('websites')
            )
            parties.append(party_obj.__dict__)
        return json.dumps(parties)

    def contact(self, context, params):
        '''get details of contact'''

        return self.party(context, params)

    def party(self, context, params):
        '''get details of pary'''

        access_token = util.get_access_token(context['headers'])

        if params.get('id') is None or params.get('party_id') == '':
            raise Exception('Provide party id')

        url = f"parties/{int(params.get('id'))}"
        respose_obj = util.rest("GET", url, access_token)

        if respose_obj.status_code != 200:
            raise Exception('Check providied party id')

        party = json.loads(respose_obj.text)['party']
        party_obj = CapsulecrmContact(
            party_id=party['id'],
            account_id=party.get('organisation').get(
                'id') if party.get('organisation') else None,
            first_name=party.get('firstName'),
            last_name=party.get('lastName'),
            email=party.get('emailAddresses')[0].get(
                'address') if party.get('emailAddresses') else None,
            business_phone=party.get('phoneNumbers')[0].get(
                'phoneNumbers') if party.get('phoneNumbers') else None,
            owner_id=party.get('owner'),
            mailing_city=party.get('addresses')[0].get(
                'city') if party.get('addresses') else None,
            mailing_country=party.get('addresses')[0].get(
                'country') if party.get('addresses') else None,
            mailing_state=party.get('addresses')[0].get(
                'state') if party.get('addresses') else None,
            mailing_street=party.get('addresses')[0].get(
                'street') if party.get('addresses') else None,
            mailing_zip=party.get('addresses')[0].get(
                'zip') if party.get('addresses') else None,
            title=party.get('title'),
            job_title=party.get('jobTitle'),
            website=party.get('websites')
        )

        return party_obj.__dict__, respose_obj.status_code

    def party_by_name(self, context, params):
        '''get details of party by name'''

        access_token = util.get_access_token(context['headers'])

        if params.get('name') is None or params.get('name') == '':
            raise Exception('Provide name')

        url = f"parties/search?q={params.get('name')}"
        respose_obj = util.rest("GET", url, access_token)

        if respose_obj.status_code != 200:
            raise Exception('Check providied name')

        parties_list = json.loads(respose_obj.text)['parties']
        return self.party_mappings(parties_list), respose_obj.status_code

    def party_by_email(self, context, params):
        '''get details of party by Email'''

        access_token = util.get_access_token(context['headers'])

        if params.get('email') is None or params.get('email') == '':
            raise Exception('Provide email')

        url = f"parties/search?q={params.get('email')}"
        respose_obj = util.rest("GET", url, access_token)

        if respose_obj.status_code != 200:
            raise Exception('Check providied Email')

        parties_list = json.loads(respose_obj.text)['parties']
        return self.party_mappings(parties_list), respose_obj.status_code

    def cases(self, context, params):
        '''List of cases'''

        access_token = util.get_access_token(context['headers'])
        activity = "kases"
        respose_obj = util.rest("GET", activity, access_token)
        cases_list = json.loads(respose_obj.text)['kases']
        return self.case_mapping(cases_list), respose_obj.status_code

    def case(self, context, params):
        '''get details of case'''

        access_token = util.get_access_token(context['headers'])

        if params.get('id') is None or params.get('id') == '':
            raise Exception('Provide case id')

        activity = f"kases/{params.get('id')}"
        respose_obj = util.rest("GET", activity, access_token)

        if respose_obj.status_code != 200:
            raise Exception('Check providied case id')

        case = []
        case.append(json.loads(respose_obj.text)['kase'])
        return self.case_mapping(case), respose_obj.status_code

    def case_mapping(self, case_list):
        # unifies case response'''

        cases = []
        for case in case_list:
            case_obj = CapsulecrmCase(
                case_id=case['id'],
                contact_id=case['party'].get(
                    'id') if case.get('party') else None,
                name=case.get('name'),
                description=case.get('description'),
                status=case.get('status'),
                owner_id=case['owner']['id']
            )
            cases.append(case_obj.__dict__)
        return json.dumps(cases)

    def opportunities(self, context, params):
        '''list of opportunities'''

        access_token = util.get_access_token(context['headers'])
        url = "opportunities"
        respose_obj = util.rest("GET", url, access_token)
        parties_list = json.loads(respose_obj.text)['opportunities']
        
        return self.opportunity_mappings(parties_list), respose_obj.status_code

    def opportunity(self, context, params):
        '''get opportunities details'''

        access_token = util.get_access_token(context['headers'])

        if params.get('opportunity_id') is None or params.get('opportunity_id') == '':
            raise Exception('Provide case id')

        url = f"opportunities/{params.get('opportunity_id')}"
        respose_obj = util.rest("GET", url, access_token)

        if respose_obj.status_code != 200:
            raise Exception('Check providied opportunity id')

        data = []
        data.append(json.loads(respose_obj.text)['opportunity'])
        
        return self.opportunity_mappings(data), respose_obj.status_code

    def opportunity_mappings(self, opportunities_list):
        # unifies opportunities response 

        opportunities = []
        for opportunity in opportunities_list:
            opportunity_obj = CapsulecrmDeal(
                deal_id=opportunity['id'],
                name=opportunity.get('name'),
                close_date=opportunity.get('expectedCloseOn'),
                description=opportunity.get('description'),
                stage_id=opportunity.get('milestone').get(
                    'id') if opportunity.get('milestone') else None,
                value=opportunity.get('value').get(
                    'amount') if opportunity.get('value') else None,
                probability=opportunity.get('probability'),
                owner_id=opportunity['owner'].get('id'),
                contact_id=opportunity['party'].get('id'),
                currency_id=opportunity['value'].get(
                    'currency') if opportunity.get('value') else None
            )
            opportunities.append(opportunity_obj.__dict__)
        return json.dumps(opportunities)

    def tags(self, context, params):
        '''list of tags in parties, opportunities and kases'''

        access_token = util.get_access_token(context['headers'])

        if params.get('entity') is None or params.get('entity') == '':
            raise Exception(
                'Provide required entity. Supported entites are parties, opportunities and kases')

        url = f"{params.get('entity')}/tags"
        respose_obj = util.rest("GET", url, access_token)

        if respose_obj.status_code != 200:
            raise Exception('Check providied entites')

        tag_list = json.loads(respose_obj.text)['tags']
        tags = []
        for tag in tag_list:
            tag_obj = CapsulecrmTag(
                tag_id=tag['id'],
                tag=tag.get('name'),
                description=tag.get('description')
            )
            tags.append(tag_obj.__dict__)
        
        return json.dumps(tags), respose_obj.status_code

    def tasks(self, context, params):
        '''list of tasks'''

        access_token = util.get_access_token(context['headers'])
        activity = "tasks"
        respose_obj = util.rest("GET", activity, access_token)
        task_list = json.loads(respose_obj.text)['tasks']
        
        return self.task_mapping(task_list), respose_obj.status_code

    def task_mapping(self, task_list):
        # unifies task response 

        tasks = []
        for task in task_list:
            task_obj = CapsulecrmTask(
                name=task.get('description'),
                description=task.get('detail'),
                category_id=task['category'].get(
                    'id') if task.get('category') else None,
                owner_id=task['owner'].get(
                    'id') if task.get('owner') else None,
                due_date=task.get('dueOn')
            )
            tasks.append(task_obj.__dict__)

        return json.dumps(tasks)

    def profile(self, context, payload):
        '''Details of authenticated user'''

        access_token = util.get_access_token(context['headers'])
        url = "users/current"
        response = util.rest("GET", url, access_token).json()['user']
        profile = {
            'id':response['id'],
            'name':response['username']
        }

        # party is contact
        party = response.get('party')
        if party:
            params = {
                "id":party.get('id')
            }
            email_obj = self.party(context, params)
            profile['email']=email_obj[0]['email']
        
        return profile