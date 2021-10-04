from dataclasses import dataclass


@dataclass
class ZohodeskContact:

    contact_id: str = None
    organization_id: str = None
    account_id: str = None
    last_name: str = None
    first_name: str = None
    title: str = None
    description: str = None
    type: str = None
    email: str = None
    secondary_email: str = None
    facebook: str = None
    twitter: str = None
    phone: str = None
    mobile: str = None
    street_address: str = None
    city: str = None
    state: str = None
    country: str = None
    zip_code: str = None

    def get_as_data(self, include_none=True):
        data = {
            "accountId": self.account_id,
            "lastName": self.last_name,
            "firstName": self.first_name,
            "title": self.title,
            "description": self.description,
            "type": self.type,
            "email": self.email,
            "secondaryEmail": self.secondary_email,
            "facebook": self.facebook,
            "twitter": self.twitter,
            "phone": self.phone,
            "mobile": self.mobile,
            "street": self.street_address,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "zip": self.zip_code
        }

        if not include_none:
            data = { key : value for key, value in data.items() if value is not None }

        return data
