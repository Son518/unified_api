import json
from project_management.pivotal_tracker.actions import PivotaltrackerActions
from project_management.pivotal_tracker.triggers import PivotaltrackerTriggers
from unified.core.app import App, AuthInfo

class PivotaltrackerApp(App,PivotaltrackerActions,PivotaltrackerTriggers):

    def __init__(self):
        super().__init__(
            name="Pivotaltracker",
            description="Pivotal Tracker is a straightforward project-planning tool that helps software development teams form realistic expectations about when work might be completed based on the team's ongoing performance.",
            category="project_management",
            logo="https://logo.500apps.com/pivotaltracker",
            auth_info=None,
            auth_type='Basic')