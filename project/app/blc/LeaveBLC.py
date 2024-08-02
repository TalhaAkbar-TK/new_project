from project.app.db import db
from project.app.repositories.LeaveRepository import LeaveRepository

class LeaveBLC:
    @staticmethod
    def get_session():
        return db.session
    
    @staticmethod
    def add_leave(args):
        session = LeaveBLC.get_session()
        result = LeaveRepository.add_leave(args,session)
        return result