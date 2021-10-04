from unified.core.triggers import Triggers
from crm.onepagecrm.entities.onepagecrm_contact import OnepagecrmContact
from crm.onepagecrm.entities.onepagecrm_deal import OnpagecrmDeal


class OnepagecrmTriggers(Triggers):

    def contact_updated(self, context, payload):
        ''' triggers when contact updated'''

        contact = OnepagecrmContact(
            contact_id=payload["data"]["contact"]["id"],
            first_name=payload["data"]["contact"]["first_name"],
            last_name=payload["data"]["contact"]["last_name"],
            job_title=payload["data"]["contact"]["job_title"],
            company_id=payload["data"]["contact"]["company_id"],
            company=payload["data"]["contact"]["company_name"],
            company_size=payload["data"]["contact"]["company_size"],
            status=payload["data"]["contact"]["status"],
            tags=payload["data"]["contact"]["tags"],
            mailing_street=payload["data"]["contact"]["address_list"][0]["address"] or None,
            mailing_city=payload["data"]["contact"]["address_list"][0]["city"] or None,
            mailing_state=payload["data"]["contact"]["address_list"][0]["state"] or None,
            mailing_country=payload["data"]["contact"]["address_list"][0]["country_code"] or None,
            mailing_zip=payload["data"]["contact"]["address_list"][0]["zip_code"] or None,
            created_date=payload["data"]["contact"]["created_at"],
            updated_date=payload["data"]["contact"]["modified_at"],
            email=payload["data"]["contact"]["emails"] or None,
        )
        return contact.__dict__

    def new_contact(self, context, payload):
        ''' triggers when new contact created'''

        contact = OnepagecrmContact(
            contact_id=payload["data"]["contact"]["id"],
            first_name=payload["data"]["contact"]["first_name"],
            last_name=payload["data"]["contact"]["last_name"],
            job_title=payload["data"]["contact"]["job_title"],
            company_id=payload["data"]["contact"]["company_id"],
            owner_id=payload["data"]["contact"]["owner_id"],
            company=payload["data"]["contact"]["company_name"],
            company_size=payload["data"]["contact"]["company_size"],
            status=payload["data"]["contact"]["status"],
            tags=payload["data"]["contact"]["tags"],
            mailing_street=payload["data"]["contact"]["address_list"][0]["address"] or None,
            mailing_city=payload["data"]["contact"]["address_list"][0]["city"] or None,
            mailing_state=payload["data"]["contact"]["address_list"][0]["state"] or None,
            mailing_country=payload["data"]["contact"]["address_list"][0]["country_code"] or None,
            mailing_zip=payload["data"]["contact"]["address_list"][0]["zip_code"] or None,
            created_date=payload["data"]["contact"]["created_at"],
            updated_date=payload["data"]["contact"]["modified_at"],
            email = payload["data"]["contact"].get('emails')[0].get('value') if payload["data"]["contact"].get('emails') else None
        )
        return contact.__dict__

    def new_next_action(self, context, payload):
        ''' triggers when new next action created'''

        next_action = OnepagecrmContact(
            action_id=payload["data"]["action"]["id"],
            company_id=payload["data"]["action"]["contact_id"],
            status=payload["data"]["action"]["status"],
            created_date=payload["data"]["action"]["created_at"],
            updated_date=payload["data"]["action"]["modified_at"],
            description=payload["data"]["action"]["text"],
            done=payload["data"]["action"]["done"]
        )
        return next_action.__dict__

    def new_won_deal(self, context, payload):
        '''triggers when new deal craeted'''

        won_deal = OnpagecrmDeal(
            deal_id=payload["data"]["deal"]["id"],
            contact_id=payload["data"]["deal"]["contact_id"],
            name=payload["data"]["deal"]["name"],
            description=payload["data"]["deal"]["text"],
            owner_name=payload["data"]["deal"]["owner"]["name"],
            owner_email=payload["data"]["deal"]["owner"]["email"],
            created_date=payload["data"]["deal"]["created_at"],
            updated_date=payload["data"]["deal"]["modified_at"],
            close_date=payload["data"]["deal"]["close_date"],
            status=payload["data"]["deal"]["status"],
            value=payload["data"]["deal"]["amount"],
            owner_id=payload["data"]["deal"]["owner_id"]
        )

        return won_deal.__dict__
