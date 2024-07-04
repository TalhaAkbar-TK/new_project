from project.app.db import db

class Department(db.model):
    __tablename__ = "department"
    department_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    employees = db.Column('Employee',backref='department')