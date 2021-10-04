from unified.core.triggers import Triggers
from crm.freshworks.entities.freshworks_contact import FreshworksContact
from crm.freshworks.entities.freshworks_account import FreshworksAccount
from crm.freshworks.entities.freshworks_deal import FreshworksDeal


class FreshworksTriggers(Triggers):

    def new_contact(self, context, payload):
        """
        triggers when new contact created
        context holds the headers 
        payload holds the request.body
        """
        contact = FreshworksContact(
            contact_id=payload["contact_id"],
            first_name=payload["contact_first_name"],
            last_name=payload["contact_last_name"],
            job_title=payload["contact_job_title"],
            email=payload["contact_email"],
            business_phone=payload["contact_work_number"],
            mobile_number=payload["contact_mobile_number"],
            external_id=payload["contact_external_id"],
            mailing_street=payload["contact_address"],
            mailing_city=payload["contact_city"],
            mailing_state=payload["contact_state"],
            mailing_zip=payload["contact_zipcode"],
            mailing_country=payload["contact_country"],
            facebook=payload["contact_facebook"],
            twitter=payload["contact_twitter"],
            linkedin=payload["contact_linkedin"],
            created_date=payload["contact_created_at"],
            updated_date=payload["contact_updated_at"],
        )
        return contact.__dict__

    def new_account(self, context, payload):
        """
        triggers when new account created
        context holds the headers 
        payload holds the request.body
        """
        account = FreshworksAccount(
            account_id=payload["sales_account_id"],
            account_name=payload["sales_account_name"],
            website=payload["sales_account_website"],
            phone=payload["sales_account_phone"],
            address=payload["sales_account_address"],
            city=payload["sales_account_city"],
            state=payload["sales_account_state"],
            zipcode=payload["sales_account_zipcode"],
            country=payload["sales_account_country"],
            mailing_street=payload["sales_account_address"],
            mailing_city=payload["sales_account_city"],
            mailing_state=payload["sales_account_state"],
            mailing_zip=payload["sales_account_zipcode"],
            mailing_country=payload["sales_account_country"],
            facebook=payload["sales_account_facebook"],
            twitter=payload["sales_account_twitter"],
            linkedin=payload["sales_account_linkedin"],
            created_date=payload["sales_account_created_at"],
            updated_date=payload["sales_account_updated_at"],
            owner_id=payload["sales_account_owner_id"])
        return account.__dict__

    def new_deal(self, context, payload):
        """
        triggers when new deal created
        context holds the headers 
        payload holds the request.body
        """
        deal = FreshworksDeal(deal_id=payload["deal_id"],
                              name=payload["deal_name"],
                              created_date=payload["deal_created_at"],
                              updated_date=payload["deal_updated_at"],
                              close_date=payload["deal_closed_date"],
                              value=payload["deal_expected_deal_value"],
                              probability=payload["deal_probability"])
        return deal.__dict__
