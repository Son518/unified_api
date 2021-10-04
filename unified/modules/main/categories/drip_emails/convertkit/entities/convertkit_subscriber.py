from dataclasses import dataclass

@dataclass
class ConvertkitSubscriber:
    tag_id: str = None
    sequence_id: str = None
    subscriber_id: str = None
    form_id: str = None
    email: str = None
    first_name: str = None
