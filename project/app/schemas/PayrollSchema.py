from marshmallow import Schema, validate, fields


class PayrollSchema(Schema):
    payroll_id = fields.Integer(dump_only=True)
    salary = fields.String(
        validate=validate.Length(
            min=3, max=30, error="length of salary field must be between 3 to 30"
        )
    )
    bonus = fields.String(
        validate=validate.Length(
            min=2, max=30, error="bonus field length must be between 2 to 30"
        )
    )
    deductions = fields.String(
        validate=validate.Length(
            min=2, max=30, error="deduction field range must be between 2 to 30"
        )
    )
    paydate = fields.Date(
        requried=True, error="date format must be like that 2024-10-01"
    )
    employee_id = fields.Integer(required=True)


class update_payroll_schema(PayrollSchema):
    payroll_id = fields.Integer(required=True)
