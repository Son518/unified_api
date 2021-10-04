from unified.core.triggers import Triggers
from project_management.paymo.entities.paymo_project import PaymoProject
from project_management.paymo.entities.paymo_task import PaymoTask
from project_management.paymo.entities.paymo_client import PaymoClient
from project_management.paymo.entities.paymo_task_list import PaymoTasklist
from project_management.paymo.entities.paymo_invoice import PaymoInvoice
from project_management.paymo.entities.paymo_report import PaymoReport
from project_management.paymo.entities.paymo_timeentry import PaymoTimeEntry


class PaymoTriggers(Triggers):

    def new_project(self, context, payload):
        ''' triggers when new  project created'''
        project = PaymoProject(

            name=payload["client"]["name"],
            code=payload["code"],
            client_id=payload["client_id"],
            workflow_id=payload["workflow_id"],
            status_id=payload["status_id"],
            hourly_billing_mode=payload["hourly_billing_mode"],
            budget_hours=payload["budget_hours"],
            price_per_hour=payload["price_per_hour"],
            estimated_price=payload["estimated_price"],
            invoiced=payload["invoiced"],
            invoice_item_id=payload["invoice_item_id"],
            billing_type=payload["billing_type"],
            managers=payload["managers"],
        )

        return project.__dict__

    def new_task(self, context, payload):
        ''' triggers when new  task created'''
        Task = PaymoTask(

            id=payload["id"],
            name=payload["name"],
            code=payload["code"],
            project_id=payload["project_id"],
            user_id=payload["user_id"],
            cover_file_id=payload["cover_file_id"],
            status_id=payload["status_id"],
            billable=payload["billable"],
            description=payload["description"],
            price_per_hour=payload["price_per_hour"],
            estimated_price=payload["estimated_price"],
            price=payload["price"],
            invoiced=payload["invoiced"],
            invoice_item_id=payload["invoice_item_id"],
            due_date=payload["due_date"],
            start_date=payload["start_date"],
        )

        return Task.__dict__

    def new_client(self, context, payload):
        ''' triggers when new client created'''
        Client = PaymoClient(
            name=payload["name"],
            address=payload["address"],
            city=payload["city"],
            state=payload["state"],
            postal_code=payload["postal_code"],
            country=payload["country"],
            phone=payload["phone"],
            fax=payload["fax"],
            email=payload["email"],
            fiscal_information=payload["fiscal_information"],
            id=payload["id"],
            created_on=payload["created_on"],
            updated_on=payload["updated_on"],
        )
        return Client.__dict__

    def new_task_list(self, context, payload):
        ''' triggers when new tasklist created'''
        Tasklist = PaymoTasklist(

            id=payload["id"],
            name=payload["name"],
            project_id=payload["project_id"],
            seq=payload["seq"],
            milestone=payload["milestone_id"],
            created_on=payload["created_on"],
            updated_on=payload["updated_on"],
        )
        return Tasklist.__dict__

    def new_invoice(self, context, payload):
        ''' triggers when new invoice created'''
        Invoice = PaymoInvoice(

            id=payload["id"],
            client_id=payload["client_id"],
            template_id=payload["template_id"],
            title=payload["title"],
            status=payload["status"],
            currency=payload["currency"],
            due_date=payload["due_date"],
            delivery_date=payload["delivery_date"],
            tax=payload["tax"],
            tax2=payload["tax2"],
            tax_amount=payload["tax_amount"],
            tax_on_tax=payload["tax_on_tax"],
            bill_to=payload["bill_to"],
            company_info=["company_info"],
            footer=payload["footer"],
            pay_online=payload["pay_online"],
            download_token=payload["download_token"],
            pdf_link=payload["pdf_link"],
            token=payload["token"],
            invoice_id=payload["invoiceitems"][0]["invoice_id"],
            item=payload["invoiceitems"][0]["item"],
            description=payload["invoiceitems"][0]["description"],
            price_unit=payload["invoiceitems"][0]["price_unit"],
            quantity=payload["invoiceitems"][0]["quantity"],
        )
        return Invoice.__dict__

    def new_time_entry(self, context, payload):
        ''' triggers when new time entry created'''
        TimeEntry = PaymoTimeEntry(

            id=payload["id"],
            task_id=payload["task_id"],
            user_id=payload["user_id"],
            description=payload["description"],
            invoice_item_id=payload["invoice_item_id"],
            billed=payload["billed"],
            project_id=payload["project_id"],
            created_on=payload["created_on"],
            updated_on=payload["updated_on"],
            date=payload["date"],
        )
        return TimeEntry.__dict__

    def new_report(self, context, payload):
        ''' triggers when new report created'''
        Report = PaymoReport(

            id=payload["id"],
            name=payload["name"],
            user_id=payload["user_id"],
            type=payload["type"],
            active=payload["active"],
            share_client_id=payload["share_client_id"],
            share_users_ids=payload["share_users_ids"],
            start_date=payload["start_date"],
            end_date=payload["end_date"],
            date_interval=payload["date_interval"],
            projects=payload["projects"],
            users=payload["users"],
            clients=payload["clients"],
        )
        return Report.__dict__
