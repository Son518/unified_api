from unified.core.triggers import Triggers
from project_management.teamwork.entities.teamwork_project import TeamworkProject
from project_management.teamwork.entities.teamwork_task import TeamworkTask
from project_management.teamwork.entities.teamwork_comment import TeamworkComment
from project_management.teamwork.entities.teamwork_message import TeamworkMessage
from project_management.teamwork.entities.teamwork_user import TeamworkUser
from project_management.teamwork.entities.teamwork_timeentry import TeamworkTimeentry
from project_management.teamwork.entities.teamwork_calendarevent import TeamworkCalendarevent
from project_management.teamwork.entities.teamwork_card import TeamworkCard
from project_management.teamwork.entities.teamwork_column import TeamworkColumn
from project_management.teamwork.entities.teamwork_company import TeamworkCompany
from project_management.teamwork.entities.teamwork_expense import TeamworkExpense
from project_management.teamwork.entities.teamwork_file import TeamworkFile
from project_management.teamwork.entities.teamwork_link import TeamworkLink
from project_management.teamwork.entities.teamwork_invoice import TeamworkInvoice
from project_management.teamwork.entities.teamwork_messagereply import TeamworkMessagereply
from project_management.teamwork.entities.teamwork_milestone import TeamworkMilestone
from project_management.teamwork.entities.teamwork_notebook import TeamworkNotebook
from project_management.teamwork.entities.teamwork_risk import TeamworkRisk
from project_management.teamwork.entities.teamwork_status import TeamworkStatus

