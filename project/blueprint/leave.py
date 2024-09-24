from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.LeaveSchema import LeaveSchema, update_leave_schema
from project.app.blc.LeaveBLC import LeaveBLC
from marshmallow import fields
from http import HTTPStatus

bp = Blueprint("leave", __name__)


@bp.route("/leave", methods=["POST"])
@use_args(LeaveSchema(), location="json")
def add_leave(args: dict):
    try:
        result = LeaveBLC.add_leave(args)
        leave_schema = LeaveSchema()
        result = leave_schema.dump(result)
        return jsonify({"message": "leave is added succussfully", "result": result})
    except Exception as e:
        return jsonify(str(e))


@bp.route("/get_leave_by_id", methods=["GET"])
@use_args({"leave_id": fields.Integer(required=True)}, location="query")
def get_leave_by_id(args):
    """getting single leave by id"""
    leave = LeaveBLC.geting_single_leave(args)
    if not leave:
        return (
            jsonify({"message": "leave not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    lea = LeaveSchema()
    result = lea.dump(leave)
    return result, HTTPStatus.OK


@bp.route("/update_leave", methods=["PUT"])
@use_args(update_leave_schema, location="json")
def update_employee(args):
    """update leave data"""
    leave = LeaveBLC.updating_leave(args)
    if not leave:
        return jsonify(
            {"message": "employee not found"},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    lea = update_leave_schema()
    result = lea.dump(leave)
    return result, HTTPStatus.OK


@bp.route("/delete_leave", methods=["DELETE"])
@use_args({"leave_id": fields.Integer()}, location="query")
def delete_leave(args):
    """Delete the leave"""
    leave = LeaveBLC.deleting_leave(args)
    return leave
