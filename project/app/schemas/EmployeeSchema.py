from marshmallow import Schema,fields,validate,validates

class EmployeeSchema(Schema):
    employee_id =fields.Integer(dump_only=True)
    name = fields.String(validate=validate.Length(min=3,max=50,error="name should be in between 3 to 50"))
    phone = fields.String(validate=validate.Length(min=6,max=20,error="phone number should be between 6 to 20"))
    email = fields.String(validate=validate.Length(min=5,max=30,error="email should be between 5 to 30"))
    address =fields.String(validate=validate.Length(min=5,max=40,error="address should be between 5 to 40"))
    department_id = fields.Integer(required=True)
    job_id = fields.Integer(required=True)