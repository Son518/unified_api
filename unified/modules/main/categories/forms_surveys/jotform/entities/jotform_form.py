from dataclasses import dataclass
from forms_surveys.entities.form import Form


@dataclass
class JotFormForm(Form):

    label: str = None
    slug: str = None
    type: str = None
    order: str = None
    questions_type: str = None
    form_height: str = None
    emails_type: str = None
    from_email: str = None
    to: str = None
    subject: str = None
    is_html: str = None
    body: str = None
    form_id: str = None
    form_title: str = None