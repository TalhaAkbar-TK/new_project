from project.app.db import db


class Job(db.Model):
    __tablename__ = "job"
    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    salaryRange = db.Column(db.String(50), nullable=True)
    employees = db.relationship("Employee", back_populates="job")
