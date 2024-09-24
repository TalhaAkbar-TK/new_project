from project.app.db import db
from project.app.models.Attendance import Attendance


class AttendanceRepository:
    @staticmethod
    def getting_attendance_by_id(args, session):
        result = (
            session.query(Attendance)
            .filter(Attendance.attendance_id == args.get("attendance_id"))
            .first()
        )
        return result

    @staticmethod
    def add_attendance(args, session):
        try:
            attendance = Attendance(**args)
            db.session.add(attendance)
            session.commit()
            return attendance
        except Exception as e:
            raise e

    @staticmethod
    def updating_attendance_data(args, session, attendance):
        if args.get("date"):
            attendance.date = args["date"]
        if args.get("check_in_time"):
            attendance.check_in_time = args["check_in_time"]
        if args.get("check_out_time"):
            attendance.check_out_time = args["check_out_time"]
        if args.get("employee_id"):
            attendance.employee_id = args["employee_id"]
        session.commit()
        return attendance
