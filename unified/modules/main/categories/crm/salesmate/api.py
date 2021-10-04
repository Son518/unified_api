# from crm.salesforce import util
# from crm.salesforce.entities.salesforce_contact import SalesforceContact
# from crm.salesforce.entities.salesforce_account import SalesforceAccount
# from crm.salesforce.entities.salesforce_opportunity import SalesforceOpportunity
# from crm.salesforce.entities.salesforce_lead import SalesforceLead
# from crm.salesforce.entities.salesforce_event import SalesforceEvent
# from crm.salesforce.entities.salesforce_task import SalesforceTask
# from crm.salesforce.entities.salesforce_note import SalesforceNote
import json

class SalesmateApi:
    @staticmethod
    def contact_by_id(context, payload):
        print("------------", context)
        return json.dumps({
            "res": "ddddddddd"
        })
        
    @staticmethod
    def test():
        return json