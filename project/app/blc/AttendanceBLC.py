from project.app.db import db
from project.app.repositories.AttendanceRepository import AttendanceRepository
from flask import jsonify
from http import HTTPStatus


class AttendanceBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def getting_attendance_by_id(args):
        session = AttendanceBLC.get_session()
        result = AttendanceRepository.getting_attendance_by_id(args, session)
        return result

    @staticmethod
    def add_attendance(args):
        session = AttendanceBLC.get_session()
        result = AttendanceRepository.add_attendance(args, session)
        return result

    @staticmethod
    def updating_attendance_data(args):
        session = AttendanceBLC.get_session()
        attendance = AttendanceRepository.getting_attendance_by_id(args, session)
        if attendance:
            result = AttendanceRepository.updating_attendance_data(
                args, session, attendance
            )
        return result

    @staticmethod
    def deleting_attendance(args):
        session = AttendanceBLC.get_session()
        attendance = AttendanceRepository.getting_attendance_by_id(args, session)
        if not attendance:
            return (
                jsonify({"message": "attendance not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            session.delete(attendance)
            session.commit()
            return (
                jsonify({"message": "attendance successfully deleted"}),
                HTTPStatus.OK,
            )
