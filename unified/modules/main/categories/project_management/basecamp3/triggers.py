from unified.core.triggers import Triggers
from project_management.basecamp3.entities.basecamp3_task import Basecamp3Task
from project_management.basecamp3.entities.basecamp3_comment import Basecamp3Comment
from project_management.basecamp3.entities.basecamp3_tasklist import Basecamp3Tasklist
from project_management.basecamp3.entities.basecamp3_message import Basecamp3Message
from project_management.basecamp3.entities.basecamp3_document import Basecamp3Document
from project_management.basecamp3.entities.basecamp3_fileupload import Basecamp3FileUpload
from project_management.basecamp3.entities.basecamp3_schedule_entry import Basecamp3ScheduleEntry


class Basecamp3Triggers(Triggers):

    def new_to_do(self, context, payload):
        '''triggers when new to do is created '''

        return self.new_task(context, payload)

    def new_task(self, context, payload):
        '''triggers when new task is created '''

        task = Basecamp3Task(
            id=payload["id"],
            name=payload["recording"]["title"],
            project_id=payload["recording"]["bucket"]["id"],
            task_id=payload["recording"]["id"],
            assigned_to=payload["creator"]["id"],
            tasklist_id=payload["recording"]["parent"]["id"],
            created_date=payload["recording"]["created_at"]
        )

        return task.__dict__

    def new_comment(self, context, payload):
        '''triggers when new comment is created '''

        comment = Basecamp3Comment(
            id=payload["recording"]["id"],
            comment_description=payload["recording"]["content"],
            task_id=payload["recording"]["parent"]["id"],
            project_id=payload["recording"]["bucket"]["id"],
            created_date=payload["recording"]["created_at"],
            comment_by=payload["recording"]["creator"]["id"]
        )

        return comment.__dict__

    def new_to_do_list(self, context, payload):
        '''triggers when new to do list is created '''

        return self.new_tasklist(context, payload)

    def new_tasklist(self, context, payload):
        '''triggers when new tasklist is created '''

        tasklist = Basecamp3Tasklist(
            id=payload["recording"]["id"],
            name=payload["recording"]["title"],
            description=payload["recording"]["content"],
            project_id=payload["recording"]["bucket"]["id"],
            todoset_id=payload["recording"]["parent"]["id"],
            created_date=payload["recording"]["created_at"]
        )

        return tasklist.__dict__

    def new_message(self, context, payload):
        '''triggers when new message is created '''

        message = Basecamp3Message(
            project_id=payload["recording"]["id"],
            message_board_id=payload["recording"]["parent"]["id"],
            subject=payload["recording"]["title"],
            content=payload["recording"]["content"],
            status=payload["recording"]["status"],
            created_date=payload["recording"]["created_at"],
        )
        return message.__dict__

    def new_document(self, context, payload):
        '''triggers when new document is created '''

        document = Basecamp3Document(
            id=payload["recording"]["id"],
            title=payload["recording"]["title"],
            content=payload["recording"]["content"],
            type=payload["recording"]["type"],
            folder_id=payload["recording"]["parent"]["id"],
            project_id=payload["recording"]["bucket"]["id"],
            uploaded_by=payload["recording"]["creator"]["id"],
            created_date=payload["created_at"],
        )

        return document .__dict__

    def new_upload(self, context, payload):
        '''triggers when new upload is created '''

        return self.new_file_upload(context, payload)

    def new_file_upload(self, context, payload):
        '''triggers when new file upload is uploaded '''

        file = Basecamp3FileUpload(
            id=payload["recording"]["id"],
            title=payload["recording"]["title"],
            notes=payload["recording"]["content"],
            type=payload["recording"]["type"],
            doc_file_id=payload["recording"]["parent"]["id"],
            project_id=payload["recording"]["bucket"]["id"],
            uploaded_by=payload["recording"]["creator"]["id"],
            created_date=payload["created_at"],
        )
        return file.__dict__

    def new_schedule_entry(self, context, payload):
        '''triggers when new schedule entry is created '''

        schedule = Basecamp3ScheduleEntry(
            id=payload["recording"]["id"],
            event_name=payload["recording"]["title"],
            event_description=payload["recording"]["content"],
            schedule_id=payload["recording"]["parent"]["id"],
            project_id=payload["recording"]["bucket"]["id"],
            created_by=payload["recording"]["creator"]["id"],
            created_date=payload["created_at"],
        )
        return schedule.__dict__
