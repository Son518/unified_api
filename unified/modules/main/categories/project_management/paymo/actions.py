import json
import requests
from flask import request,Response
from project_management.paymo import util
from unified.core.actions import Actions
from project_management.paymo.entities.paymo_project import PaymoProject
from project_management.paymo.entities.paymo_task import PaymoTask
from project_management.paymo.entities.paymo_client import PaymoClient
from project_management.paymo.entities.paymo_task_list import PaymoTasklist
from project_management.paymo.entities.paymo_invoice import PaymoInvoice
from project_management.paymo.entities.paymo_expense import PaymoExpense
from project_management.paymo.entities.paymo_timeentry import PaymoTimeEntry


class PaymoActions(Actions):

    def create_project(self, context, payload):
        ''' creates project '''

        access_token = util.get_basic_token(context["headers"])
        task_schema = PaymoProject(**payload)
        
        data = {
            "name": task_schema.project_name,
            "description": task_schema.project_description,
            "billable": task_schema.billable,
            "client_id": task_schema.client_id
            }

        response = util.rest("POST", "https://app.paymoapp.com/api/projects", access_token,data)
        return json.loads(response.text)

    def create_task(self, context,payload):
        ''' creates task'''
              
        access_token = util.get_basic_token(context["headers"])
        task_schema = PaymoTask(**payload)

        data = {
              "project_id": task_schema.project_id,
              "task_list_id": task_schema.task_list_id,
              "name": task_schema.name,
              "description": task_schema.description,
              "priority_id": task_schema.priority_id,
              "start_date": task_schema.start_date,
              "due_date": task_schema.due_date,
              "billable": task_schema.billable,
              "budget_hours": task_schema.budget_hours,
              "price_per_hour": task_schema.price_per_hour,
              "assigned_users": task_schema.assigned_users
              }

        response = util.rest("POST", "https://app.paymoapp.com/api/tasks",access_token,data)
        return json.loads(response.text)

    def create_client(self, context,payload):
        ''' creates client'''
              
        access_token = util.get_basic_token(context["headers"])
        task_schema = PaymoClient(**payload)

        data = {
              "name": task_schema.name,
              "email": task_schema.email,
              "address": task_schema.address,
              "city": task_schema.city,
              "state": task_schema.state,
              "postal_code": task_schema.postal_code,
              "country": task_schema.country,
              "phone": task_schema.phone,
              "fax": task_schema.fax,
              "website_url": task_schema.website_url,
              "fiscal_information": task_schema.fiscal_information
              }

        response = util.rest("POST", "https://app.paymoapp.com/api/clients",access_token,data)
        return json.loads(response.text)

    def create_task_list(self, context,payload):
        ''' creates tasklist'''
              
        access_token = util.get_basic_token(context["headers"])
        task_schema = PaymoTasklist(**payload)

        data = {
              "project_id": task_schema.project_id,
              "name": task_schema.name,
               }

        response = util.rest("POST", "https://app.paymoapp.com/api/tasklists",access_token,data)
        return json.loads(response.text)


    def create_expense(self, context,payload):
        ''' creates expense'''
              
        access_token = util.get_basic_token(context["headers"])
        task_schema = PaymoExpense(**payload)

        data = {
              "client_id": task_schema.client_id,
              "name": task_schema.name,
              "amount": task_schema.amount,
              "currency": task_schema.currency,
              "date": task_schema.date,
              "notes": task_schema.notes
             
              }

        response = util.rest("POST", "https://app.paymoapp.com/api/expenses",access_token,data)
        return json.loads(response.text)


    def create_invoice(self, context,payload):
        ''' creates invoice'''
        
        access_token = util.get_basic_token(context["headers"])
        task_schema = PaymoInvoice(**payload)

        data = {
              "template_id": task_schema.template_id,
              "client_id": task_schema.client_id,
              "status": task_schema.status,
              "currency": task_schema.currency,
              "start_date": task_schema.start_date,
              "due_date": task_schema.due_date,
              "tax_percentage": task_schema.tax_percentage,
              "bill_to": task_schema.bill_to,
              "company_info": task_schema.company_info,
              "footer": task_schema.footer,
              "notes": task_schema.notes,
              "out_standing": task_schema.out_standing,
              "tax_text": task_schema.tax_text,
              "tax_2": task_schema.tax_2,
              "tax_on_tax": task_schema.tax_on_tax,
              "tax_2_tax": task_schema.tax_2_tax,
              "pay_online": task_schema.pay_online
            
              }

        response = util.rest("POST", "https://app.paymoapp.com/api/invoices",access_token,data)
        return json.loads(response.text)

    def create_time_entry(self, context,payload):
        ''' creates TimeEntry'''
        
        access_token = util.get_basic_token(context["headers"])
        task_schema = PaymoTimeEntry(**payload)

        data = {
              "project_id": task_schema.project_id,
              "task_list_id": task_schema.task_list_id,
              "task_id": task_schema.task_id,
              "start_time": task_schema.start_time,
              "end_time": task_schema.end_time,
              "description": task_schema.description
              }

        response = util.rest("POST", "https://app.paymoapp.com/api/entries",access_token,data)
        return json.loads(response.text)
