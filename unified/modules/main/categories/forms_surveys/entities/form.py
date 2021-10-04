from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Form:
    workspace_id: str = None
    title: str = None

    ## Following fields are really required to create a good form. We followed Zapier.
    # fields: List = None
    # welcome_screens
    # thankyou_screens
    # theme_id
    # settings: Dict
    # cui_settings
    # variables
    # logic