from marshmallow import Schema, fields


class AttendanceSchema(Schema):
    attendance_id = fields.Integer(dump_only=True)
    date = fields.Date(requried=True)
    check_in_time = fields.Time(required=False, allow_none=True)
    check_out_time = fields.Time(required=False, allow_none=True)
    employee_id = fields.Integer(required=True)


class Update_Attendance_Schema(AttendanceSchema):
    attendance_id = fields.Integer(required=True)
