from project.app.db import db
from sqlalchemy import Date, Time


class Attendance(db.Model):
    __tablename__ = "attendance"
    attendance_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(Date, nullable=False)
    check_in_time = db.Column(Time, nullable=True)
    check_out_time = db.Column(Time, nullable=True)
    employee_id = db.Column(
        db.Integer, db.ForeignKey("employee.employee_id"), nullable=False
    )
    employees = db.relationship("Employee", back_populates="attendances")
