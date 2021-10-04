import json
from crm.nocrm_io.entities.nocrm_io_lead import NoCRMioLead
from crm.nocrm_io.entities.nocrm_io_row import NoCRMioRow
from crm.nocrm_io import util


class NocrmioApi():

    def lead_by_email(self, context, params):
        """
        retieves lead based on email parameter
        context holds headers
        params holds email
        """
        leads = json.loads(
            util.rest("GET", "leads", context["headers"], params).text)
        lead_value = []
        for lead in leads:
            lead_value.append(self.nocrm_io_api_mappings(lead))
        return json.dumps(lead_value)

    def prospecting_list_by_title(self, context, params):
        """
        retieves prospecting_list based on title parameter
        context holds headers
        params holds title
        """
        prospecting_list = json.loads(
            util.rest("GET", "prospects", context["headers"], params).text)
        row_obj = NoCRMioRow(prospecting_list_id=prospecting_list[0]["id"]
                             ).__dict__
        return row_obj

    def nocrm_io_api_mappings(self, payload):
        """
        mapping function for unification
        """
        lead_obj = NoCRMioLead(
            lead_id=payload["id"],
            title=payload["title"],
            description=payload["description"],
            step_name=payload["step"],
            tags=payload["tags"])
        return lead_obj.__dict__
