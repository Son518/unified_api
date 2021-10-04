# from . import module
import json
from teamchat.chatwork.actions import ChatworkActions
from teamchat.chatwork.api import ChatworkApi

from unified.core.app import App, AuthInfo


class ChatworkApp(App, ChatworkActions, ChatworkApi):

    def __init__(self):
        super().__init__(
            name="Chatwork",
            description="Keep your team focused and working together with Chatwork's team chat, tasks, video chats, and more in one place.",
            category="teamchat",
            logo="https://logo.500apps.com/chatwork",
            auth_info=None,
            auth_type='basic')
