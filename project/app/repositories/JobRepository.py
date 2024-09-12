from project.app.db import db
from project.app.models.Job import Job


class JobRepository:
    @staticmethod
    def add_job(args, session):
        try:
            job = Job(**args)
            db.session.add(job)
            session.commit()
            return job
        except Exception as e:
            raise e
