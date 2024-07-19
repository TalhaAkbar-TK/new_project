from project.app.db import db
from project.app.models.Department import Department
class DepartmentRepository:
    @staticmethod
    def add_department(args,session):

        try:
            department = Department(**args)
            db.session.add(department)
            session.commit()
            return department
        except Exception as e:
            raise e