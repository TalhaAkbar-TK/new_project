from marshmallow import Schema, validate, fields


class LeaveSchema(Schema):
    leave_id = fields.Integer(dump_only=True)
    start_date = fields.Date(required=False)
    end_date = fields.Date(required=False)
    leave_type = fields.String(
        validate=validate.Length(
            min=5, max=50, error="leave type must be between 5 to 50"
        )
    )
    status = fields.String(
        validate=validate.Length(min=5, max=50, error="status need to be ")
    )
    employee_id = fields.Integer(required=True)


class update_leave_schema(LeaveSchema):
    leave_id = fields.Integer(required=True)
