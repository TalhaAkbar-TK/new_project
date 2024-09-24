from project.app.db import db
from project.app.repositories.PerformanceRepository import PerformanceRepository
from flask import jsonify
from http import HTTPStatus


class PerformanceBLC:
    @staticmethod
    def get_session():

        return db.session

    @staticmethod
    def getting_performance_by_id(args):
        session = PerformanceBLC.get_session()
        result = PerformanceRepository.getting_performance_by_id(args, session)
        return result

    @staticmethod
    def add_performance(args):
        session = PerformanceBLC.get_session()
        result = PerformanceRepository.add_performance(args, session)
        return result

    @staticmethod
    def updating_performance(args):
        session = PerformanceBLC.get_session()
        performance = PerformanceRepository.getting_performance_by_id(args, session)
        if performance:
            result = PerformanceRepository.updating_performance(
                args, session, performance
            )
            return result

    @staticmethod
    def deleting_performance(args):
        session = PerformanceBLC.get_session()
        performance = PerformanceRepository.getting_performance_by_id(args, session)
        if not performance:
            return (
                jsonify({"message": "performance not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            session.delete(performance)
            session.commit()
            return (
                jsonify({"message": "performance is deleted successfully"}),
                HTTPStatus.OK,
            )
