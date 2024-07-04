from project.app.db import db

class Empolyee(db.Model):
    __tablename__ ="empolyee"
    empolyee_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    phone = db.Column(db.String(11),nullable=True)
    email = db.Column(db.String(50),nullable =True)
    address = db.Column(db.String(100),nullable =True)
    department_id = db.Column(db.integer,db.ForeignKey('department.department_id'),nullable =False)
    job_id = db.Column(db.integer,db.Foreignkey('job.job_id'),nullable = False)
