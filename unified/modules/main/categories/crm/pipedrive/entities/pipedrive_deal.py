# from unified.modules.main.categories.crm.entities.lead import Lead
from crm.entities.deal import Deal
from dataclasses import dataclass


@dataclass
class PipedriveCRMDeal(Deal):

    title: str = None
    expected_close_date: str = None
    status_id: str = None
    creation_date: str = None
    person_id: str = None
    status: str = None
    currency: str = None
    visible_to: str = None
    organization_id: str = None
    label_id: str = None