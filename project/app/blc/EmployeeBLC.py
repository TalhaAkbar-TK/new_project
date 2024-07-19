from project.app.db import db
from project.app.repositories.EmployeeRepository import EmployeeRepository

class EmployeeBLC:
    @staticmethod
    def get_session():
        return db.session
    @staticmethod
    def add_employee(args):
        session= EmployeeBLC.get_session()
        result = EmployeeRepository.add_employee(args,session)
        return result