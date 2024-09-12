from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.EmployeeSchema import (
    EmployeeSchema,
    All_Details_EmployeeSchema,
    update_employee_schema,
)
from project.app.blc.EmployeeBLC import EmployeeBLC
from marshmallow import fields
from http import HTTPStatus

bp = Blueprint("employee", __name__)


@bp.route("/employee", methods=["POST"])
@use_args(EmployeeSchema, location="json")
def add_employee(args: dict):

    try:
        result = EmployeeBLC.add_employee(args)
        employee_schema = EmployeeSchema()
        result = employee_schema.dump(result)
        return jsonify({"message": "employee add succussfully", "result": result})
    except Exception as e:
        return jsonify(str(e))


@bp.route("/get_employee_by_id", methods=["GET"])
@use_args({"employee_id": fields.Integer(required=True)}, location="query")
def get_employee_by_id(args):
    """getting single employee by id"""
    employee = EmployeeBLC.geting_single_employee(args)
    if not employee:
        return (
            jsonify({"message": "employee not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    emp = EmployeeSchema()
    result = emp.dump(employee)
    return result, HTTPStatus.OK


@bp.route("/get_employee_full_details", methods=["GET"])
@use_args({"employee_id": fields.Integer(required=True)}, location="query")
def get_employee_full_details(args):
    """getting full employee details"""
    employee = EmployeeBLC.geting_employee_full_details(args)
    if not employee:
        return (
            jsonify({"message": "employee not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    emp = All_Details_EmployeeSchema()
    result = emp.dump(employee)
    return result, HTTPStatus.OK


@bp.route("/update_employee", methods=["PUT"])
@use_args(update_employee_schema, location="json")
def update_employee(args):
    """update employee data"""
    employee = EmployeeBLC.updating_employee(args)
    if not employee:
        return jsonify(
            {"message": "employee not found"},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    emp = update_employee_schema()
    result = emp.dump(employee)
    return result, HTTPStatus.OK


@bp.route("/delete_employee", methods=["DELETE"])
@use_args({"employee_id": fields.Integer()}, location="query")
def delete_employee(args):
    """Delete the employee"""
    employee = EmployeeBLC.deleting_employee(args)
    return employee
