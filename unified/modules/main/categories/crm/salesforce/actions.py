from crm.salesforce import util
from crm.salesforce.entities.salesforce_contact import SalesforceContact
from crm.salesforce.entities.salesforce_account import SalesforceAccount
from crm.salesforce.entities.salesforce_opportunity import SalesforceOpportunity
from crm.salesforce.entities.salesforce_lead import SalesforceLead
from crm.salesforce.entities.salesforce_event import SalesforceEvent
from crm.salesforce.entities.salesforce_note import SalesforceNote
from crm.salesforce.entities.salesforce_task import SalesforceTask
from unified.core.actions import Actions
import json


class SalesforceActions(Actions):

    def create_contact(self, context, payload):
        """ Create new contact """

        access_token = util.get_access_token(context['headers'])
        contact = SalesforceContact(**payload)
        url = util.get_url(context) + "sobjects/Contact"

        contact_data = {
            "Salutation": contact.salutation,
            "LastName": contact.last_name,
            "FirstName": contact.first_name,
            "AccountId": contact.account_id,
            "Title": contact.title,
            "Department": contact.department,
            "Birthdate": util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', contact.birth_date),
            "ReportsToId": contact.reports_to,
            "LeadSource": contact.lead_source,
            "Phone": contact.phone,
            "HomePhone": contact.homephone,
            "MobilePhone": contact.mobile,
            "OtherPhone": contact.other_mobile,
            "Fax": contact.fax,
            "Email": contact.email,
            "AssistantName": contact.assistant,
            "AssistantPhone": contact.asst_mobile,
            "MailingStreet": contact.mailing_street,
            "MailingCity": contact.mailing_city,
            "MailingState": contact.mailing_state,
            "MailingPostalCode": contact.mailing_zip,
            "MailingCountry": contact.mailing_country,
            "OtherStreet": contact.other_street,
            "OtherCity": contact.other_city,
            "OtherState": contact.other_state,
            "OtherPostalCode": contact.other_zip,
            "OtherCountry": contact.other_country,
            "Languages__c": contact.languages,
            "Level__c": contact.level,
            "Description": contact.description
        }

        if contact.owner_id is not None:
            contact_data["OwnerId"] = contact.owner_id

        response = util.rest("POST", url, access_token, contact_data)

        return json.loads(response.text)

    def create_account(self, context, payload):
        """ Create new account """

        access_token = util.get_access_token(context['headers'])
        account = SalesforceAccount(**payload)
        url = util.get_url(context) + "sobjects/Account"

        account_data = {
            "Name": account.account_name,
            "ParentId": account.parent_id,
            "AccountNumber": account.account_number,
            "Site": account.account_site,
            "Type": account.type,
            "Industry": account.industry,
            "AnnualRevenue": account.annual_revenue,
            "Rating": account.rating,
            "Phone": account.phone,
            "Fax": account.fax,
            "Website": account.website,
            "TickerSymbol": account.ticker_symbol,
            "Ownership": account.ownership,
            "NumberOfEmployees": account.employees,
            "Sic": account.sic_code,
            "BillingStreet": account.billing_street,
            "BillingCity": account.billing_city,
            "BillingPostalCode": account.billing_zip,
            "BillingState": account.billing_state,
            "BillingCountry": account.billing_country,
            "ShippingStreet": account.shipping_street,
            "ShippingCity": account.shipping_city,
            "ShippingPostalCode": account.shipping_zip,
            "ShippingState": account.shipping_state,
            "ShippingCountry": account.shipping_country,
            "CustomerPriority__c": account.customer_priority,
            "SLAExpirationDate__c": account.end_date,
            "NumberofLocations__c": account.number_of_locations,
            "Active__c": account.active,
            "SLA__c": account.sla,
            "SLASerialNumber__c": account.sla_serial_number,
            "UpsellOpportunity__c": account.upsell_opportunity,
            "Description": account.description
        }

        if account.owner_id is not None:
            account_data["OwnerId"] = account.owner_id

        response = util.rest("POST", url, access_token, account_data)

        return json.loads(response.text)

    def create_opportunities(self, context, payload):
        """ Create new opportunity """

        access_token = util.get_access_token(context['headers'])
        opportunity = SalesforceOpportunity(**payload)
        url = util.get_url(context) + "sobjects/Opportunity"

        opportunity_data = {
            "AccountId": opportunity.account_id,
            "Amount": opportunity.amount,
            "Name": opportunity.opportunity_name,
            "CloseDate": opportunity.end_date,
            "Type": opportunity.type,
            "LeadSource": opportunity.lead_source,
            "NextStep": opportunity.next_step,
            "StageName": opportunity.stage,
            "OrderNumber__c": opportunity.order_number,
            "CurrentGenerators__c": opportunity.current_generator,
            "TrackingNumber__c": opportunity.tracking_number,
            "MainCompetitors__c": opportunity.main_competitor,
            "DeliveryInstallationStatus__c": opportunity.delivery_status,
            "Description": opportunity.description,
        }

        if opportunity.owner_id is not None:
            opportunity_data["OwnerId"] = opportunity.owner_id

        if opportunity.probability is not None:
            opportunity_data["Probability"] = opportunity.probability.rstrip('%')

        if opportunity.private is not None:
            opportunity_data["IsPrivate"] = opportunity.private

        response = util.rest("POST", url, access_token, opportunity_data)

        return json.loads(response.text)

    def create_lead(self, context, payload):
        """ Create new lead """

        access_token = util.get_access_token(context['headers'])
        lead = SalesforceLead(**payload)
        url = util.get_url(context) + "sobjects/Lead"

        lead_data = {
            "Salutation": lead.salutation,
            "LastName": lead.last_name,
            "FirstName": lead.first_name,
            "Company": lead.company,
            "Title": lead.title,
            "LeadSource": lead.lead_source,
            "Industry": lead.industry,
            "AnnualRevenue": lead.annual_revenue,
            "Phone": lead.phone,
            "MobilePhone": lead.mobile,
            "Fax": lead.fax,
            "Email": lead.email,
            "Website": lead.website,
            "Status": lead.lead_status,
            "Rating": lead.rating,
            "NumberOfEmployees": lead.no_employees,
            "ProductInterest__c": lead.product_interest,
            "SICCode__c": lead.sic_code,
            "CurrentGenerators__c": lead.current_generator,
            "NumberofLocations__c": lead.no_locations,
            "Street": lead.street,
            "City": lead.city,
            "PostalCode": lead.postal_code,
            "Country": lead.country,
            "State": lead.state,
            "Primary__c": lead.primary,
            "Description": lead.description
        }

        if lead.owner_id is not None:
            lead_data["OwnerId"] = lead.owner_id

        response = util.rest("POST", url, access_token, lead_data)

        return json.loads(response.text)

    def create_event(self, context, payload):
        """ Create new event """

        access_token = util.get_access_token(context['headers'])
        event = SalesforceEvent(**payload)
        url = util.get_url(context) + "sobjects/Event"

        event_data = {
              "Subject": event.subject,
              "StartDateTime": util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', event.start_date),
              "EndDateTime": util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', event.end_date),
              "IsAllDayEvent": event.all_day_event,
              "WhoId": event.name_id,
              "WhatId": event.related_to,
              "OwnerId": event.assigned_to,
              "Location": event.location
        }

        response = util.rest("POST", url, access_token, event_data)

        return json.loads(response.text)

    def create_note(self, context, payload):
        """ Create new note """

        access_token = util.get_access_token(context['headers'])
        note = SalesforceNote(**payload)
        url = util.get_url(context) + "sobjects/Note"

        note_data = {
              "Body": note.body,
              "ParentId": note.parent,
              "Title": note.title,
        }

        if note.owner_id is not None:
            note_data["OwnerId"] = note.owner_id

        if note.private is not None:
            note_data["IsPrivate"] = note.private

        response = util.rest("POST", url, access_token, note_data)

        return json.loads(response.text)

    def create_task(self, context, payload):
        """ Create new task """

        access_token = util.get_access_token(context['headers'])
        task = SalesforceTask(**payload)
        url = util.get_url(context) + "sobjects/Task"

        task_data = {
              "Subject": task.subject,
              "ActivityDate": util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', task.end_date),
              "WhoId": task.name_id,
              "WhatId": task.related_to,
              "OwnerId": task.assigned_to,
              "Status": task.status
        }

        response = util.rest("POST", url, access_token, task_data)

        return json.loads(response.text)

    def update_contact(self, context, payload):
        """ Update existing contact """

        access_token = util.get_access_token(context['headers'])
        contact = SalesforceContact(**payload)
        url = util.get_url(context) + "composite/batch"

        contact_data = {
            "Salutation": contact.salutation,
            "LastName": contact.last_name,
            "FirstName": contact.first_name,
            "AccountId": contact.account_id,
            "Title": contact.title,
            "Department": contact.department,
            "Birthdate": contact.birth_date,
            "ReportsToId": contact.reports_to,
            "LeadSource": contact.lead_source,
            "Phone": contact.phone,
            "HomePhone": contact.homephone,
            "MobilePhone": contact.mobile,
            "OtherPhone": contact.other_mobile,
            "Fax": contact.fax,
            "Email": contact.email,
            "AssistantName": contact.assistant,
            "AssistantPhone": contact.asst_mobile,
            "MailingStreet": contact.mailing_street,
            "MailingCity": contact.mailing_city,
            "MailingState": contact.mailing_state,
            "MailingPostalCode": contact.mailing_zip,
            "MailingCountry": contact.mailing_country,
            "OtherStreet": contact.other_street,
            "OtherCity": contact.other_city,
            "OtherState": contact.other_state,
            "OtherPostalCode": contact.other_zip,
            "OtherCountry": contact.other_country,
            "Languages__c": contact.languages,
            "Level__c": contact.level,
            "Description": contact.description
        }

        if contact.owner_id is not None:
            contact_data["OwnerId"] = contact.owner_id

        data = {
            "batchRequests": [
                {
                    "method": "PATCH",
                    "url": f"v52.0/sobjects/Contact/{contact.contact_id}",
                    "richInput": contact_data
                },
                {
                    "method": "GET",
                    "url": f"v52.0/sobjects/Contact/{contact.contact_id}"
                }
            ]
        }

        response = util.rest("POST", url, access_token, data)

        return json.loads(response.text)

    def update_opportunities(self, context, payload):
        """ Update existing opportunity """

        access_token = util.get_access_token(context['headers'])
        opportunity = SalesforceOpportunity(**payload)
        url = util.get_url(context) + "composite/batch"

        opportunity_data = {
                "AccountId": opportunity.account_id,
                "Amount": opportunity.amount,
                "Name": opportunity.opportunity_name,
                "CloseDate": opportunity.end_date,
                "Type": opportunity.type,
                "LeadSource": opportunity.lead_source,
                "NextStep": opportunity.next_step,
                "StageName": opportunity.stage,
                "OrderNumber__c": opportunity.order_number,
                "CurrentGenerators__c": opportunity.current_generator,
                "TrackingNumber__c": opportunity.tracking_number,
                "MainCompetitors__c": opportunity.main_competitor,
                "DeliveryInstallationStatus__c": opportunity.delivery_status,
                "Description": opportunity.description,
        }

        if opportunity.owner_id is not None:
            opportunity_data["OwnerId"] = opportunity.owner_id

        if opportunity.probability is not None:
            opportunity_data["Probability"] = opportunity.probability.rstrip('%')

        if opportunity.private is not None:
            opportunity_data["IsPrivate"] = opportunity.private

        data = {
            "batchRequests": [
                {
                    "method": "PATCH",
                    "url": f"v52.0/sobjects/Opportunity/{opportunity.deal_id}",
                    "richInput": opportunity_data
                },
                {
                    "method": "GET",
                    "url": f"v52.0/sobjects/Opportunity/{opportunity.deal_id}"
                }
            ]
        }

        response = util.rest("POST", url, access_token, data)

        return json.loads(response.text)

    def update_account(self, context, payload):
        """ Update existing account """

        access_token = util.get_access_token(context['headers'])
        account = SalesforceAccount(**payload)
        url = util.get_url(context) + "composite/batch"

        account_data = {
            "Name": account.account_name,
            "ParentId": account.parent_id,
            "AccountNumber": account.account_number,
            "Site": account.account_site,
            "Type": account.type,
            "Industry": account.industry,
            "AnnualRevenue": account.annual_revenue,
            "Rating": account.rating,
            "Phone": account.phone,
            "Fax": account.fax,
            "Website": account.website,
            "TickerSymbol": account.ticker_symbol,
            "Ownership": account.ownership,
            "NumberOfEmployees": account.employees,
            "Sic": account.sic_code,
            "BillingStreet": account.billing_street,
            "BillingCity": account.billing_city,
            "BillingPostalCode": account.billing_zip,
            "BillingState": account.billing_state,
            "BillingCountry": account.billing_country,
            "ShippingStreet": account.shipping_street,
            "ShippingCity": account.shipping_city,
            "ShippingPostalCode": account.shipping_zip,
            "ShippingState": account.shipping_state,
            "ShippingCountry": account.shipping_country,
            "CustomerPriority__c": account.customer_priority,
            "SLAExpirationDate__c": account.end_date,
            "NumberofLocations__c": account.number_of_locations,
            "Active__c": account.active,
            "SLA__c": account.sla,
            "SLASerialNumber__c": account.sla_serial_number,
            "UpsellOpportunity__c": account.upsell_opportunity,
            "Description": account.description
        }

        if account.owner_id is not None:
            account_data["OwnerId"] = account.owner_id

        data = {
            "batchRequests": [
                {
                    "method": "PATCH",
                    "url": f"v52.0/sobjects/Account/{account.account_id}",
                    "richInput": account_data
                },
                {
                    "method": "GET",
                    "url": f"v52.0/sobjects/Account/{account.account_id}"
                }
            ]
        }

        response = util.rest("POST", url, access_token, data)

        return json.loads(response.text)

    def update_lead(self, context, payload):
        """ Update existing lead """

        access_token = util.get_access_token(context['headers'])
        lead = SalesforceLead(**payload)
        url = util.get_url(context) + "composite/batch"

        lead_data = {
            "Salutation": lead.salutation,
            "LastName": lead.last_name,
            "FirstName": lead.first_name,
            "Company": lead.company,
            "Title": lead.title,
            "LeadSource": lead.lead_source,
            "Industry": lead.industry,
            "AnnualRevenue": lead.annual_revenue,
            "Phone": lead.phone,
            "MobilePhone": lead.mobile,
            "Fax": lead.fax,
            "Email": lead.email,
            "Website": lead.website,
            "Status": lead.lead_status,
            "Rating": lead.rating,
            "NumberOfEmployees": lead.no_employees,
            "ProductInterest__c": lead.product_interest,
            "SICCode__c": lead.sic_code,
            "CurrentGenerators__c": lead.current_generator,
            "NumberofLocations__c": lead.no_locations,
            "Street": lead.street,
            "City": lead.city,
            "PostalCode": lead.postal_code,
            "Country": lead.country,
            "State": lead.state,
            "Primary__c": lead.primary,
            "Description": lead.description
        }

        if lead.owner_id is not None:
            lead_data["OwnerId"] = lead.owner_id

        data = {
            "batchRequests": [
                {
                    "method": "PATCH",
                    "url": f"v52.0/sobjects/Lead/{lead.lead_id}",
                    "richInput": lead_data
                },
                {
                    "method": "GET",
                    "url": f"v52.0/sobjects/Lead/{lead.lead_id}"
                }
            ]
        }

        response = util.rest("POST", url, access_token, data)

        return json.loads(response.text)
