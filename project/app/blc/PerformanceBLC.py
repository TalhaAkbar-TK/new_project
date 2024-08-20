from project.app.db import db
from project.app.repositories.PerformanceRepository import PerformanceRepository


class PerformanceBLC:
    @staticmethod
    def get_session():

        return db.session

    @staticmethod
    def add_performance(args):
        session = PerformanceBLC.get_session()
        result = PerformanceRepository.add_performance(args, session)
        return result
