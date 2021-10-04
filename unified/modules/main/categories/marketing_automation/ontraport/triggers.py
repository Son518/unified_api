from dataclasses import dataclass
from unified.core.triggers import Triggers
from marketing_automation.ontraport.entities.ontraport_contact import OntraportContact


class OntraportTriggers(Triggers):

    def new_contact(self, context, payload):
        """Get a new contant details
        """

        data = OntraportContact(
            contact_id= payload["data"].get("id"),
            first_name= payload["data"].get("firstname"),
            last_name= payload["data"].get("lastname"),
            email_address= payload["data"].get("email"),
            date= payload["data"].get("date"),
            office_phone= payload["data"].get("office_phone"),
            company= payload["data"].get("company"),
            title= payload["data"].get("title"),
            country= payload["data"].get("country"),
            zip_code= payload["data"].get("zip"),
            owner= payload["data"].get("owner"),
            unique_id= payload["data"].get("unique_id"),
            profile_image= payload["data"].get("profile_image")
        )
        return data.__dict__


    def tag_added(self, context, payload):
        """Tag Added to Contact"""

        data = OntraportContact(
            contact_id= payload["data"]["id"],
            owner= payload["data"]["owner"],
            first_name= payload["data"]["firstname"],
            last_name= payload["data"]["lastname"],
            email_address= payload["data"]["email"],
            address= payload["data"]["address"],
            city= payload["data"]["city"],
            state= payload["data"]["state"],
            zip_code= payload["data"]["zip"],
            date= payload["data"]["date"],
            office_phone= payload["data"]["office_phone"],
            company= payload["data"]["company"],
            country= payload["data"]["country"],
            unique_id= payload["data"]["unique_id"],
            profile_image= payload["data"]["profile_image"],
            contact_cat= payload["data"]["contact_cat"]
        )
        return data.__dict__


    def tag_removed(self, context, payload):
        """Triggers when a Tag is successfully removed from contact"""
        
        data = OntraportContact(
            contact_id= payload["data"]["id"],
            owner= payload["data"]["owner"],
            first_name= payload["data"]["firstname"],
            last_name= payload["data"]["lastname"],
            email_address= payload["data"]["email"],
            address= payload["data"]["address"],
            city= payload["data"]["city"],
            state= payload["data"]["state"],
            zip_code= payload["data"]["zip"],
            date= payload["data"]["date"],
            office_phone= payload["data"]["office_phone"],
            company= payload["data"]["company"],
            country= payload["data"]["country"],
            unique_id= payload["data"]["unique_id"],
            profile_image= payload["data"]["profile_image"],
            contact_cat= payload["data"]["contact_cat"]
        )
        return data.__dict__