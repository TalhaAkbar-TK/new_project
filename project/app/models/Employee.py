from project.app.db import db


class Employee(db.Model):
    __tablename__ = "employee"
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey("department.department_id"))
    job_id = db.Column(db.Integer, db.ForeignKey("job.job_id"))

    job = db.relationship("Job", back_populates="employees")
    department = db.relationship("Department", back_populates="employees")
    attendances = db.relationship(
        "Attendance", cascade="all,delete", back_populates="employees"
    )
    leaves = db.relationship("Leave", cascade="all,delete", back_populates="employees")
    payrolls = db.relationship(
        "Payroll", cascade="all,delete", back_populates="employees"
    )
    performances = db.relationship(
        "Performance", cascade="all,delete", back_populates="employees"
    )
