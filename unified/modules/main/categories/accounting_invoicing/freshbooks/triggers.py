import json
from accounting_invoicing.freshbooks import util
from core.triggers import Triggers
from accounting_invoicing.freshbooks.entities.freshbooks_client import FreshbooksClient
from accounting_invoicing.freshbooks.entities.freshbooks_estimate import FreshbooksEstimate
from accounting_invoicing.freshbooks.entities.freshbooks_invoice import FreshbooksInvoice
from accounting_invoicing.freshbooks.entities.freshbooks_expense import FreshbooksExpense
from accounting_invoicing.freshbooks.entities.freshbooks_project import FreshbooksProject
from accounting_invoicing.freshbooks.entities.freshbooks_time_entry import FreshbooksTimeentry


class FreshbooksTriggers(Triggers):

    def new_client(self,context,payload):
        """
        triggers when new_client create 
        context holds the headers 
        """
        client_obj1=FreshbooksClient(
                                    name=payload["name"],
                                    object_id=payload["object_id"],
                                    user_id=payload["user_id"],
                                    account_id=payload["account_id"]
                                    )
        return client_obj1.__dict__

    def new_estimate(self,context,payload):
        """
        triggers when new_estimate create 
        context holds the headers 
        """
        estimate_obj=FreshbooksEstimate(
                                        name=payload["name"],
                                        object_id=payload["object_id"],
                                        user_id=payload["user_id"],
                                        account_id=payload["account_id"]
                                        )
        return estimate_obj.__dict__

    def new_expense(self,context,payload):
        """
        triggers when new_expense create 
        context holds the headers 
        """
        expense_obj=FreshbooksExpense(
                                    name=payload["name"],
                                    object_id=payload["object_id"],
                                    user_id=payload["user_id"],
                                    account_id=payload["account_id"]
                                    )
        return expense_obj.__dict__

    def new_invoice(self,context,payload):
        """
        triggers when new_invoice create 
        context holds the headers 
        """
        invoice_obj=FreshbooksInvoice(
                                    name=payload["name"],
                                    object_id=payload["object_id"],
                                    user_id=payload["user_id"],
                                    account_id=payload["account_id"]
                                    )
        return invoice_obj.__dict__

    def new_time_entry(self,context,payload):
        """
        triggers when new_timeentry( create 
        context holds the headers 
        """
        timeentry_obj=FreshbooksTimeentry(
                                    name=payload["name"],
                                    object_id=payload["object_id"],
                                    account_id=payload["account_id"],
                                    business_id=payload["business_id"]
                                    )
        return timeentry_obj.__dict__

    def new_project(self,context,payload):
        """
        triggers when new_project create 
        context holds the headers 
        """
        project_obj=FreshbooksProject(
                                    name=payload["name"],
                                    object_id=payload["object_id"],
                                    account_id=payload["account_id"]
                                    )
        return project_obj.__dict__

    def updated_estimate(self,context,payload):
        """
        triggers when estimate updated 
        context holds the headers 
        holds the request.body
        """
        estimate1=FreshbooksEstimate(
                                    name=payload["name"],
                                    object_id=payload["object_id"],
                                    user_id=payload["user_id"],
                                    account_id=payload["account_id"]
                                    )
        return estimate1.__dict__

    def updated_invoice(self,context,payload):
        """
        triggers when invoice updated 
        context holds the headers 
        """
        invoice_obj=FreshbooksInvoice(
                                name=payload["name"],
                                object_id=payload["object_id"],
                                user_id=payload["user_id"],
                                account_id=payload["account_id"]
                                )
        return invoice_obj.__dict__

    def updated_project(self,context,payload):
        """
        triggers when project updated 
        context holds the headers 
        """
        project1=FreshbooksProject(
                                    name=payload["name"],
                                    object_id=payload["object_id"],
                                    account_id=payload["account_id"]
                                    )
        return project1.__dict__

    def new_invoice_payment(self,context,payload):
        """
        triggers when invoice payment added 
        context holds the headers 
        """
        payment=FreshbooksInvoice(
                                name=payload["name"],
                                object_id=payload["object_id"],
                                user_id=payload["user_id"],
                                account_id=payload["account_id"]
                                )
        return payment.__dict__
