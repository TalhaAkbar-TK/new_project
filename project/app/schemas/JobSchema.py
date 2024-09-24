from marshmallow import Schema, fields, validate

# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
# from project.app.models.Job import Job


class JobSchema(Schema):
    job_id = fields.Integer(dump_only=True)
    title = fields.String(
        validate=validate.Length(
            min=3, max=50, error="title should be in range 3 to 50"
        )
    )
    description = fields.String(
        validate=validate.Length(
            min=10, max=100, error="description should be in range 10 to 100"
        )
    )
    salaryRange = fields.String(
        validate=validate.Length(
            min=4, max=50, error="salryrange should be in range between 4 to 10"
        )
    )


class update_job_schema(JobSchema):
    job_id = fields.Integer(required=True)
