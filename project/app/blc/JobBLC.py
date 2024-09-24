from project.app.db import db
from project.app.repositories.JobRepository import JobRepository
from flask import jsonify
from http import HTTPStatus


class JobBLC:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_job(args):
        session = JobBLC.get_session()
        result = JobRepository.add_job(args, session)
        return result

    @staticmethod
    def getting_job_by_id(args):
        session = JobBLC.get_session()
        result = JobRepository.getting_job_by_id(args, session)
        return result

    @staticmethod
    def updating_job_data(args):
        session = JobBLC.get_session()
        job = JobRepository.getting_job_by_id(args, session)
        if job:
            result = JobRepository.updating_job_data(args, session, job)
        return result

    @staticmethod
    def deleting_job(args):
        session = JobBLC.get_session()
        job = JobRepository.getting_job_by_id(args, session)
        if not job:
            return (
                jsonify({"message": "job not found"}),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        else:
            session.delete(job)
            session.commit()
            return (
                jsonify({"message": "job successfully deleted"}),
                HTTPStatus.OK,
            )
