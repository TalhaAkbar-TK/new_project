from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.DepartmentSchema import DepartmentSchema
from project.app.blc.DepartmentBLC import DepartmentBLC

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
