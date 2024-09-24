# from project.app.db import db
from project.app.models.Payroll import Payroll


class PayrollRepository:
    @staticmethod
    def geting_single_payroll(args, session):
        result = (
            session.query(Payroll)
            .filter(Payroll.payroll_id == args.get("payroll_id"))
            .first()
        )
        return result

    @staticmethod
    def add_payroll(args, session):
        try:
            payroll = Payroll(**args)
            session.add(payroll)
            session.commit()
            return payroll
        except Exception as e:
            raise e

    def update_payroll_data(args, session, payroll):
        if args.get("salary"):
            payroll.salary = args["salary"]
        if args.get("bonus"):
            payroll.bonus = args["bonus"]
        if args.get("deductions"):
            payroll.deductions = args["deductions"]
        if args.get("paydate"):
            payroll.paydate = args["paydate"]
        if args.get("employee_id"):
            payroll.employee_id = args["employee_id"]
        session.commit()
        return payroll
