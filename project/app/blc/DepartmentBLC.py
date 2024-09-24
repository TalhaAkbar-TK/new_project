from project.app.db import db
from project.app.repositories.DepartmentRepository import DepartmentRepository
from flask import jsonify
from http import HTTPStatus


class DepartmentBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_department(args):
        session = DepartmentBLC.get_session()
        result = DepartmentRepository.add_department(args, session)
        return result

    @staticmethod
    def getting_department_by_id(args):
        session = DepartmentBLC.get_session()
        result = DepartmentRepository.getting_department_by_id(args, session)
        return result

    @staticmethod
    def updating_department(args):
        session = DepartmentBLC.get_session()
        department = DepartmentRepository.getting_department_by_id(args, session)
        if department:
            result = DepartmentRepository.updating_department(args, session, department)
            return result

    @staticmethod
    def deleting_department(args):
        session = DepartmentBLC.get_session()
        department = DepartmentRepository.getting_department_by_id(args, session)
        if not department:
            return (
                jsonify({"message": "department not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            session.delete(department)
            session.commit()
            return (
                jsonify({"message": "department successfully deleted"}),
                HTTPStatus.OK,
            )
