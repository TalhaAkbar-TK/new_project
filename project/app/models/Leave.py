from project.app.db import db
from sqlalchemy import Date,Time

class Leave(db.Model):
    __tablename__ = 'leave'
    leave_id = db.Column(db.Integer,primary_key=True)
    # EmployeeID, StartDate, EndDate, LeaveType, Status)
    start_date = db.Column(Date,nullable=False)
    end_date = db.Column(Date,nullable=False)
    leave_type = db.Column(db.String(50),nullable = True)
    status = db.Column(db.String(50),nullable = True)
    employee_id = db.Column(db.Integer,db.ForeignKey('employee.employee_id'),nullable=False)
    employees = db.relationship('Employee',back_populates='leaves')