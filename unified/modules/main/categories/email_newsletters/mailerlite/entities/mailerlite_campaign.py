from email_newsletters.entities.campaign import Campaign
from dataclasses import dataclass


@dataclass
class MalierliteCampaign(Campaign):

    groups_ids: list = None