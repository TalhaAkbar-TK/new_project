from flask import Blueprint,jsonify
from webargs.flaskparser import use_args
from project.app.schemas.AttendanceSchema import AttendanceSchema
from project.app.blc.AttendanceBLC import AttendanceBLC

bp = Blueprint('attendance',__name__)
@bp.route('/attendance',methods=['POST'])
@use_args(AttendanceSchema(),location='json')

def add_attendance(args:dict):
    try:
        result = AttendanceBLC.add_attendance(args)
        attendance_schema = AttendanceSchema()
        result = attendance_schema.dump(result)
        return jsonify({"message":"employee add succussfully","result":result})
    except Exception as e :
        return jsonify(str(e))