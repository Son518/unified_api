from dataclasses import dataclass


@dataclass
class ZohodeskAccount:

    id: str = None
    organization_id: str = None
    name: str = None
    description: str = None
    email: str = None
    website: str = None
    fax: str = None
    phone: str = None
    industry: str = None
    owner_id: str = None
    street: str = None
    city: str = None
    state: str = None
    country: str = None
    zip_code: str = None
    annual_revenue: str = None

    def get_as_data(self, include_none=True):

        data = {
            "accountName": self.name,
            "description": self.description,
            "email": self.email,
            "website": self.website,
            "fax": self.fax,
            "phone": self.phone,
            "industry": self.industry,
            "ownerId": self.owner_id,
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "code": self.zip_code,
            "annualrevenue": self.annual_revenue
        }

        if not include_none:
            data = { key : value for key, value in data.items() if value is not None }

        return data
