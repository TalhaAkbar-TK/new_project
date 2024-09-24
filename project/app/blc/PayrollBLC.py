from project.app.db import db
from project.app.repositories.PayrollRepository import PayrollRepository
from flask import jsonify
from http import HTTPStatus


class PayrollBLC:
    @staticmethod
    def get_session():
        return db.session

    def geting_single_payroll(args):
        session = PayrollBLC.get_session()
        result = PayrollRepository.geting_single_payroll(args, session)
        return result

    @staticmethod
    def add_payroll(args):
        session = PayrollBLC.get_session()
        result = PayrollRepository.add_payroll(args, session)
        return result

    @staticmethod
    def update_payroll_data(args):
        session = PayrollBLC.get_session()
        payroll = PayrollRepository.geting_single_payroll(args, session)
        if payroll:
            result = PayrollRepository.update_payroll_data(args, session, payroll)
            return result

    @staticmethod
    def deleting_payroll(args):
        session = PayrollBLC.get_session()
        payroll = PayrollRepository.geting_single_payroll(args, session)
        if not payroll:
            return (
                jsonify({"message": "payroll not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            session.delete(payroll)
            session.commit()
            return (jsonify({"message": "payroll deleted successfully"}), HTTPStatus.OK)
