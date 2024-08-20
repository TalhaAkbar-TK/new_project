from project.app.db import db
from project.app.repositories.JobRepository import JobRepository


class JobBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_job(args):
        session = JobBLC.get_session()
        result = JobRepository.add_job(args, session)
        return result