class TeamworkTriggers(Triggers):

    def new_project(self, context, payload):
        ''' triggers when new  project created'''
        project = TeamworkProject(
            project_description=payload["project"]["description"],
            end_date=payload["project"]["endDate"],
            id=payload["project"]["id"],
            project_name=payload["project"]["name"],
            start_date=payload["project"]["startDate"],
            status=payload["project"]["status"],
            tags=payload["project"]["tags"],
            owner_id=payload["project"]["ownerId"],
            company_id=payload["project"]["companyId"],
            category_id=payload["project"]["categoryId"],
            created_date=payload["project"]["dateCreated"])

        return project.__dict__

    def new_task(self, context, payload):
        ''' triggers when new  task created'''

        task = TeamworkTask(
            description=payload["task"]["description"],
            assigned_user_ids=payload["task"]["assignedUserIds"],
            parent_id=payload["task"]["parentId"],
            progress=payload["task"]["progress"],
            date_created=payload["task"]["dateCreated"],
            estimated_minutes=payload["task"]["estimatedMinutes"],
            due_date=payload["task"]["dueDate"],
            id=payload["task"]["id"],
            tags=payload["task"]["tags"],
            name=payload["task"]["name"],
            project_id=payload["task"]["projectId"],
            start_date=payload["task"]["startDate"],
            has_custom_fields=payload["task"]["hasCustomFields"],
            status=payload["task"]["status"],
            tasklist_id=payload["task"]["taskListId"],
            date_updated=payload["task"]["dateUpdated"])

        return task.__dict__

    def new_comment(self, context, payload):
        ''' triggers when new  comment created '''

        comment = TeamworkComment(
            created_date=payload["comment"]["dateCreated"],
            comment_description=payload["comment"]["body"],
            id=payload["comment"]["id"],
            project_id=payload["comment"]["projectId"],
            task_id=payload["comment"]["objectId"],
            updated_date=payload["comment"]["dateUpdated"])

        return comment.__dict__

    def new_tasklist(self, context, payload):
        ''' triggers when new  tasklist created'''
        tasklist = TeamworkTask(
            description=payload["taskList"]["description"],
            id=payload["taskList"]["id"],
            name=payload["taskList"]["name"],
            project_id=payload["taskList"]["projectId"],
            status=payload["taskList"]["status"],
            milestone_id=payload["taskList"]["milestoneId"],
            template_id=payload["taskList"]["templateId"])

        return tasklist.__dict__

    def updated_project(self, context, payload):
        ''' triggers when new  project updated or deleted '''
        project = TeamworkProject(project_description=payload["project"]["description"],
                                        project_id=payload["project"]["id"],
                                        end_date=payload["project"]["endDate"],
                                        id=payload["project"]["id"],
                                        project_name=payload["project"]["name"],
                                        start_date=payload["project"]["startDate"],
                                        status=payload["project"]["status"],
                                        tags=payload["project"]["tags"],
                                        owner_id=payload["project"]["ownerId"],
                                        company_id=payload["project"]["companyId"],
                                        category_id=payload["project"]["categoryId"],
                                        created_date=payload["project"]["dateCreated"]
                                        )
        return project.__dict__

    def delete_project(self, context, payload):
        ''' triggers when new  project updated or deleted '''
        project = TeamworkProject(id=payload["id"],
                                    project_id=payload["id"],
                                    avatar=payload["eventCreator"]["avatar"]
                                    )
        return project.__dict__


    def new_message(self, context, payload):
        ''' triggers when new  message created'''
        message = TeamworkMessage(
            id=payload["message"]["id"],
            subject=payload["message"]["subject"],
            status=payload["message"]["status"],
            category_id=payload["message"]["categoryId"],
            project_id=payload["message"]["projectId"]
        )
        return message.__dict__

    def new_time_entry(self, context, payload):
        ''' triggers when new  new time entry created'''

        time_entry = TeamworkTimeentry(
            id=payload["time"]["id"],
            hours=payload["time"]["hours"],
            minutes=payload["time"]["minutes"],
            date=payload["time"]["date"],
            task_id=payload["time"]["taskId"],
            project_id=payload["time"]["projectId"],
            description=payload["time"]["description"],
            created_date=payload["time"]["dateCreated"],
            updated_date=payload["time"]["dateUpdated"]
        )
        return time_entry.__dict__

    def new_person(self, context, payload):
        ''' triggers when new  user created'''

        user = TeamworkUser(
            people_id=payload['user']['id'],
            first_name=payload["user"]["firstName"],
            last_name=payload["user"]["lastName"],
            user_type=payload["user"]["type"],
            created_date=payload["user"]["dateCreated"],
            updated_date=payload["user"]["dateUpdated"]
        )
        return user.__dict__

    def updated_task(self, context, payload):
        ''' triggers when new  task updated or deleted '''
        task = TeamworkTask(description=payload["task"]["description"],
                                assigned_user_ids=payload["task"]["assignedUserIds"],
                                parent_id=payload["task"]["parentId"],
                                progress=payload["task"]["progress"],
                                date_created=payload["task"]["dateCreated"],
                                estimated_minutes=payload["task"]["estimatedMinutes"],
                                due_date=payload["task"]["dueDate"],
                                id=payload["task"]["id"],
                                tags=payload["task"]["tags"],
                                name=payload["task"]["name"],
                                project_id=payload["task"]["projectId"],
                                start_date=payload["task"]["startDate"],
                                has_custom_fields=payload["task"]["hasCustomFields"],
                                status=payload["task"]["status"],
                                tasklist_id=payload["task"]["taskListId"],
                                date_updated=payload["task"]["dateUpdated"])
        return task.__dict__

    def delete_task(self, context, payload):
        ''' triggers when new  task updated or deleted '''
        
        task = TeamworkTask(id=payload["id"],
                                    project_id=payload["id"],
                                    avatar=payload["eventCreator"]["avatar"]
                                    )
        return task.__dict__

    def new_calendar_event(self,context,payload):
        ''' triggers when new  calendar event created'''

        calendar_event = TeamworkCalendarevent(id=payload["event"]["id"],
                                                title=payload["event"]["title"],
                                                description=payload["event"]["description"],
                                                where=payload["event"]["where"],
                                                start_date=payload["event"]["start"],
                                                end_date=payload["event"]["end"],
                                                reminders=payload["event"]["reminders"],
                                                attendees=payload["event"]["attendees"],
                                                created_date=payload["event"]["dateCreated"],
                                                updated_date=payload["event"]["dateUpdated"])

        return calendar_event.__dict__

    def new_card(self,context,payload):
        ''' triggers when new  card created'''

        card = TeamworkCard(id=payload["card"]["id"],
                            column_id=payload["card"]["columnId"],
                            task_id=payload["card"]["taskId"],
                            project_id=payload["card"]["projectId"],
                            status=payload["card"]["status"],
                            name=payload["card"]["name"],
                            created_date=payload["card"]["dateCreated"],
                            updated_date=payload["card"]["dateUpdated"],
                            start_date=payload["card"]["startDate"],
                            due_date=payload["card"]["dueDate"],
                            tags=payload["card"]["tags"],
                            columns=payload["column"])

        return card.__dict__

    def new_column(self,context,payload):
        ''' triggers when new  column created'''

        column = TeamworkColumn(id=payload["column"]["id"],
                                name=payload["column"]["name"],
                                color=payload["column"]["color"],
                                status=payload["column"]["status"],
                                created_date=payload["column"]["dateCreated"],
                                updated_date=payload["column"]["dateUpdated"],
                                project_id=payload["column"]["projectId"])

        return column.__dict__

    def new_company(self,context,payload):
        ''' triggers when new  company created'''
        company = TeamworkCompany(id=payload["company"]["id"],
                                name=payload["company"]["name"],
                                website=payload["company"]["website"],
                                phone=payload["company"]["phone"],
                                fax=payload["company"]["fax"],
                                city=payload["company"]["city"],
                                state=payload["company"]["state"],
                                zip=payload["company"]["zip"],
                                country_code=payload["company"]["countryCode"],
                                email=payload["company"]["email"],
                                address=payload["company"]["addressLine1"])
        return company.__dict__

    def new_expense(self,context,payload):
        ''' triggers when new  expense created'''

        expense = TeamworkExpense(id=payload["expense"]["id"],
                                name=payload["expense"]["name"],
                                description=payload["expense"]["description"],
                                date=payload["expense"]["date"],
                                cost=payload["expense"]["cost"],
                                invoice_id=payload["expense"]["invoiceId"],
                                project_id=payload["expense"]["projectId"],
                                updated_date=payload["expense"]["dateUpdated"])
        
        return expense.__dict__

    def new_file(self,context,payload):
        ''' triggers when new  file created'''

        file = TeamworkFile(id=payload["file"]["id"],
                            version=payload["file"]["version"],
                            description=payload["file"]["description"],
                            category_id=payload["file"]["categoryId"],
                            project_id=payload["file"]["projectId"],
                            tags=payload["file"]["tags"],
                            updated_date=payload["file"]["dateUpdated"],
                            version_id=payload["file"]["versionId"],
                            name=payload["file"]["name"],
                            size=payload["file"]["size"],
                            url=payload["file"]["thumbUrl"],
                            created_date=payload["file"]["dateCreated"])

        return file.__dict__

    def new_invoice(self,context,payload):
        ''' triggers when new  invoice created'''

        invoice = TeamworkInvoice(id=payload["invoice"]["id"],
                                number=payload["invoice"]["number"],
                                po_number=payload["invoice"]["poNumber"],
                                description=payload["invoice"]["description"],
                                date=payload["invoice"]["date"],
                                status=payload["invoice"]["status"],
                                currency_code=payload["invoice"]["currencyCode"],
                                fixed_cost=payload["invoice"]["fixedCost"],
                                project_id=payload["invoice"]["projectId"],
                                company_id=payload["invoice"]["companyId"],
                                created_date=payload["invoice"]["dateCreated"],
                                updated_date=payload["invoice"]["dateUpdated"])

        return invoice.__dict__

    def new_link(self,context,payload):
        ''' triggers when new  link created'''

        link = TeamworkLink(id=payload["link"]["id"],
                            title=payload["link"]["title"],
                            description=payload["link"]["description"],
                            code=payload["link"]["code"],
                            width=payload["link"]["width"],
                            height=payload["link"]["height"],
                            tags=payload["link"]["tags"],
                            link=payload["link"]["categoryId"],
                            project_id=payload["link"]["projectId"],
                            created_date=payload["link"]["dateCreated"],
                            updated_date=payload["link"]["dateUpdated"])
        return link.__dict__

    def new_message_reply(self,context,payload):
        ''' triggers when new  messafe reply created'''
        reply = TeamworkMessagereply(id=payload["messagePost"]["id"],
                                    body=payload["messagePost"]["body"],
                                    content_type=payload["messagePost"]["contentType"],
                                    status=payload["messagePost"]["status"],
                                    user_id=payload["messagePost"]["userId"],
                                    message_id=payload["messagePost"]["messageId"],
                                    created_date=payload["messagePost"]["dateCreated"],
                                    updated_date=payload["messagePost"]["dateUpdated"])

        return reply.__dict__

    def new_milestone(self,context,payload):
        ''' triggers when new  milestone created'''

        milestone =  TeamworkMilestone(milestone_id=payload["milestone"]["id"],
                                        name=payload["milestone"]["name"],
                                        description=payload["milestone"]["description"],
                                        deadline=payload["milestone"]["deadline"],
                                        status=payload["milestone"]["status"],
                                        project_id=payload["milestone"]["projectId"],
                                        tasklist_id=payload["milestone"]["tasklistIds"],
                                        created_date=payload["milestone"]["dateCreated"],
                                        updated_date=payload["milestone"]["dateUpdated"],
                                        tags=payload["milestone"]["tags"],
                                        responsible_party_id=payload["milestone"]["responsiblePartyIds"],
                                        tasklists=payload["taskLists"],
                                        users=payload["users"])

        return milestone.__dict__

    def new_notebook(self,context,payload):
        ''' triggers when new  notebook created'''

        notebook = TeamworkNotebook(id=payload["notebook"]["id"],
                                    name=payload["notebook"]["name"],
                                    description=payload["notebook"]["description"],
                                    tags=payload["notebook"]["tags"],
                                    category_id=payload["notebook"]["categoryId"],
                                    project_id=payload["notebook"]["projectId"],
                                    created_date=payload["notebook"]["dateCreated"],
                                    version=payload["notebook"]["version"],
                                    version_id=payload["notebook"]["versionId"])
        return notebook.__dict__

    def new_risk(self,context,payload):
        ''' triggers when new  risk created'''

        risk = TeamworkRisk(id=payload["risk"]["id"],
            source=payload["risk"]["source"],
            probability=payload["risk"]["probability"],
            probability_value=payload["risk"]["probabilityValue"],
            impact=payload["risk"]["impact"],
            impact_value=payload["risk"]["impactValue"],
            result=payload["risk"]["result"],
            impact_cost=payload["risk"]["impactCost"],
            impact_performance=payload["risk"]["impactPerformance"],
            impact_schedule=payload["risk"]["impactSchedule"],
            mitigation_plan=payload["risk"]["mitigationPlan"],
            status=payload["risk"]["status"],
            project_id=payload["risk"]["projectId"],
            created_date=payload["risk"]["dateCreated"],
            updated_date=payload["risk"]["dateUpdated"])

        return risk.__dict__

    def new_status(self,context,payload):
        ''' triggers when new  status created'''

        status = TeamworkStatus(id=payload["status"]["id"],
                                user_id=payload["status"]["userId"],
                                date=payload["status"]["date"],
                                message=payload["status"]["message"])

        return status.__dict__

    