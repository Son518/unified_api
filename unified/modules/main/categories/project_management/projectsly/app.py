from unified.core.app import App, AuthInfo
from project_management.projectsly.triggers import ProjectslyTriggers

class ProjectslyApp(App, ProjectslyTriggers):

    def __init__(self):

        super().__init__(
            name="Projectsly",
            description="Plan your work well, track it effectively, and collaborate with your team members efficiently like never before.",
            category="Project management",
            logo="https://logo.500apps.com/projectsly",
            auth_info=None,
            auth_type='basic'
        )
