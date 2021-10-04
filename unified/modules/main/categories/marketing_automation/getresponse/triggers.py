from dataclasses import dataclass
from unified.core.triggers import Triggers
from marketing_automation.getresponse.entities.getresponse_contact import GetresponseContact

class GetresponseTriggers(Triggers):

    def new_contact(self, context, payload):
        """Get a new contant details
        """

        data = GetresponseContact(
            contact_id= payload.get("CONTACT_ID"),
            name= payload.get("contact_name"),
            email= payload.get("contact_email"),
            list_id= payload.get("CAMPAIGN_ID"),
            campaignId= payload.get("CAMPAIGN_ID"),
            email_address= payload.get("contact_email"),
            campaign_name= payload.get("campaign_name")
        )
        return data.__dict__