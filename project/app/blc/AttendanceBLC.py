from project.app.db import db
from project.app.repositories.AttendanceRepository import AttendanceRepository


class AttendanceBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_attendance(args):
        session = AttendanceBLC.get_session()
        result = AttendanceRepository.add_attendance(args, session)
        return result
