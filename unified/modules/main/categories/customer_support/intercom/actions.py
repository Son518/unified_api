import json
from core.actions import Actions
from customer_support.intercom import util
from customer_support.intercom.entities.intercom_contact import IntercomContact
from customer_support.intercom.entities.intercom_company import IntercomCompany
from customer_support.intercom.entities.intercom_event import IntercomEvent
from customer_support.intercom.api import IntercomApi


class IntercomActions(Actions):

    def create_user(self, context, user_payload):
        """
        creates new user
        context holds headers
        user_payload holds request.body
        """
        user_entity = IntercomContact(**user_payload)
        user_data = {
            "role": "user",
            "email": user_entity.email,
            "name": user_entity.full_name,
            "signed_up_at": user_entity.created_date,
        }
        response = util.rest(
            "POST", "contacts", context["headers"]["access_token"], user_data).text
        return json.loads(response)

    def create_lead(self, context, lead_payload):
        """
        creates new lead
        context holds headers
        lead_payload holds request.body
        """
        lead_entity = IntercomContact(**lead_payload)
        lead_data = {
            "role": "lead",
            "email": lead_entity.email,
            "name": lead_entity.full_name,
            "phone": lead_entity.phone_number,
            "unsubscribed_from_emails": lead_entity.unsubscribed,
            "signed_up_at": lead_entity.created_date,
        }
        response = util.rest(
            "POST", "contacts", context["headers"]["access_token"], lead_data).text
        return json.loads(response)

    def update_user(self, context, user_payload):
        """
        updates existing user
        context holds headers
        user_payload holds request.body
        """
        user_entity = IntercomContact(**user_payload)
        user_data = {
            "role": "user",
            "name": user_entity.full_name,
            "signed_up_at": user_entity.created_date,
            "unsubscribed_from_emails": user_entity.unsubscribed_from_emails,
            "phone": user_entity.phone_number,
        }
        params = {"email": user_entity.lookup_email}
        user_id = IntercomApi().user_by_email(context, params)["user_id"]
        response = util.rest(
            "PUT", "contacts", context["headers"]["access_token"], user_data, user_id).text
        return json.loads(response)

    def update_lead(self, context, user_payload):
        """
        updates existing lead
        context holds headers
        lead_payload holds request.body
        """
        user_entity = IntercomContact(**user_payload)
        user_data = {
            "role": "lead",
            "name": user_entity.full_name,
            "email": user_entity.email,
            "signed_up_at": user_entity.created_date,
            "unsubscribed": user_entity.unsubscribed_from_emails,
            "phone": user_entity.phone_number,
        }
        response = util.rest(
            "PUT", "contacts", context["headers"]["access_token"], user_data, user_entity.lead_id).text
        return json.loads(response)

    def update_company(self, context, company_payload):
        """
        updates details of company 
        context holds headers
        company_payload holds request.body
        """
        company_entity = IntercomCompany(**company_payload)
        company_data = {
            "company_id": company_entity.company,
            "monthly_spend": company_entity.monthly_revenue,
            "plan": company_entity.plan
        }
        response = util.rest(
            "POST", "companies", context["headers"]["access_token"], company_data).text
        return json.loads(response)

    def add_event(self, context, event_payload):
        """
        add new event
        context holds headers
        event_payload holds request.body
        """
        event_entity = IntercomEvent(**event_payload)
        event_data = {
            "event_name": event_entity.event_name,
            "email": event_entity.email,
            "created_at": event_entity.created_date
        }
        response = util.rest(
            "POST", "events", context["headers"]["access_token"], event_data)
        if response.status_code == 202:
            return {"status": "completed"}
        return json.loads(response.text)

    def add_note(self, context, note_payload):
        """
        adds note on specified id
        context holds headers
        note_payload holds request.body
        """
        note_entity = IntercomContact(**note_payload)
        note_data = {
            "body": note_entity.note_text,
            "admin_id": note_entity.admin_id
        }
        response = util.rest(
            "POST", "notes", context["headers"]["access_token"], note_data, note_entity.id).text
        return json.loads(response)

    def add_tag_on_company(self, context, tag_payload):
        """
        add tag to company
        context holds headers
        lead_payload holds request.body
        """
        tag_entity = IntercomCompany(**tag_payload)
        tag_data = {
            "name": tag_entity.tag_name,
            "companies": [{
                "id": tag_entity.company
            }]
        }
        response = util.rest(
            "POST", "tags", context["headers"]["access_token"], tag_data).text
        return json.loads(response)

    def add_tag_on_lead(self, context, tag_payload):
        """
        creates new tag and adds on specified id
        context holds headers
        tag_payload holds request.body
        """
        tag_entity = IntercomContact(**tag_payload)
        create_tag_data = {"name": tag_entity.tag_name}
        tag_response = util.rest(
            "POST", "tags", context["headers"]["access_token"], create_tag_data).text
        add_tag_data = {"id": json.loads(tag_response)["id"]}
        response = util.rest(
            "POST", "add_tags", context["headers"]["access_token"], add_tag_data, tag_entity.lead).text
        return response

    def add_tag_on_user(self, context, tag_payload):
        """
        creates new tag and adds on specified id
        context holds headers
        tag_payload holds request.body
        """
        tag_entity = IntercomContact(**tag_payload)
        create_tag_data = {"name": tag_entity.tag_name}
        tag_response = util.rest(
            "POST", "tags", context["headers"]["access_token"], create_tag_data).text
        add_tag_data = {"id": json.loads(tag_response)["id"]}
        print(add_tag_data)
        response = util.rest(
            "POST", "add_tags", context["headers"]["access_token"], add_tag_data, tag_entity.user).text
        return response

    def remove_tag_on_company(self, context, tag_payload):
        """
        removes tag from company
        context holds headers
        tag_payload holds request.body
        """
        tag_entity = IntercomCompany(**tag_payload)
        tag_data = {
            "name": tag_entity.tag_name,
            "companies": [{
                "id": tag_entity.company,
                "untag": tag_entity.untag
            }]
        }
        response = util.rest(
            "POST", "tags", context["headers"]["access_token"], id=tag_data).text
        return json.loads(response)

    def remove_tag_on_user(self, context, tag_payload):
        """
        removes tag from user
        context holds headers
        tag_payload holds request.body
        """
        tag_entity = IntercomContact(**tag_payload)
        tag_data = [tag_entity.user_id, tag_entity.tag_id]
        response = util.rest(
            "DELETE", "tags", context["headers"]["access_token"], id=tag_data).text
        return response

    def remove_tag_on_lead(self, context, tag_payload):
        """
        removes tag from lead
        context holds headers
        tag_payload holds request.body
        """
        tag_entity = IntercomContact(**tag_payload)
        tag_data = [tag_entity.lead_id, tag_entity.tag_id]
        response = util.rest(
            "DELETE", "tags", context["headers"]["access_token"], id=tag_data).text
        return response
