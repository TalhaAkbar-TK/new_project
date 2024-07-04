from project.app.db import db

class Job(db.model):
    __tablename__ ="job"
    job_id =db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(100),nullable=True)
    salaryRange = db.column(db.String(50),nullable=True)
    employees = db.relationship("Employee",backref='job')