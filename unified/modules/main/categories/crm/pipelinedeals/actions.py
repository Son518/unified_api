import json
from crm.pipelinedeals import util
from unified.core.actions import Actions
from crm.pipelinedeals.entities.pipelinedeals_activity import PipelinedealsActivity
from crm.pipelinedeals.entities.pipelinedeals_company import PipelinedealsCompany
from crm.pipelinedeals.entities.pipelinedeals_deal import PipelinedealsDeal
from crm.pipelinedeals.entities.pipelinedeals_event import PipelinedealsEvent
from crm.pipelinedeals.entities.pipelinedeals_person import PipelinedealsPerson
from crm.pipelinedeals.entities.pipelinedeals_task import PipelinedealsTask

class PipelinedealsActions:

    def create_activity(self, context, payload):
        '''Creates a activity.'''
        activity_entity = PipelinedealsActivity(**payload)
        endpoint = 'notes'
        data = {
                "note": 
                    {
                    "content": activity_entity.content,
                    "deal_id": activity_entity.deal_id,
                    "company_id": activity_entity.company_id,
                    "person_id": activity_entity.person_id,
                }
            }
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)

    def create_company(self, context, payload):
        '''Creates a company.'''
        company_entity = PipelinedealsCompany(**payload)
        endpoint = 'companies'
        data = {
                "company": 
                        {
                        "name": company_entity.name,
                        "phone1": company_entity.phone,
                        "web": company_entity.website,
                        "email": company_entity.email,
                        "company": company_entity.company,
                        "address_1": company_entity.address,
                        "city": company_entity.city,
                        "state": company_entity.state,
                        "postal_code": company_entity.postal_code,
                        "country": company_entity.country,
                        "region_id": company_entity.region_id,
                        "industry_id": company_entity.industry_id
                        }
                    }
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)

    def create_deal(self, context, payload):
        '''Creates a deal.'''
        deal_entity = PipelinedealsDeal(**payload)
        endpoint = 'deals'
        data = {
                "deal": 
                        {
                        "name": deal_entity.name,
                        "expected_close_date": deal_entity.expected_close_date,
                        "company_name": deal_entity.company_name,
                        "primary_contact_id": deal_entity.primary_contact_id,
                        "status": deal_entity.status,
                        "value": deal_entity.value,
                        "stage_id": deal_entity.stage_id,
                        "source_id": deal_entity.source_id,
                        "product_interest_id": deal_entity.product_interest_id
                    }
                }
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)

    def create_event(self, context, payload):
        '''Creates a event.'''
        event_entity = PipelinedealsEvent(**payload)
        endpoint = 'calendar_entries'
        data = {
                "calendar_entry": {
                                "name": event_entity.name,
                                "description": event_entity.description,
                                "association_type": event_entity.association_type,
                                "association_id": event_entity.association_id,
                                "start_time": event_entity.start_time,
                                "end_time": event_entity.end_time,
                                "category_id": event_entity.category_id,
                                "type": event_entity.type
                                }
                            }
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)
    
    def create_person(self, context, payload):
        '''Creates a person.'''
        person_entity = PipelinedealsPerson(**payload)
        endpoint = 'people'
        data = {
                "person": {
                            "first_name": person_entity.first_name,
                            "last_name": person_entity.last_name,
                            "mobile": person_entity.mobile,
                            "phone": person_entity.phone,
                            "position": person_entity.position,
                            "website": person_entity.website,
                            "email": person_entity.email,
                            "company_name": person_entity.company,
                            "type": person_entity.type,
                            "work_address_1": person_entity.work_address,
                            "work_city": person_entity.work_city,
                            "work_state": person_entity.work_state,
                            "work_postal_code": person_entity.work_postal_code,
                            "work_country": person_entity.work_country,
                            "home_address_1": person_entity.home_address,
                            "home_city": person_entity.home_city,
                            "home_state": person_entity.home_state,
                            "home_country": person_entity.home_country,
                            "home_postal_code": person_entity.home_postal_code,
                            "lead_status_id": person_entity.status_id,
                            "lead_source_id": person_entity.source_id,
                            "summary": person_entity.summary,
                            "facebook_url": person_entity.facebook_url,
                            "linked_in_url": person_entity.linkedin_url,
                            "twitter": person_entity.twitter_username
                        }
                    }
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)

    def create_task(self, context, payload):
        '''Creates a task.'''
        task_entity = PipelinedealsTask(**payload)
        endpoint = 'calendar_entries'
        data = {
                "calendar_entry": {
                                    "name": task_entity.name,
                                    "description": task_entity.description,
                                    "due_date": task_entity.due_date,
                                    "association_type": task_entity.association_type,
                                    "category_id": task_entity.category_id,
                                    "type": task_entity.type
                                }
                            }
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)

    def update_company(self, context, payload):
        '''Updates a company detailes.'''
        company_entity = PipelinedealsCompany(**payload)
        endpoint = 'companies'
        data = {
                "company": 
                        {
                        "company_id": company_entity.company_id,
                        "name": company_entity.name,
                        "phone1": company_entity.phone,
                        "web": company_entity.website,
                        "email": company_entity.email,
                        "address_1": company_entity.address,
                        "city": company_entity.city,
                        "state": company_entity.state,
                        "postal_code": company_entity.postal_code,
                        "country": company_entity.country,
                        "region_id": company_entity.region_id,
                        "industry_id": company_entity.industry_id
                        }
                    }
        response = util.rest("PUT",endpoint,context['headers']['api_key'],data,company_entity.company_id)
        return json.loads(response.text)
        
    def update_deal(self, context, payload):
        '''Updatess a deal.'''
        deal_entity = PipelinedealsDeal(**payload)
        endpoint = 'deals'
        data = {
                "deal": 
                        {
                        "deal_id": deal_entity.deal_id,
                        "name": deal_entity.name,
                        "expected_close_date": deal_entity.expected_close_date,
                        "company_name": deal_entity.company_name,
                        "primary_contact": deal_entity.primary_contact_id,
                        "status": deal_entity.status,
                        "value": deal_entity.value,
                        "source_id": deal_entity.source_id,
                        "stage_id": deal_entity.stage_id
                    }
                }
        response = util.rest("PUT",endpoint,context['headers']['api_key'],data,deal_entity.deal_id)
        return json.loads(response.text)

    def update_person(self, context, payload):
        '''Updates a person information.'''
        person_entity = PipelinedealsPerson(**payload)
        endpoint = 'people'
        data = {
                "person": {
                            "person_id": person_entity.person_id,
                            "first_name": person_entity.first_name,
                            "last_name": person_entity.last_name,
                            "mobile": person_entity.mobile,
                            "phone": person_entity.phone,
                            "position": person_entity.position,
                            "website": person_entity.website,
                            "email": person_entity.email,
                            "company_name": person_entity.company,
                            "work_address_1": person_entity.work_address,
                            "home_address_1": person_entity.home_address,
                            "facebook_url": person_entity.facebook_url,
                            "linked_in_url": person_entity.linkedin_url,
                            "twitter": person_entity.twitter_username,
                            "lead_status_id": person_entity.status_id,
                            "lead_source_id" : person_entity.source_id
                        }
                    }
        response = util.rest("PUT",endpoint,context['headers']['api_key'],data,person_entity.person_id)
        return json.loads(response.text)