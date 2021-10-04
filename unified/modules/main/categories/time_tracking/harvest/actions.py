from unified.core.actions import Actions
import json
import requests
from time_tracking.harvest import util
from time_tracking.harvest.entities.harvest_client import HarvestClient
from time_tracking.harvest.entities.harvest_contact import HarvestContact
from time_tracking.harvest.entities.harvest_project import HarvestProject
from time_tracking.harvest.entities.harvest_task import HarvestTask
from time_tracking.harvest.entities.harvest_timesheet_entry import HarvestTimesheetEntry


class HarvestAction(Actions):

    def create_client(self, context, payload):
        """ Create a client"""

        client_data = HarvestClient(**payload)
        data = {
            "name": client_data.name
        }
        response = util.rest("POST", "clients", context, data)
        return json.loads(response.text)

    def create_contact(self, context, payload):
        """ Create a contact"""

        contact_data = HarvestContact(**payload)
        data = {
            "client_id": contact_data.client_id,
            "first_name": contact_data.first_name
        }

        if contact_data.last_name is not None:
            data["last_name"] = contact_data.last_name

        if contact_data.email is not None:
            data["email"] = contact_data.email
        
        if contact_data.title is not None:
            data["title"] = contact_data.title
        
        if contact_data.phone_office is not None:
            data["phone_office"] = contact_data.phone_office
        
        if contact_data.phone_mobile is not None:
            data["phone_mobile"] = contact_data.phone_mobile
        
        if contact_data.fax is not None:
            data["fax"] = contact_data.fax   
                
        response = util.rest("POST", "contacts", context, data)
        return json.loads(response.text)

    def create_project(self, context, payload):
        """ Create a project"""

        project_data = HarvestProject(**payload)
        data = {
            "client_id": project_data.client_id,
            "name": project_data.name
        }

        if project_data.code is not None:
            data["code"] = project_data.code

        if project_data.is_active is not None:
            data["is_active"] = project_data.is_active
        
        if project_data.is_billable is not None:
            data["is_billable"] = project_data.is_billable
        
        if project_data.bill_by is not None:
            data["bill_by"] = project_data.bill_by
        
        if project_data.project_billing_rate is not None:
            data["hourly_rate"] = project_data.project_billing_rate
        
        if project_data.budget_by is not None:
            data["budget_by"] = project_data.budget_by

        if project_data.budget_amount is not None:
            data["budget"] = int(project_data.budget_amount)

        if project_data.notes is not None:
            data["notes"] = project_data.notes
                
        response = util.rest("POST", "projects", context, data)
        return json.loads(response.text)

    def create_task(self, context, payload):
        """ Create a task"""

        task_data = HarvestTask(**payload)
        data = {
            "name": task_data.task_name
        }
                
        response = util.rest("POST", "tasks", context, data)
        return json.loads(response.text)

    def create_timesheet_entry(self, context, payload):
        """ Create a time sheet entry"""

        timesheet_data = HarvestTimesheetEntry(**payload)
        
        data = {
            "project_id": timesheet_data.project,
            "task_id": timesheet_data.task,
            "spent_date": timesheet_data.spent_at
        }  

        if timesheet_data.notes is not None:
            data["notes"] = timesheet_data.notes

        if timesheet_data.hours is not None:
            data["hours"] = timesheet_data.hours
            
        response = util.rest("POST", "time_entries", context, data)
        return json.loads(response.text)