from marshmallow import Schema, fields, validate
from project.app.schemas.AttendanceSchema import AttendanceSchema
from project.app.schemas.PerformanceSchema import PerformanceSchema
from project.app.schemas.JobSchema import JobSchema
from project.app.schemas.DepartmentSchema import DepartmentSchema
from project.app.schemas.LeaveSchema import LeaveSchema
from project.app.schemas.PayrollSchema import PayrollSchema


class EmployeeSchema(Schema):
    employee_id = fields.Integer(dump_only=True)
    name = fields.String(
        validate=validate.Length(
            min=3, max=50, error="name should be in between 3 to 50"
        )
    )
    phone = fields.String(
        validate=validate.Length(
            min=6, max=20, error="phone number should be between 6 to 20"
        )
    )
    email = fields.String(
        validate=validate.Length(min=5, max=30, error="email should be between 5 to 30")
    )
    address = fields.String(
        validate=validate.Length(
            min=5, max=40, error="address should be between 5 to 40"
        )
    )
    department_id = fields.Integer(required=True)
    job_id = fields.Integer(required=True)


class All_Details_EmployeeSchema(EmployeeSchema):

    attendances = fields.Nested("AttendanceSchema", many=True)
    department = fields.Nested("DepartmentSchema")
    job = fields.Nested("JobSchema")
    leaves = fields.Nested("LeaveSchema", many=True)
    payrolls = fields.Nested("PayrollSchema")
    performances = fields.Nested("PerformanceSchema")


class update_employee_schema(EmployeeSchema):
    employee_id = fields.Integer(required=True)
