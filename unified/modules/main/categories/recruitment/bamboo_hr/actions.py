import json

from unified.core.actions import Actions
from recruitment.bamboo_hr.entities.bamboo_employee import BambooEmployee
from recruitment.bamboo_hr.entities.bamboo_time_off import BambooTimeOff
from recruitment.bamboo_hr.entities.bamboo_time_off_summary import BambooTimeOffSummary
from recruitment.bamboo_hr.entities.bamboo_file import BambooFile
from recruitment.bamboo_hr import util

class BambooHrActions(Actions):

    def create_employee(self, context, task_entity):
        '''Creates a new employee'''

        task_schema = BambooEmployee(**task_entity)
        headers = context['headers']
        method = "POST"
        url = "/employees/"

        task_data = util.create_employee_payload(task_schema)
        result = util.get_bamboo_request(method, url, headers, body=task_data)

        querystring = {"fields":"employee_id,firstName,lastName,dateOfBirth,address1,address2,city,state,zipcode,country,hireDate,bestEmail"}
        employee_id = result.headers["Location"].split("/")[-1]
        url2 = url + employee_id
        result = json.loads(util.get_bamboo_request("GET", url2, headers, params=querystring).text)

        bamboo_employee = BambooEmployee(
            employee_id=result["id"],
            first_name=result["firstName"],
            last_name=result["lastName"],
            date_of_birth=result["dateOfBirth"],
            address1=result["address1"],
            address2=result["address2"],
            city=result["city"],
            state=result["state"],
            zip_code=result["zipcode"],
            country=result["country"],
            hire_date=result["hireDate"],
            work_email=result["bestEmail"]
        )

        return bamboo_employee.__dict__

    def get_summary_of_whos_out(self, context, task_entity):
        '''Gets a summary of which people are out'''

        headers = context['headers']
        method = "GET"
        url = "/time_off/whos_out/"

        task_data = {
            "startDate": task_entity["start_date"],
            "endDate": task_entity["end_date"]
        }
        summary_list = []
        result = json.loads(util.get_bamboo_request(method, url, headers, params=task_data).text)
        for summary in result:
            bamboo_summary = BambooTimeOffSummary(
                summary_id=summary["id"],
                employee_id=summary["employeeId"],
                employee_name=summary["name"],
                start_date=summary["start"],
                type=summary["type"],
                end_date=summary["end"]
            )
            summary_list.append(bamboo_summary.__dict__)
        return json.dumps(summary_list)

    def respond_to_timeoff_request(self, context, task_entity):
        '''Responds to a time off request'''

        task_schema = BambooTimeOff(**task_entity)
        headers = context["headers"]
        method = "PUT"
        url = "/time_off/requests/{id}/status/".format(id=task_schema.request_id)
        task_data = {
            "status": task_schema.status,
            "note": task_schema.note
        }
        result = util.get_bamboo_request(method, url, headers, body=task_data)
        if result.status_code == 200:
            response = {"completed": 200}
        else: response = {"failed": 403}
        return response

    def update_employee(self, context, task_entity):
        '''Updates an employee'''

        task_schema = BambooEmployee(**task_entity)
        headers = context['headers']
        method = "POST"
        url = "/employees/{id}".format(id=task_schema.employee_id)

        task_data = util.create_employee_payload(task_schema)
        result = util.get_bamboo_request(method, url, headers, body=task_data)

        querystring = {"fields":"employee_id,firstName,lastName,dateOfBirth,address1,address2,city,state,zipcode,country,hireDate,bestEmail"}
        result = json.loads(util.get_bamboo_request("GET", url, headers, params=querystring).text)

        bamboo_employee = BambooEmployee(
            employee_id=result["id"],
            first_name=result["firstName"],
            last_name=result["lastName"],
            date_of_birth=result["dateOfBirth"],
            address1=result["address1"],
            address2=result["address2"],
            city=result["city"],
            state=result["state"],
            zip_code=result["zipcode"],
            country=result["country"],
            hire_date=result["hireDate"],
            work_email=result["bestEmail"]
        )

        return bamboo_employee.__dict__

    def upload_employee_file(self, context, task_entity):
        '''Creates a new file for an employee'''

        task_schema = BambooFile(**task_entity)
        headers = context['headers']
        method = "POST"
        url = "/employees/{id}/files/".format(id=task_schema.employee_id)
        task_data = {
            "category": task_schema.category_id,
            "fileName": task_schema.file_name,
            "share": task_schema.share_this_file_with_employee
        }
        files = {"file": (task_schema.file_name, task_schema.file_content)}

        result = util.get_bamboo_request(method, url, headers, body=task_data, files=files)
        file_id = result.headers["Location"].split("/")[-1]
        url2 = url + file_id
        result = util.get_bamboo_request("GET", url2, headers)
        file_content = {"file_content": result.text}
        return file_content
