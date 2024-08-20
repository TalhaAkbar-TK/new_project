from project.app.db import db
from project.app.repositories.PayrollRepository import PayrollRepository


class PayrollBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_payroll(args):
        session = PayrollBLC.get_session()
        result = PayrollRepository.add_payroll(args, session)
        return result
