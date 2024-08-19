from project.app.db import db
from sqlalchemy import Date
class Payroll(db.Model):
    __tablename__ = "payroll"
    payroll_id = db.Column(db.Integer,primary_key =True)
    salary = db.Column(db.String(30),nullable=False)
    bonus = db.Column(db.String(30),nullable=True)
    deductions = db.Column(db.String(30),nullable=True)
    paydate = db.Column(Date,nullable=False)

    employee_id = db.Column(db.Integer,db.ForeignKey('employee.employee_id'))
    employees = db.relationship('Employee',back_populates='payrolls')

