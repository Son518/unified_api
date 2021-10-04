import json

from recruitment.bamboo_hr.entities.bamboo_employee import BambooEmployee
from recruitment.bamboo_hr.entities.bamboo_time_off import BambooTimeOff
from recruitment.bamboo_hr import util

class BambooHrApi():

    def employee(self, context, params):
        '''Gets an employee'''

        headers = context['headers']
        method = "GET"
        url = "/employees/{id}".format(id=params["employee_id"])
        querystring = {"fields":"employee_id,firstName,lastName,dateOfBirth,address1,address2,city,state,zipcode,country,hireDate,bestEmail"}

        result = json.loads(util.get_bamboo_request(method, url, headers, params=querystring).text)

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
