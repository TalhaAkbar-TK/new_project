from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.DepartmentSchema import (
    DepartmentSchema,
    Update_DepartmentSchema,
)
from project.app.blc.DepartmentBLC import DepartmentBLC
from marshmallow import fields
from http import HTTPStatus

bp = Blueprint("department", __name__)


@bp.route("/department", methods=["POST"])
@use_args(DepartmentSchema(), location="json")
def add_department(args: dict):

    try:
        result = DepartmentBLC.add_department(args)
        department_schema = DepartmentSchema()
        result = department_schema.dump(result)
        return jsonify({"message": "department add succussfully", "result": result})
    except Exception as e:
        return jsonify(str(e))


@bp.route("/get_department_by_id", methods=["GET"])
@use_args({"department_id": fields.Integer(required=True)}, location="query")
def get_department_by_id(args):
    """getting department by id"""
    deparment = DepartmentBLC.getting_department_by_id(args)
    if not deparment:
        return (
            jsonify({"message": "department not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    dep = DepartmentSchema()
    result = dep.dump(deparment)
    return result, HTTPStatus.OK


@bp.route("/update_department", methods=["PUT"])
@use_args(Update_DepartmentSchema, location="json")
def update_department(args):
    """updating department data"""
    department = DepartmentBLC.updating_department(args)
    if not department:
        return jsonify(
            {"message": "department not found"},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    dep = Update_DepartmentSchema()
    result = dep.dump(department)
    return result, HTTPStatus.OK


@bp.route("/delete_department", methods=["DELETE"])
@use_args({"department_id": fields.Integer()}, location="query")
def delete_job(args):
    """Delete the department"""
    department = DepartmentBLC.deleting_department(args)
    return department
