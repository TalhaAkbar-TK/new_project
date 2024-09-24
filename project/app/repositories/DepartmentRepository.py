from project.app.db import db
from project.app.models.Department import Department


class DepartmentRepository:
    @staticmethod
    def add_department(args, session):

        try:
            department = Department(**args)
            db.session.add(department)
            session.commit()
            return department
        except Exception as e:
            raise e

    @staticmethod
    def getting_department_by_id(args, session):
        result = (
            session.query(Department)
            .filter(Department.department_id == args.get("department_id"))
            .first()
        )
        return result

    def updating_department(args, session, department):
        if args.get("name"):
            department.name = args["name"]
        session.commit()
        return department
