from project.app.db import db
from project.app.models.Leave import Leave


class LeaveRepository:
    @staticmethod
    def geting_single_leave(args, session):
        result = (
            session.query(Leave).filter(Leave.leave_id == args.get("leave_id")).first()
        )
        return result

    @staticmethod
    def add_leave(args, session):
        try:
            leave = Leave(**args)
            db.session.add(leave)
            session.commit()
            return leave
        except Exception as e:
            raise e

    def updating_leave(args, session, leave):
        if args.get("start_date"):
            leave.start_date = args["start_date"]
        if args.get("end_date"):
            leave.end_date = args["end_date"]
        if args.get("leave_type"):
            leave.leave_type = args["leave_type"]
        if args.get("status"):
            leave.status = args["status"]
        if args.get("employee_id"):
            leave.employee_id = args["employee_id"]
        session.commit()
        return leave
