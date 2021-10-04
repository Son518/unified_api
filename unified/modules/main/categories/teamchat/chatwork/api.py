import json
from teamchat.chatwork import util
from teamchat.chatwork.entities.chatwork_room import ChatworkRoom
from teamchat.chatwork.entities.chatwork_task import ChatworkTask


class ChatworkApi():

    def room(self, context, params):
        """
        gets a room using room_id
        context holds the headers 
        param holds room_id
        """
        client = util.get_chatwork_client(context["headers"])
        room = client.get_rooms_by_id(params["room_id"])
        room_obj = ChatworkRoom(name=room["name"],
                                description=room["description"],
                                icon=room["icon_path"],
                                room_id=room["room_id"]
                                )
        return room_obj.__dict__

    def chatroom_task(self, context, params):
        """
        gets a task from using room_id and task_id
        context holds the headers 
        params holds room_id,task_id
        """
        client = util.get_chatwork_client(context["headers"])
        task = client.get_rooms_task_information(
            params["room_id"], params["task_id"])
        task_obj = ChatworkTask(task_description=task["body"],
                                end_date=str(task["limit_time"]),
                                task_id=task["task_id"]
                                )
        return task_obj.__dict__

    def profile(self, context, params):
        """
        get call to show authenticated user information
        """
        client = util.get_chatwork_client(context["headers"])
        response = client.get_me()
        profile = {
            'id':response['account_id'],
            'name':response['name'],
            'email':response['login_mail']
        }
        return profile
    
    def verify(self, context, params):
        """
        get call to verify user authenticated information
        """
        client = util.get_chatwork_client(context["headers"])
        response = client.get_me()
        return response