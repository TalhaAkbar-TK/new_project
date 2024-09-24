from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.AttendanceSchema import (
    AttendanceSchema,
    Update_Attendance_Schema,
)
from project.app.blc.AttendanceBLC import AttendanceBLC
from marshmallow import fields
from http import HTTPStatus

bp = Blueprint("attendance", __name__)


@bp.route("/attendance", methods=["POST"])
@use_args(AttendanceSchema(), location="json")
def add_attendance(args: dict):
    try:
        result = AttendanceBLC.add_attendance(args)
        attendance_schema = AttendanceSchema()
        result = attendance_schema.dump(result)
        return jsonify({"message": "attendance add succussfully", "result": result})
    except Exception as e:
        return jsonify(str(e))


@bp.route("/get_attendance_by_id", methods=["Get"])
@use_args({"attendance_id": fields.Integer(required=True)}, location="query")
def get_attendance_by_id(args):
    """getting attendance by id"""
    attendance = AttendanceBLC.getting_attendance_by_id(args)
    if not attendance:
        return (
            jsonify({"message": "attendance not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    atten = AttendanceSchema()
    result = atten.dump(attendance)
    return result


@bp.route("/update_attendance", methods=["PUT"])
@use_args(Update_Attendance_Schema, location="json")
def update_attendance(args):
    """update attendance data"""
    attendance = AttendanceBLC.updating_attendance_data(args)
    if not attendance:
        return jsonify(
            {"message": "attendance not found"},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    atten = Update_Attendance_Schema()
    result = atten.dump(attendance)
    return result, HTTPStatus.OK


@bp.route("/delete_attendance", methods=["DELETE"])
@use_args({"attendance_id": fields.Integer()}, location="query")
def delete_attendance(args):
    """Delete the attendace"""
    attendance = AttendanceBLC.deleting_attendance(args)
    return attendance
