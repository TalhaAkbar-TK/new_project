from project.app.db import db
from project.app.models.Employee import Employee
from project.app.models.Leave import Leave
from project.app.models.Job import Job
from project.app.models.Payroll import Payroll
from project.app.models.Performance import Performance
from project.app.models.Department import Department
from project.app.models.Attendance import Attendance


class EmployeeRepository:
    @staticmethod
    def add_employee(args, session):
        try:
            employee = Employee(**args)
            db.session.add(employee)
            session.commit()
            return employee
        except Exception as e:
            raise e

    @staticmethod
    def geting_single_employee(args, session):
        result = (
            session.query(Employee)
            .filter(Employee.employee_id == args.get("employee_id"))
            .first()
        )
        return result

    @staticmethod
    def geting_employee_full_details(args, session):
        result = (
            session.query(Employee)
            .filter(Employee.employee_id == args.get("employee_id"))
            .first()
        )
        return result

    @staticmethod
    def updating_employee(args, session, employee):
        # employee.name = args.get("name")
        # employee.phone = args.get("phone")
        # employee.email = args.get("email")
        # employee.address = args.get("address")
        # employee.department_id = args.get("department_id")
        # employee.job_id = args.get("job_id")
        if "name" in args and args["name"] is not None:
            employee.name = args["name"]
        if "phone" in args and args["phone"] is not None:
            employee.phone = args["phone"]
        if "email" in args and args["email"] is not None:
            employee.email = args["email"]
        if "address" in args and args["address"] is not None:
            employee.address = args["address"]
        if "department_id" in args and args["department_id"] is not None:
            employee.department_id = args["department_id"]
        if "job_id" in args and args["job_id"] is not None:
            employee.job_id = args["job_id"]
        session.commit()
        result = (
            session.query(Employee)
            .filter(employee.employee_id == args.get("employee_id"))
            .first()
        )
        return result
