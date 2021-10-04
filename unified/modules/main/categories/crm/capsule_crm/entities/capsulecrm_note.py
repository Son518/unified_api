from dataclasses import dataclass
@dataclass
class CapsulecrmNote:
    entity_type:str = None
    entity_id:str = None
    note:str = None