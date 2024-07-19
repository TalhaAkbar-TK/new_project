from project.app.db import db
from project.app.repositories.DepartmentRepository import DepartmentRepository

class DepartmentBLC:
    @staticmethod
    def get_session():
        return db.session
    @staticmethod
    def add_department(args):
        session=DepartmentBLC.get_session()
        result =DepartmentRepository.add_department(args,session)
        return result