import json
from core.triggers import Triggers
from crm.nocrm_io.entities.nocrm_io_lead import NoCRMioLead
from crm.nocrm_io.entities.nocrm_io_row import NoCRMioRow


class NoCRMioTriggers(Triggers):

    def new_lead(self, context, payload):
        """
        triggers when new lead created
        context headers
        payload holds request.data
        """
        return self.nocrm_io_mappings(payload)

    def lead_content_has_changed(self, context, payload):
        """
        triggers when lead content has changed
        context headers
        payload holds request.data
        """
        return self.nocrm_io_mappings(payload)

    def lead_deleted(self, context, payload):
        """
        triggers when new lead deleted
        context headers
        payload holds request.data
        """
        return self.nocrm_io_mappings(payload)

    def lead_status_changed(self, context, payload):
        """
        triggers when new lead status changed
        context headers
        payload holds request.data
        """
        return self.nocrm_io_mappings(payload)

    def lead_step_changed(self, context, payload):
        """
        triggers when new lead step changed
        context headers
        payload holds request.data
        """
        return self.nocrm_io_mappings(payload)

    def new_prospect_created(self, context, payload):
        """
        triggers when new prospects created
        context headers
        payload holds request.data
        """
        row = payload["webhook_event"]["data"]
        row_obj = NoCRMioRow(prospecting_list_id=row["id"],
                             name=row["content"][0],
                             first_name=row["content"][1],
                             last_name=row["content"][2],
                             phone=row["content"][3],
                             email=row["content"][4]
                             )
        return row_obj.__dict__

    def nocrm_io_mappings(self, payload):
        """
        mapping function for unification of payload
        """
        lead = payload["webhook_event"]["data"]
        fields = lead["fields"]
        lead_obj = NoCRMioLead(
            lead_id=lead["id"],
            last_name=fields["last_name"],
            first_name=fields["first_name"],
            title=lead["title"],
            probability=lead["probability"],
            amount=lead["amount"],
            description=lead["description"],
            street=fields["address"],
            city=fields["city"],
            state=fields["state"],
            zip=fields["zipcode"],
            phone=fields["phone"],
            mobile=fields["mobile"],
            fax=fields["fax"],
            email=fields["email"],
            user_email=lead["user"]["email"],
            step_name=lead["step"])
        return lead_obj.__dict__
