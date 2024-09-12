from project.app.db import db
from sqlalchemy import Date


class Performance(db.Model):
    __tablename__ = "performance"
    performance_id = db.Column(db.Integer, primary_key=True)
    review_date = db.Column(Date, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    feedback = db.Column(db.String(50), nullable=True)

    employee_id = db.Column(db.Integer, db.ForeignKey("employee.employee_id"))
    employees = db.relationship("Employee", back_populates="performances")
