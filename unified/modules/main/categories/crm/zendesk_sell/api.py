import json
import basecrm
from crm.zendesk_sell import util
from crm.zendesk_sell.entities.zendesk_sell_contact import ZendesksellContact
from crm.zendesk_sell.entities.zendesk_sell_lead import ZendesksellLead
from crm.zendesk_sell.entities.zendesk_sell_deal import ZendesksellDeal
from crm.zendesk_sell.entities.zendesk_sell_sequence import ZendesksellSequence

class ZendesksellApi():

    def contact(self,context,params):
        ''' return all contacts'''

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        contact = client.contacts.retrieve(id=params["contact_id"])
        
        contact_obj = ZendesksellContact(name=contact.get("name") or None,
                                                email=contact.get("email") or None,
                                                first_name=contact.get("first_name") or None,
                                                last_name=contact.get("last_name") or None,
                                                contact_id=contact.get("id") or None,
                                                customer_status=contact.get("customer_status") or None,
                                                prospect_status=contact.get("prospect_status") or None,
                                                twitter=contact.get("twitter") or None,
                                                facebook=contact.get("facebook") or None,
                                                linkedin=contact.get("linkedin") or None,
                                                website=contact.get("website") or None,
                                                description=contact.get("description") or None,
                                                owner_id=contact.get("owner_id") or None,                  
                                                mailing_street=contact.get("address").get("line1") or None,
                                                mailing_city=contact.get("address").get("city") or None,
                                                mailing_state=contact.get("address").get("state") or None,
                                                mailing_zip=contact.get("address").get("postal_code") or None,
                                                mailing_country=contact.get("address").get("country") or None,
                                                business_phone=contact.get("phone") or None,
                                                created_date=contact.get("created_at") or None,
                                                updated_date=contact.get("updated_at") or None
                                                )
            
        return json.dumps(contact_obj.__dict__)

    def contacts(self,context,params):
        ''' return all contacts'''

        client = basecrm.Client(access_token=context["headers"]["access_token"])
        contacts = client.contacts.list()
        print(len(contacts))
        contact_value = []
        for contact in contacts:
            contact_obj = ZendesksellContact(name=contact.get("name") or None,
                                                email=contact.get("email") or None,
                                                first_name=contact.get("first_name") or None,
                                                last_name=contact.get("last_name") or None,
                                                contact_id=contact.get("id") or None,
                                                customer_status=contact.get("customer_status") or None,
                                                prospect_status=contact.get("prospect_status") or None,
                                                twitter=contact.get("twitter") or None,
                                                facebook=contact.get("facebook") or None,
                                                linkedin=contact.get("linkedin") or None,
                                                website=contact.get("website") or None,
                                                description=contact.get("description") or None,
                                                owner_id=contact.get("owner_id") or None,                  
                                                mailing_street=contact.get("address").get("line1") or None,
                                                mailing_city=contact.get("address").get("city") or None,
                                                mailing_state=contact.get("address").get("state") or None,
                                                mailing_zip=contact.get("address").get("postal_code") or None,
                                                mailing_country=contact.get("address").get("country") or None,
                                                business_phone=contact.get("phone") or None,
                                                created_date=contact.get("created_at") or None,
                                                updated_date=contact.get("updated_at") or None
                                                )
            contact_value.append(contact_obj.__dict__)
        return json.dumps(contacts)

    def contact_by_name(self,context,params):
        
        client = basecrm.Client(access_token=context["headers"]["access_token"])
        contacts = client.contacts.list(name=params["name"])
        print(len(contacts))
        
        contact_value = []
        for contact in contacts:
                contact_obj = ZendesksellContact(name=contact.get("name") or None,
                                                    email=contact.get("email") or None,
                                                    first_name=contact.get("first_name") or None,
                                                    last_name=contact.get("last_name") or None,
                                                    contact_id=contact.get("id") or None,
                                                    customer_status=contact.get("customer_status") or None,
                                                    prospect_status=contact.get("prospect_status") or None,
                                                    twitter=contact.get("twitter") or None,
                                                    facebook=contact.get("facebook") or None,
                                                    linkedin=contact.get("linkedin") or None,
                                                    website=contact.get("website") or None,
                                                    description=contact.get("description") or None,
                                                    owner_id=contact.get("owner_id") or None,                  
                                                    mailing_street=contact.get("address").get("line1") or None,
                                                    mailing_city=contact.get("address").get("city") or None,
                                                    mailing_state=contact.get("address").get("state") or None,
                                                    mailing_zip=contact.get("address").get("postal_code") or None,
                                                    mailing_country=contact.get("address").get("country") or None,
                                                    business_phone=contact.get("phone") or None,
                                                    created_date=contact.get("created_at") or None,
                                                    updated_date=contact.get("updated_at") or None
                                                    )
                contact_value.append(contact_obj.__dict__)
        return json.dumps(contact_value)
    
    def contact_by_email(self,context,params):
        
        client = basecrm.Client(access_token=context["headers"]["access_token"])
        contacts = client.contacts.list(email=params["email"])
        
        contact_value = []
        for contact in contacts:
            contact_obj = ZendesksellContact(name=contact.get("name") or None,
                                                    email=contact.get("email") or None,
                                                    first_name=contact.get("first_name") or None,
                                                    last_name=contact.get("last_name") or None,
                                                    contact_id=contact.get("id") or None,
                                                    customer_status=contact.get("customer_status") or None,
                                                    prospect_status=contact.get("prospect_status") or None,
                                                    twitter=contact.get("twitter") or None,
                                                    facebook=contact.get("facebook") or None,
                                                    linkedin=contact.get("linkedin") or None,
                                                    website=contact.get("website") or None,
                                                    description=contact.get("description") or None,
                                                    owner_id=contact.get("owner_id") or None,                  
                                                    mailing_street=contact.get("address").get("line1") or None,
                                                    mailing_city=contact.get("address").get("city") or None,
                                                    mailing_state=contact.get("address").get("state") or None,
                                                    mailing_zip=contact.get("address").get("postal_code") or None,
                                                    mailing_country=contact.get("address").get("country") or None,
                                                    business_phone=contact.get("phone") or None,
                                                    created_date=contact.get("created_at") or None,
                                                    updated_date=contact.get("updated_at") or None
                                                    )
            contact_value.append(contact_obj.__dict__)
        return json.dumps(contact_value)
        
    def deals(self,context,params):
                
        url = "https://api.getbase.com/v2/deals"
        deals = json.loads(util.rest("GET",url,{},context["headers"]["access_token"]).text)
        deals = deals["items"]
        deal_value = []
        for deal in deals:
            deal = deal["data"]
            print(deal)
            deal_obj = ZendesksellDeal(deal_id=deal.get("id") or None,
                                          created_date=deal.get("created_at") or None,
                                          updated_date=deal.get("updated_at") or None,
                                          name=deal.get("name") or None,
                                          hot=deal.get("hot") or None,
                                          currency=deal.get("currency") or None,
                                          primary_contact=deal.get("contact_id") or None,
                                          tag=deal.get("tag") or None,
                                          source=deal.get("source_id"),
                                          stage_id=deal.get("stage_id") or None,
                                          value=deal.get("value") or None,
                                          owner_id=deal.get("owner_id") or None
                                          )
            deal_value.append(deal_obj.__dict__)
        return json.dumps(deal_value)

    def deal(self,context,params):
                
        url = f"https://api.getbase.com/v2/deals/{params['deal_id']}"
        deal = json.loads(util.rest("GET",url,{},context["headers"]["access_token"]).text)
        deal = deal["data"]
        deal_obj = ZendesksellDeal(deal_id=deal.get("id") or None,
                                          created_date=deal.get("created_at") or None,
                                          updated_date=deal.get("updated_at") or None,
                                          name=deal.get("name") or None,
                                          hot=deal.get("hot") or None,
                                          currency=deal.get("currency") or None,
                                          primary_contact=deal.get("contact_id") or None,
                                          tag=deal.get("tag") or None,
                                          source=deal.get("source_id"),
                                          stage_id=deal.get("stage_id") or None,
                                          value=deal.get("value") or None,
                                          owner_id=deal.get("owner_id") or None
                                          )
        return deal_obj.__dict__

    def deal_by_name(self,context,params):
        
        access_token=context["headers"]["access_token"]
        url=f"https://api.getbase.com/v2/deals?name={params['name']}"
        deal = json.loads(util.rest("GET", url, {}, access_token).text)
        deal = deal["items"][0]["data"]
        deal_obj = ZendesksellDeal(deal_id=deal.get("id") or None,
                                            created_date=deal.get("created_at") or None,
                                            updated_date=deal.get("updated_at") or None,
                                            name=deal.get("name") or None,
                                            hot=deal.get("hot") or None,
                                            currency=deal.get("currency") or None,
                                            primary_contact=deal.get("contact_id") or None,
                                            tag=deal.get("tag"),
                                            source=deal.get("source_id"),
                                            stage_id=deal.get("stage_id") or None,
                                            value=deal.get("value") or None,
                                            owner_id=deal.get("owner_id") or None
                                            )
        
        return deal_obj.__dict__

    def deal_by_stage(self,context,params):
        
        access_token=context["headers"]["access_token"]
        url=f"https://api.getbase.com/v2/deals?stage_id={params['stage_id']}"
        deal = json.loads(util.rest("GET", url, {}, access_token).text)
        deal = deal["items"][0]["data"]
        deal_obj = ZendesksellDeal(deal_id=deal.get("id") or None,
                                            created_date=deal.get("created_at") or None,
                                            updated_date=deal.get("updated_at") or None,
                                            name=deal.get("name") or None,
                                            hot=deal.get("hot") or None,
                                            currency=deal.get("currency") or None,
                                            primary_contact=deal.get("contact_id") or None,
                                            tag=deal.get("tag"),
                                            source=deal.get("source_id"),
                                            stage_id=deal.get("stage_id") or None,
                                            value=deal.get("value") or None,
                                            owner_id=deal.get("owner_id") or None
                                            )
        
        return deal_obj.__dict__

    def deal_by_source(self,context,params):
        
        access_token=context["headers"]["access_token"]
        url=f"https://api.getbase.com/v2/deals?source_id={params['source_id']}"
        deal = json.loads(util.rest("GET", url, {}, access_token).text)
        print(deal)
        deal = deal["items"][0]["data"]
        deal_obj = ZendesksellDeal(deal_id=deal.get("id") or None,
                                            created_date=deal.get("created_at") or None,
                                            updated_date=deal.get("updated_at") or None,
                                            name=deal.get("name") or None,
                                            hot=deal.get("hot") or None,
                                            currency=deal.get("currency") or None,
                                            primary_contact=deal.get("contact_id") or None,
                                            tag=deal.get("tag"),
                                            source=deal.get("source_id"),
                                            stage_id=deal.get("stage_id") or None,
                                            value=deal.get("value") or None,
                                            owner_id=deal.get("owner_id") or None
                                            )
        
        return deal_obj.__dict__

    def leads(self,context,params):
        
        client = basecrm.Client(access_token=context["headers"]["access_token"])
        leads = client.leads.list()
        lead_value = []

        for lead in leads:
            lead_obj = ZendesksellLead(lead_id=lead.get("id") or None,
                                          owner_id=lead.get("owner_id") or None, 
                                          first_name=lead.get("first_name") or None, 
                                          last_name=lead.get("last_name") or None,
                                          created_date=lead.get("created_at") or None,
                                          updated_date=lead.get("updated_at") or None, 
                                          twitter=lead.get("twitter") or None, 
                                          work_number=lead.get("phone") or None, 
                                          mobile_number=lead.get("mobile") or None,
                                          facebook=lead.get("facebook") or None , 
                                          email=lead.get("email") or None,
                                          title=lead.get("title") or None, 
                                          skype=lead.get("skype") or None,
                                          linkedin=lead.get("linkedin") or None, 
                                          description=lead.get("description") or None, 
                                          industry=lead.get("industry") or None, 
                                          fax=lead.get("fax") or None, 
                                          website=lead.get("website")or None, 
                                          street=lead.get("address").get("line1")or None, 
                                          city=lead.get("address").get("city")or None, 
                                          zip=lead.get("address").get("postal_code") or None,
                                          state=lead.get("address").get("state"), 
                                          source=lead.get("source_id"),
                                          country=lead.get("address").get("country")
                                          )
            lead_value.append(lead_obj.__dict__)

        return json.dumps(lead_value)

    def lead(self,context,params):
        
        client = basecrm.Client(access_token=context["headers"]["access_token"])
        lead = client.leads.retrieve(id=params["lead_id"])
        print(lead)
        lead_obj = ZendesksellLead(lead_id=lead.get("id") or None,
                                          owner_id=lead.get("owner_id") or None, 
                                          first_name=lead.get("first_name") or None, 
                                          last_name=lead.get("last_name") or None,
                                          created_date=lead.get("created_at") or None,
                                          updated_date=lead.get("updated_at") or None, 
                                          twitter=lead.get("twitter") or None, 
                                          work_number=lead.get("phone") or None, 
                                          mobile_number=lead.get("mobile") or None,
                                          facebook=lead.get("facebook") or None , 
                                          email=lead.get("email") or None,
                                          title=lead.get("title") or None, 
                                          skype=lead.get("skype") or None,
                                          linkedin=lead.get("linkedin") or None, 
                                          description=lead.get("description") or None, 
                                          industry=lead.get("industry") or None, 
                                          fax=lead.get("fax") or None, 
                                          website=lead.get("website")or None, 
                                          street=lead.get("address").get("line1")or None, 
                                          city=lead.get("address").get("city")or None, 
                                          zip=lead.get("address").get("postal_code") or None,
                                          state=lead.get("address").get("state"), 
                                          source=lead.get("source_id"),
                                          country=lead.get("address").get("country")
                                          )

        return lead_obj.__dict__
    
    def lead_by_source(self,context,params):
        
        client = basecrm.Client(access_token=context["headers"]["access_token"])
        lead = client.leads.list(source_id=params["source_id"])[0]
        lead_obj = ZendesksellLead(lead_id=lead.get("id") or None,
                                          owner_id=lead.get("owner_id") or None, 
                                          first_name=lead.get("first_name") or None, 
                                          last_name=lead.get("last_name") or None,
                                          created_date=lead.get("created_at") or None,
                                          updated_date=lead.get("updated_at") or None, 
                                          twitter=lead.get("twitter") or None, 
                                          work_number=lead.get("phone") or None, 
                                          mobile_number=lead.get("mobile") or None,
                                          facebook=lead.get("facebook") or None , 
                                          email=lead.get("email") or None,
                                          title=lead.get("title") or None, 
                                          skype=lead.get("skype") or None,
                                          linkedin=lead.get("linkedin") or None, 
                                          description=lead.get("description") or None, 
                                          industry=lead.get("industry") or None, 
                                          fax=lead.get("fax") or None, 
                                          website=lead.get("website")or None, 
                                          street=lead.get("address").get("line1")or None, 
                                          city=lead.get("address").get("city")or None, 
                                          zip=lead.get("address").get("postal_code") or None,
                                          state=lead.get("address").get("state"), 
                                          source=lead.get("source_id"),
                                          country=lead.get("address").get("country")
                                          )

        return lead_obj.__dict__
                
    def sequence(self,context,params):
        
        access_token=context["headers"]["access_token"]
        url=f"https://api.getbase.com/v2/sequences/{params['sequence_id']}"
        sequence = json.loads(util.rest("GET", url, {}, access_token).text)
        sequence = sequence["data"]
        
        sequence_obj = ZendesksellSequence(sequence_id=sequence.get("id"),
                                              sequence_name=sequence.get("name"),
                                              created_date=sequence.get("created_at"),  
                                              updated_date=sequence.get("updated_at"),
                                              total_steps=sequence.get("steps_total")
                                              )
                    
        return sequence_obj.__dict__

    def contacts_by_phone_number(self,context,params):
        """
        get contacts by phone number
        """        
        client = basecrm.Client(access_token=context["headers"]["access_token"])
        contacts = client.contacts.list(mobile=params["phone"])
        contact_value = []
        for contact in contacts:
                contact_obj = ZendesksellContact(name=contact.get("name") or None,
                                                    email=contact.get("email") or None,
                                                    mobile_number=contact.get("mobile") or None,
                                                    first_name=contact.get("first_name") or None,
                                                    last_name=contact.get("last_name") or None,
                                                    contact_id=contact.get("id") or None,
                                                    customer_status=contact.get("customer_status") or None,
                                                    prospect_status=contact.get("prospect_status") or None,
                                                    twitter=contact.get("twitter") or None,
                                                    facebook=contact.get("facebook") or None,
                                                    linkedin=contact.get("linkedin") or None,
                                                    website=contact.get("website") or None,
                                                    description=contact.get("description") or None,
                                                    owner_id=contact.get("owner_id") or None,                  
                                                    mailing_street=contact.get("address").get("line1") or None,
                                                    mailing_city=contact.get("address").get("city") or None,
                                                    mailing_state=contact.get("address").get("state") or None,
                                                    mailing_zip=contact.get("address").get("postal_code") or None,
                                                    mailing_country=contact.get("address").get("country") or None,
                                                    business_phone=contact.get("phone") or None,
                                                    created_date=contact.get("created_at") or None,
                                                    updated_date=contact.get("updated_at") or None
                                                    )
                contact_value.append(contact_obj.__dict__)
        return json.dumps(contact_value)

    def profile(self,context,params):
        """
        get call to show authenticated user information
        """
        client = basecrm.Client(access_token=context["headers"]["access_token"])
        account = client.accounts.self()
        profile = {
            'id': account['id'],
            'name':account['name']
        }
        return profile
    
    def verify(self,context,params):
        """
        get call to verify user authenticated information
        """
        client = basecrm.Client(access_token=context["headers"]["access_token"])
        users = client.users.list()
        return json.dumps(users)