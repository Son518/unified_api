from dataclasses import dataclass


@dataclass
class PipedriveCRMNote():

    note_id: str = None
    content: str = None
    deal_id: str = None
    pin_note_on_specified_deal: str = None
    organization_id: str = None
    pin_note_on_specified_organization: str = None
    person_id: str = None
    pin_note_on_specified_person: str = None
    lead_id: str = None
    pin_note_on_specified_lead: str = None
    