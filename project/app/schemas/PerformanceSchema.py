from marshmallow import Schema, validate, fields


class PerformanceSchema(Schema):
    performance_id = fields.Integer(dump_only=True)
    review_date = fields.Date(requried=True)
    score = fields.Integer(requried=True)
    feedback = fields.String(
        validate=validate.Length(
            min=3, max=100, error="length of feedback should be between 3 to 100"
        )
    )
    employee_id = fields.Integer(required=True)


class update_performance_schema(PerformanceSchema):
    performance_id = fields.Integer(required=True)
