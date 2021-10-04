from dataclasses import dataclass


@dataclass
class SlackReminder():

    text: str = None
    remind_when: str = None
    remind_who: str = None
    team_id: str = None
