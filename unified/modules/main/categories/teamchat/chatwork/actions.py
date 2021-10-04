import json
from core.actions import Actions
from teamchat.chatwork import util
from teamchat.chatwork.entities.chatwork_room import ChatworkRoom
from teamchat.chatwork.entities.chatwork_task import ChatworkTask


class ChatworkActions(Actions):

    def create_task(self, context, task_payload):
        """
        adds task to room
        context holds the headers 
        task_payload holds the request.body
        """
        client = util.get_chatwork_client(context["headers"])
        task_entity = ChatworkTask(**task_payload)
        if task_entity.end_date:
            task_entity.end_date = util.date_format_to_epoch(
                task_entity.end_date)
        response = client.add_rooms_task(
            task_entity.room_id, task_entity.task_description, task_entity.end_date, [task_entity.assignees])
        return response

    def send_message(self, context, message_payload):
        """
        sends message from room
        context holds the headers 
        message_payload holds the request.body
        """
        client = util.get_chatwork_client(context["headers"])
        message_entity = ChatworkRoom(**message_payload)
        response = client.send_message(
            message_entity.room_id, message_entity.text)
        return json.loads(response.text)
