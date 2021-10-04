import json
import requests
from requests.api import request
from recruitment.zoho_recruit import util
from recruitment.zoho_recruit.entities.zoho_recruit_record import ZohorecruitRecord

class ZohorecruitApi():

    def record(self,context,params):
        """gets record by record_id"""
        access_token = util.get_access_token(context['headers'])
        endpoint = f"Candidates/{params['record_id']}"
        response = json.loads(util.rest("GET", endpoint, access_token).text)
        record = response.get("data")[0]
        record_obj = ZohorecruitRecord(
                                origin=record.get('Origin'),
                                first_name=record.get('First_Name'),
                                last_name=record.get('Last_Name'),
                                email=record.get('Email'),
                                mobile=record.get('Mobile'),
                                phone=record.get('Phone'),
                                fax=record.get('Fax'),
                                website=record.get('Website'),
                                street=record.get('Street'),
                                city=record.get('City'),
                                state=record.get('State'),
                                pin_code=record.get('Zip_Code'),
                                associated_tags=record.get('Associated_Tags'),
                                candidate_owner=record.get('Candidate_Owner'),
                                candidate_status=record.get('Candidate_Status'),
                                current_employer=record.get('Current_Employer'),
                                current_job_title=record.get('Current_Job_Title'),
                                experience_in_years=record.get('Experience_in_Years'),
                                highest_qualification_held=record.get('Highest_Qualification_Held'),
                                current_salary=record.get('Current_Salary'),
                                rating=record.get('Rating'),
                                skype_id=record.get('Skype_ID'),
                                skill_set=record.get('Skill_Set'),
                                source=record.get('Source'),
                                twitter=record.get('Twitter'),
                                secondary_email=record.get('Secondary_Email'),
                                degree=record.get("Educational_Details")[0].get('Degree') if record.get('Educational_Details') else None,
                                duration_from=record.get("Educational_Details")[0].get('Duration').get("from") if record.get('Educational_Details') else None,
                                duration_to=record.get("Educational_Details")[0].get('Duration').get('to') if record.get('Educational_Details') else None,
                                institute=record.get("Educational_Details")[0].get('Institute_School') if record.get('Educational_Details') else None,
                                department=record.get("Educational_Details")[0].get('Major_Department') if record.get('Educational_Details') else None,
                                company=record.get("Experience_Details")[0].get('Company') if record.get('Experience_Details') else None,
                                occupation=record.get("Experience_Details")[0].get('Occupation_Title') if record.get('Experience_Details') else None,
                                summary=record.get("Experience_Details")[0].get('Summary') if record.get('Experience_Details') else None,
                                work_duration_to=record.get("Experience_Details")[0].get('Work_Duration').get('to') if record.get('Experience_Details') else None,
                                work_duration_from=record.get("Experience_Details")[0].get('Work_Duration').get('from') if record.get('Experience_Details') else None,
                            )
        return record_obj.__dict__