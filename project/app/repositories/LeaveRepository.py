from project.app.db import db
from project.app.models.Leave import Leave


class LeaveRepository:
    @staticmethod
    def add_leave(args, session):
        try:
            leave = Leave(**args)
            db.session.add(leave)
            session.commit()
            return leave
        except Exception as e:
            raise e
