from dataclasses import dataclass

@dataclass
class TeamworkCalendarevent():

    id: str = None
    title: str = None
    description: str = None
    where: str = None
    start_date: str = None
    end_date: str = None
    allDay: str = None
    type: str = None
    privacy: str = None
    reminders: str = None
    attendees: str = None
    created_date: str = None
    updated_date: str = None
