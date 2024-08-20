from project.app.db import db
from project.app.models.Employee import Employee


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
