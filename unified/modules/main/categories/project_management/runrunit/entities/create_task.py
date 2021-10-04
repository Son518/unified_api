from dataclasses import dataclass


@dataclass
class RunrunitTask():
    title: str = None
    type_id: str = None
    team_id: str = None
    description: str = None
    end_date: str = None
    start_date: str = None
    board_id: str = None
    board_stage_id: str = None
    assignee: str = None
    project_id: str = None
    on_going: bool = False
