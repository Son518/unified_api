import json
from crm.nocrm_io import util
from core.actions import Actions
from crm.nocrm_io.entities.nocrm_io_lead import NoCRMioLead
from crm.nocrm_io.entities.nocrm_io_row import NoCRMioRow


class NocrmioActions(Actions):

    def create_lead(self, context, lead_payload):
        """
        creates a lead 
        context holds the headers 
        lead_payload holds the request.body
        """
        lead_entity = NoCRMioLead(**lead_payload)
        data = {
            "title": lead_entity.title,
            "description": lead_entity.description,
            "user_id": lead_entity.user_email,
            "tags": [lead_entity.tags],
            "created_at": lead_entity.creation_date
        }
        response = util.rest("POST", "leads", context["headers"], data).text
        return json.loads(response)

    def add_comment(self, context, comment_payload):
        """
        adds comments to  a lead 
        context holds the headers 
        comment_payload holds the request.body
        """
        comment_entity = NoCRMioLead(**comment_payload)
        data = {
            "content": comment_entity.comment,
        }
        response = util.rest(
            "POST", "comments", context["headers"], data, comment_entity.lead_id).text
        return json.loads(response)

    def add_tags(self, context, tag_payload):
        """
        add tags to a lead 
        context holds the headers 
        tag_payload holds the request.body
        """
        lead_entity = NoCRMioLead(**tag_payload)
        data = {
            "tags": [lead_entity.tags],
        }
        response = util.rest(
            "PUT", "tags", context["headers"], data, lead_entity.lead_id).text
        return json.loads(response)

    def change_lead_title(self, context, lead_payload):
        """
        changes a lead title
        context holds the headers 
        lead_payload holds the request.body
        """
        lead_entity = NoCRMioLead(**lead_payload)
        data = {
            "title": lead_entity.title
        }
        response = util.rest(
            "PUT", "leads", context["headers"], data, lead_entity.lead_id).text
        return json.loads(response)

    def change_status(self, context, lead_payload):
        """
        changes a lead status 
        context holds the headers 
        lead_payload holds the request.body
        """
        lead_entity = NoCRMioLead(**lead_payload)
        data = {
            "status": lead_entity.status.lower()
        }
        response = util.rest(
            "PUT", "leads", context["headers"], data, lead_entity.lead_id).text
        return json.loads(response)

    def change_step(self, context, lead_payload):
        """
        changes a lead step 
        context holds the headers 
        lead_payload holds the request.body
        """
        lead_entity = NoCRMioLead(**lead_payload)
        data = {
            "step": lead_entity.step_name,
            "step_id": lead_entity.step_id
        }
        response = util.rest(
            "PUT", "leads", context["headers"], data, lead_entity.lead_id).text
        return json.loads(response)

    def create_row(self, context, row_payload):
        """
        creates row in prospect list
        context holds the headers 
        row_payload holds the request.body
        """
        row_entity = NoCRMioRow(**row_payload)
        content = [row_entity.name, row_entity.first_name,
                   row_entity.last_name, row_entity.email, row_entity.phone]
        data = {
            "content": [content]
        }
        response = util.rest(
            "POST", "rows", context["headers"], data, row_entity.prospecting_list_id).text
        return response

    def log_an_activity(self, context, comment_payload):
        """
        logs an activity in lead 
        context holds the headers 
        lead_payload holds the request.body
        """
        comment_entity = NoCRMioLead(**comment_payload)
        data = {
            "content": comment_entity.comment,
            "activity_id": comment_entity.activity_id
        }
        response = util.rest(
            "POST", "comments", context["headers"], data, comment_entity.lead_id).text
        return json.loads(response)

    def set_amount_and_probability(self, context, lead_payload):
        """
        sets an amount and probability in lead
        context holds the headers 
        lead_payload holds the request.body
        """
        lead_entity = NoCRMioLead(**lead_payload)
        data = {
            "amount": lead_entity.amount,
            "probability": lead_entity.probability
        }
        response = util.rest(
            "PUT", "leads", context["headers"], data, lead_entity.lead_id).text
        return json.loads(response)

    def set_the_estimated_closing_date(self, context, lead_payload):
        """
        sets estimated closing date in lead
        context holds the headers 
        lead_payload holds the request.body
        """
        lead_entity = NoCRMioLead(**lead_payload)
        data = {
            "estimated_closing_date	": lead_entity.close_date
        }
        response = util.rest(
            "PUT", "leads", context["headers"], data, lead_entity.lead_id).text
        return json.loads(response)
