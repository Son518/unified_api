from dataclasses import dataclass, field
from crm.entities.lead import Lead
from datetime import datetime, timezone
from crm.insightly import util

# Insightly application Specific Lead entites

@dataclass
class InsightlyLead(Lead):
    pass
