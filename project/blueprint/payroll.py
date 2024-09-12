from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.PayrollSchema import PayrollSchema
from project.app.blc.PayrollBLC import PayrollBLC

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
