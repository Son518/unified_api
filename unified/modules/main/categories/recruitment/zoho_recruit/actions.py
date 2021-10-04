import json
from requests.models import Response
from core.actions import Actions
from recruitment.zoho_recruit import util
from recruitment.zoho_recruit.entities.zoho_recruit_record import ZohorecruitRecord

class ZohorecruitActions(Actions):

    def create_record(self, context, payload):
        """
        creates a new record
        context holds the headers 
        payload holds the request.body
        """
        access_token = util.get_access_token(context["headers"])
        record = ZohorecruitRecord(**payload)
        endpoint = f"{record.module}"
        record_data = self.retrieve_record_body(record)
        response = util.rest("POST",endpoint,access_token,record_data)
        return json.loads(response.text)

    def retrieve_record_body(self, record):
        record_data = {
                        "data": [
                            {
                                "Last_Name": record.last_name,
                                "First_Name": record.first_name,
                                "Layout_id": record.layout_id,
                                "Email": record.email,
                                "Company": record.company,
                                "Candidate_Status": record.candidate_status,
                                "Mobile": record.mobile,
                                "City": record.city,
                                "Phone": record.phone,
                                "Fax": record.fax,
                                "Website": record.website,
                                "Street": record.street,
                                "State": record.state,
                                "Ratings": record.rating,
                                "Experience_in_Years": record.experience_in_years,
                                "Highest_Qualification_Held": record.highest_qualification_held,
                                "Current_Job_Title": record.current_job_title,
                                "Current_Employer": record.current_employer,
                                "Expected Salary": record.expected_salary,
                                "Current_Salary": record.current_salary,
                                "Additional_Info": record.additional_info,
                                "Skype_ID": record.skype_id,
                                "Twitter": record.twitter,
                                "Skill_Set": record.skill_set,
                                "Zip_Code": record.pin_code,
                                "Secondary_Email": record.secondary_email,
                            }
                        ],
                    "trigger":[record.trigger]
                }
        if record.degree and record.institute and record.department:
            record_data["data"][0]["Educational_Details"]= [
                        {
                            "Degree": record.degree,
                            "Duration": {
                                    "from": record.duration_from,
                                    "to": record.duration_to
                                },
                            "Institute_School": record.institute,
                            "Major_Department": record.department
                        }
                    ]
        if record.company and record.occupation and record.summary:
            record_data["data"][0]["Experience_Details"] = [
                        {
                            "Company": record.company,
                            "Work_Duration": {
                                    "from": record.work_duration_from,
                                    "to": record.work_duration_to
                                },
                            "Occupation_Title": record.occupation,
                            "Summary": record.summary,
                        }
                    ]
        return record_data

    def update_record(self, context, payload):
        """
        updates a record
        context holds the headers 
        payload holds the request.body
        """
        access_token = util.get_access_token(context["headers"])
        record = ZohorecruitRecord(**payload)
        endpoint = f"{record.module}/{record.record_id}"
        record_data = self.retrieve_record_body(record)
        response = util.rest("PUT",endpoint,access_token,record_data)
        return json.loads(response.text)

    def update_record_status(self, context, payload):
        """
        updates a record status
        context holds the headers 
        payload holds the request.body
        """
        access_token = util.get_access_token(context["headers"])
        record = ZohorecruitRecord(**payload)
        endpoint = f"{record.module}/status"
        record_data = {
                        "data": [
                            {
                                "ids": [record.record_id],
                                "Candidate_Status": record.status,
                                "comments": record.comments
                            }
                        ],
                        "trigger":[record.trigger]
                    }
        response = util.rest("PUT",endpoint,access_token,record_data)
        return json.loads(response.text)