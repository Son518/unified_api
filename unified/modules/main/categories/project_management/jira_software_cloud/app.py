from unified.core.app import App, AuthInfo
from project_management.jira_software_cloud.actions import JiraSoftwareCloudActions
from project_management.jira_software_cloud.triggers import JiraSoftwareCloudTriggers
from project_management.jira_software_cloud.api import JiraSoftwareCloudApi


class JirasoftwarecloudApp(App, JiraSoftwareCloudActions, JiraSoftwareCloudTriggers, JiraSoftwareCloudApi):

    def __init__(self):
        super().__init__(
            name = "JiraSoftwareCloud",
            description = "JiraSoftwareCloud is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
            category = "Project management",
            logo = "https://logo.500apps.com/JiraSoftwareCloud",
            auth_info = None,
            auth_type = 'oauth2')
