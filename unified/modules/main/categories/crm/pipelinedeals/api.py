import json
from flask import jsonify
import requests
from requests.api import request
from crm.pipelinedeals.entities.pipelinedeals_company import PipelinedealsCompany
from crm.pipelinedeals.entities.pipelinedeals_deal import PipelinedealsDeal
from crm.pipelinedeals.entities.pipelinedeals_person import PipelinedealsPerson
from crm.pipelinedeals import util

class PipelinedealsApi():

    def company(self, context, params):
        '''get company by id'''

        endpoint='companies'
        response = json.loads(util.rest("GET",endpoint,context['headers']["api_key"],{},params['company_id']).text)
        company_obj = PipelinedealsCompany(
                                        name=response['name'],
                                        website=response['web'],
                                        email=response['email'],
                                        address=response['address_1'],
                                        city=response['city'],
                                        state=response['state'],
                                        postal_code=response['postal_code'],
                                        country=response['country']
                                    )
        return company_obj.__dict__

    def deal(self, context, params):
        '''get deal by id'''
        
        endpoint='deals'
        response = json.loads(util.rest("GET",endpoint,context['headers']["api_key"],{},params['deal_id']).text)
        deal_obj = PipelinedealsDeal(
                                    name=response['name'],
                                    primary_contact_id=response['primary_contact_id'],
                                    status=response['status'],
                                    value=response['value']
                                )
        return deal_obj.__dict__

    def person(self, context, params):
        '''get people by id'''
        
        endpoint='people'
        response = json.loads(util.rest("GET",endpoint,context['headers']["api_key"],{},params['person_id']).text)
        person_obj = PipelinedealsPerson(
                                        first_name=response['first_name'],
                                        last_name=response['last_name'],
                                        phone=response['phone'],
                                        position=response['position'],
                                        website=response['website'],
                                        email=response['email'],
                                        type=response['type'],
                                        work_address=response['work_address_1'],
                                        work_city=response['work_city'],
                                        work_state=response['work_state'],
                                        work_postal_code=response['work_postal_code'],
                                        work_country=response['work_country'],
                                        home_address=response['home_address_1'],
                                        home_city=response['home_city'],
                                        home_state=response['home_state'],
                                        home_country=response['home_country'],
                                        home_postal_code=response['home_postal_code'],
                                        summary=response['summary'],
                                        facebook_url=response['facebook_url']
                                    )
        return person_obj.__dict__

    def contacts_by_phone_number(self, context, params):
        '''get contacts by phone number'''

        endpoint = 'people/phone_number'
        response = json.loads(util.rest("GET",endpoint,context['headers']["api_key"],{},phone_number=params['person_phone']).text)      
        contacts = response['entries']
        contact_value = []
        for contact in contacts:
            contact_obj = PipelinedealsPerson(
                                            contact_id=contact.get("id") or None, 
                                            first_name=contact.get("first_name") or None,
                                            last_name=contact.get("last_name") or None,
                                            phone=contact.get("phone") or None,
                                            position=contact.get("position") or None,
                                            website=contact.get("website") or None,
                                            email=contact.get("email") or None,
                                            type=contact.get("type") or None,
                                            work_address=contact.get("work_address_1") or None,
                                            work_city=contact.get("work_city") or None,
                                            work_state=contact.get("work_state") or None,
                                            work_postal_code=contact.get("work_postal_code") or None,
                                            work_country=contact.get("work_country") or None,
                                            home_address=contact.get("home_address_1") or None,
                                            home_city=contact.get("home_city") or None,
                                            home_state=contact.get("home_state") or None,
                                            home_country=contact.get("home_country") or None,
                                            home_postal_code=contact.get("home_postal_code") or None,
                                            summary=contact.get("summary") or None,
                                            facebook_url=contact.get("facebook_url") or None,
                                            mobile=contact.get("mobile") or None
                                        )
            contact_value.append(contact_obj.__dict__)
        return json.dumps(contact_value)
