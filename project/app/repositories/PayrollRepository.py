# from project.app.db import db
from project.app.models.Payroll import Payroll


class PayrollRepository:
    @staticmethod
    def add_payroll(args, session):
        try:
            payroll = Payroll(**args)
            session.add(payroll)
            session.commit()
            return payroll
        except Exception as e:
            raise e
