from unified.core.app import App, AuthInfo
from customer_support.jira_service_desk.actions import JiraservicedeskActions
from customer_support.jira_service_desk.triggers import JiraservicedeskTriggers

class JiraservicedeskApp(App, JiraservicedeskActions, JiraservicedeskTriggers):

    def __init__(self):
        super().__init__(
            name = "Jira ServiceDesk",
            description = "Jira's service desk empowers teams to deliver great service experiences and ensures your employees and customers can get help quickly.",
            category = "Customer Support",
            logo = "https://logo.500apps.com/jiraservicedesk",
            auth_info = None,
            auth_type = 'oauth2')
