from unified.core.triggers import Triggers
from crm.pipelinedeals.entities.pipelinedeals_company import PipelinedealsCompany
from crm.pipelinedeals.entities.pipelinedeals_deal import PipelinedealsDeal
from crm.pipelinedeals.entities.pipelinedeals_person import PipelinedealsPerson
import json

class PipelinedealsTriggers(Triggers):

    def new_company(self, context, payload):
        """ Create new company"""
        response = payload['event_data']
        data = PipelinedealsCompany(
                                    trigger=payload['trigger'],
                                    name=response['name'],
                                    phone=response['phone1'],
                                    website=response['web'],
                                    email=response['email'],
                                    company=response['user']['account']['company_name'],
                                    address=response['address_1'],
                                    city=response['city'],
                                    state=response['state'],
                                    postal_code=response['postal_code'],
                                    country=response['country'],
                                    owner_name=response['owner_name'],
                                    user_id=response['user_id']
                                )
        return data.__dict__

    def new_deal(self, context, payload):
        """ Create new deal"""
        response = payload['event_data']
        data = PipelinedealsDeal(
                                name=response['name'],
                                company_name=response['primary_contact']['company_name'],
                                primary_contact_id=response['primary_contact_id'],
                                status=response['status'],
                                value=response['value'],
                                stage_id=response['deal_stage_id'],
                                source_id=response['source_id'],
                                account_id=response['account_id'],
                                trigger=payload['trigger'],
                                company_id=response['company_id'],
                                probability=response['probability']
                            )
        return data.__dict__

    def new_person(self, context, payload):
        """ Create new person"""
        response = payload['event_data']
        data = PipelinedealsPerson(
                                    first_name=response['first_name'],
                                    last_name=response['last_name'],
                                    phone=response['phone'],
                                    position=response['position'],
                                    website=response['website'],
                                    email=response['email'],
                                    company=response['company_id'],
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
                                    status_id=response['lead_status_id'],
                                    source_id=response['lead_source_id'],
                                    summary=response['summary'],
                                    facebook_url=response['facebook_url']
                                )
        return data.__dict__
   
    def moved_deal(self, context, payload):
        """moved deal"""
        response = payload['event_data']
        data = PipelinedealsDeal(
                                name=response['name'],
                                company_name=response['primary_contact']['company_name'],
                                primary_contact_id=response['primary_contact_id'],
                                status=response['status'],
                                value=response['value'],
                                stage_id=response['deal_stage_id'],
                                source_id=response['source_id'],
                                account_id=response['account_id'],
                                trigger=payload['trigger'],
                                company_id=response['company_id'],
                                probability=response['probability'],
                                updated_by_user_id=response['updated_by_user_id'],
                                deal_pipeline_id=response['deal_pipeline_id'],
                                deal_stage_id=response['deal_stage_id']
                            )
        return data.__dict__

    def status_changed_on_deal(self, context, payload):
        """deal status changed"""
        response = payload['event_data']
        data = PipelinedealsDeal(
                                name=response['name'],
                                company_name=response['primary_contact']['company_name'],
                                primary_contact_id=response['primary_contact_id'],
                                status=response['status'],
                                value=response['value'],
                                stage_id=response['deal_stage_id'],
                                source_id=response['source_id'],
                                account_id=response['account_id'],
                                trigger=payload['trigger'],
                                company_id=response['company_id'],
                                probability=response['probability'],
                                updated_by_user_id=response['updated_by_user_id'],
                                deal_pipeline_id=response['deal_pipeline_id']
                            )
        return data.__dict__