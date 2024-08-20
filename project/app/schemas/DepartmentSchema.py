from marshmallow import Schema, fields, validate


class DepartmentSchema(Schema):
    department_id = fields.Integer(dump_only=True)
    name = fields.String(
        validate=validate.Length(min=3, max=50, error="name should be in range 3 to 50")
    )
