from agilecrm.client import Client
from unified.core.triggers import Triggers
from crm.agilecrm.entities.agilecrm_contact import AgilecrmContact
from crm.agilecrm.entities.agilecrm_deal import AgilecrmDeal
from crm.agilecrm.entities.agilecrm_task import AgilecrmTask
from crm.agilecrm.util import agilecrm_authentication
from crm.agilecrm.entities.agilecrm_event import AgilecrmEvent
from crm.agilecrm.entities.agilecrm_tag import AgilecrmTag
import json


class AgilecrmTriggers(Triggers):
    
    def contact_data(self, event_data, key):
        try:
            return [entity for entity in event_data['properties'] if entity['name'] == key][0].get('value')
        except (KeyError, IndexError, Exception) as error:
            return None


    def new_contact(self, contact, payload):
        event_data = payload["eventData"]
        contact = AgilecrmContact(
            first_name = self.contact_data(event_data,'first_name'),
            last_name = self.contact_data(event_data,'last_name'),
            email = self.contact_data(event_data,'email'),
            business_phone = self.contact_data(event_data,'phone'),
            company = self.contact_data(event_data,'company'),
            phone = self.contact_data(event_data,'phone'),
            title = self.contact_data(event_data,'title'),
            mailing_street = json.loads(self.contact_data(event_data,'address')).get('address'),
            mailing_city = json.loads(self.contact_data(event_data,'address')).get('city'),
            mailing_country = json.loads(self.contact_data(event_data,'address')).get('countryname'),
            mailing_state = json.loads(self.contact_data(event_data,'address')).get('state'),
            mailing_zip = json.loads(self.contact_data(event_data,'address')).get('zip'),
            contact_id=event_data["id"],
            contact_type=event_data["type"],
            star_value=event_data["star_value"],
            lead_score=event_data["lead_score"],
            tags=event_data["tags"],
            owner_id=event_data["owner"]["id"],
            domain=event_data["owner"]["domain"],
            description=payload["eventName"])

        return contact.__dict__

    def new_deal(self, contact, payload):

        owner_data = payload["eventData"]
        deal = AgilecrmDeal(
            name=owner_data["name"],
            deal_id=owner_data["id"],
            apply_discount=owner_data["apply_discount"],
            discount_value=owner_data["discount_value"],
            discount_amt=owner_data["discount_amt"],
            owner_id=owner_data["owner"]["id"],
            owner_email=owner_data["owner"]["email"],
            contact_id=owner_data["contact_ids"],
            probability=owner_data["probability"],
            owner=owner_data["owner"]["name"],
            created_date=str(owner_data["created_time"]),
            end_date=str(owner_data["close_date"]))

        return deal.__dict__
