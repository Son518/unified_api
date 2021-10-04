from dataclasses import dataclass


@dataclass
class SalesforceNote:

    note_id: str = None
    body: str = None
    parent: str = None
    title: str = None
    private: str = None
    owner_id: str = None
