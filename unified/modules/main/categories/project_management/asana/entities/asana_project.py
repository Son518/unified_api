from dataclasses import dataclass, field
from project_management.entities.project import Project
from project_management.asana import util

@dataclass
class AsanaProject(Project):
    default_view: str = None
    team: str = None
    public: str = None
    followers: str = None
    is_template: bool = False
    owner: str = None
    # start_date:str
    end_date: str = None

    def __post_init__(self):
        # for api, convert date in app's format to epoch
        if not (self.end_date is None or "-" in self.end_date):
            # for action, convert epoch  to app's format
            format = "%Y-%m-%d"
            self.end_date = util.epoch_to_format(format, self.end_date)
