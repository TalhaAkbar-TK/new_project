from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.PerformanceSchema import PerformanceSchema
from project.app.blc.PerformanceBLC import PerformanceBLC


bp = Blueprint("performance", __name__)


@bp.route("/performance", methods=["POST"])
@use_args(PerformanceSchema, location="json")
def add_performance(args: dict):
    try:
        result = PerformanceBLC.add_performance(args)

        performance_schema = PerformanceSchema()
        result = performance_schema.dump(result)
        return jsonify(
            {"message": "performance table is updated suceussfullt ", "result": result}
        )
    except Exception as e:
        return jsonify(str(e))
