from dataclasses import dataclass

@dataclass
class Message:

    message_name: str = None
    message_subject: str = None
    message_type: str = None
    spam_score: str = None