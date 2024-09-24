from project.app.db import db
from project.app.repositories.LeaveRepository import LeaveRepository
from http import HTTPStatus
from flask import jsonify


class LeaveBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def geting_single_leave(args):
        session = LeaveBLC.get_session()
        result = LeaveRepository.geting_single_leave(args, session)
        return result

    @staticmethod
    def add_leave(args):
        session = LeaveBLC.get_session()
        result = LeaveRepository.add_leave(args, session)
        return result

    @staticmethod
    def updating_leave(args):
        session = LeaveBLC.get_session()
        leave = LeaveRepository.geting_single_leave(args, session)
        if leave:
            result = LeaveRepository.updating_leave(args, session, leave)
            return result

    @staticmethod
    def deleting_leave(args):
        session = LeaveBLC.get_session()
        leave = LeaveRepository.geting_single_leave(args, session)
        if not leave:
            return (
                jsonify({"message": "leave not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            session.delete(leave)
            session.commit()
            return (jsonify({"message": "leave successfully deleted"}), HTTPStatus.OK)
