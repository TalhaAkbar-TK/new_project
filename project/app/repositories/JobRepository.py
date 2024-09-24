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

    @staticmethod
    def getting_job_by_id(args, session):
        result = session.query(Job).filter(Job.job_id == args.get("job_id")).first()
        return result

    @staticmethod
    def updating_job_data(args, session, job):
        if args.get("title"):
            job.title = args["title"]
        if args.get("description"):
            job.description = args["description"]
        if args.get("salaryRange"):
            job.salaryRange = args["salaryRange"]
        session.commit()
        return job
