from dataclasses import dataclass


@dataclass
class Campaign:
    
    campaign: str = None
    list_id: str = None
    segement_id_type: str = None
    subject: str = None
    from_name: str = None
    from_address: str = None
    reply_to: str = None
    html_content: str = None
    template_id: str = None
    html_url: str = None
    ab_testing: str = None
    type: str = None
    campaign_id: str = None
