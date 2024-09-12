from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.LeaveSchema import LeaveSchema
from project.app.blc.LeaveBLC import LeaveBLC

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
