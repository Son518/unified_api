from dataclasses import dataclass, field
from crm.entities.account import Account
from datetime import datetime, timezone
from crm.insightly import util

# Insightly application Specific Account entites

@dataclass
class InsightlyAccount(Account):
    fax: str = None
    billing_street: str = None
    billing_city: str = None
    billing_state: str = None
    billing_postal_code: str = None
    billing_country: str = None
    email_domains: str = None
    tags: str = None
    facebook: str = None
    linkedin: str = None
    twitter: str = None
    organization_id: str = None
    organization_name: str = None
    organization_owner_id: str = None
    mailing_zipcode: str = None
    billing_zipcode: str = None
    billing_city: str = None
    billing_country: str = None
    biiling_postal_code: str = None
    billing_state: str = None
    billing_street: str = None
    shipping_city: str = None
    shipping_country: str = None
    shipping_postal_code: str = None
    shipping_state: str = None
    shipping_street: str = None
    visible_to: str = None
    image: str = None
    opportunity_owner_id: str = None
    visible_team_id: str = None
    date_created: str = None
    date_updated: str = None
    last_activity: str = None
    next_activity: str = None
    created_user_id: str = None
    website: str = None
    customfields: str = None
    links: str = None
    dates: str = None
