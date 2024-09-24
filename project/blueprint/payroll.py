from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.PayrollSchema import PayrollSchema, update_payroll_schema
from project.app.blc.PayrollBLC import PayrollBLC
from marshmallow import fields
from http import HTTPStatus

bp = Blueprint("payroll", __name__)


@bp.route("/payroll", methods=["POST"])
@use_args(PayrollSchema, location="json")
def add_payroll(args: dict):
    try:
        result = PayrollBLC.add_payroll(args)
        payroll_schema = PayrollSchema()
        result = payroll_schema.dump(result)
        return jsonify({"message": "payroll is added succussfully", "result": result})
    except Exception as e:
        return jsonify(str(e))


@bp.route("/get_payroll_by_id", methods=["GET"])
@use_args({"payroll_id": fields.Integer(required=True)}, location="query")
def get_payroll_by_id(args):
    """getting single payroll by id"""
    payroll = PayrollBLC.geting_single_payroll(args)
    if not payroll:
        return (
            jsonify({"message": "payroll not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    pay = PayrollSchema()
    result = pay.dump(payroll)
    return result, HTTPStatus.OK


@bp.route("/update_payroll", methods=["PUT"])
@use_args(update_payroll_schema, location="json")
def update_payroll(args):
    """update payroll data"""
    payroll = PayrollBLC.update_payroll_data(args)
    if not payroll:
        return jsonify(
            {"message": "payroll not found"},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    pay = update_payroll_schema()
    result = pay.dump(payroll)
    return result, HTTPStatus.OK


@bp.route("/delete_payroll", methods=["DELETE"])
@use_args({"payroll_id": fields.Integer()}, location="query")
def delete_payroll(args):
    """delete the payroll"""
    payroll = PayrollBLC.deleting_payroll(args)
    return payroll
