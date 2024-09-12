from project.app.db import db
from project.app.models.Attendance import Attendance


class AttendanceRepository:
    @staticmethod
    def add_attendance(args, session):
        try:
            attendance = Attendance(**args)
            db.session.add(attendance)
            session.commit()
            return attendance
        except Exception as e:
            raise e
