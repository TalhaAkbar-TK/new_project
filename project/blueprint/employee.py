from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.EmployeeSchema import EmployeeSchema
from project.app.blc.EmployeeBLC import EmployeeBLC

bp = Blueprint("employee", __name__)


@bp.route("/employee", methods=["POST"])
@use_args(EmployeeSchema(), location="json")
def add_employee(args: dict):

    try:
        result = EmployeeBLC.add_employee(args)
        employee_schema = EmployeeSchema()
        result = employee_schema.dump(result)
        return jsonify({"message": "employee add succussfully", "result": result})
    except Exception as e:
        return jsonify(str(e))
