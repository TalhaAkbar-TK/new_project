from project.app.db import db
from project.app.repositories.EmployeeRepository import EmployeeRepository
from flask import jsonify
from http import HTTPStatus


class EmployeeBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_employee(args):
        session = EmployeeBLC.get_session()
        result = EmployeeRepository.add_employee(args, session)
        return result

    @staticmethod
    def geting_single_employee(args):
        session = EmployeeBLC.get_session()
        res = EmployeeRepository.geting_single_employee(args, session)
        return res

    @staticmethod
    def geting_employee_full_details(args):
        session = EmployeeBLC.get_session()
        res = EmployeeRepository.geting_employee_full_details(args, session)
        return res

    @staticmethod
    def updating_employee(args):
        session = EmployeeBLC.get_session()
        employee = EmployeeRepository.geting_single_employee(args, session)
        if employee:
            res = EmployeeRepository.updating_employee(args, session, employee)
            return res

    @staticmethod
    def deleting_employee(args):

        session = EmployeeBLC.get_session()

        employee = EmployeeRepository.geting_single_employee(args, session)
        if not employee:
            return (
                jsonify({"message": "employee not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            session.delete(employee)
            session.commit()
            return (
                jsonify({"message": "employee successfully deleted"}),
                HTTPStatus.OK,
            )
