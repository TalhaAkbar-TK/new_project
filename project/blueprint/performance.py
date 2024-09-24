from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.PerformanceSchema import (
    PerformanceSchema,
    update_performance_schema,
)
from project.app.blc.PerformanceBLC import PerformanceBLC
from marshmallow import fields
from http import HTTPStatus

bp = Blueprint("performance", __name__)


@bp.route("/performance", methods=["POST"])
@use_args(PerformanceSchema, location="json")
def add_performance(args: dict):
    try:
        result = PerformanceBLC.add_performance(args)

        performance_schema = PerformanceSchema()
        result = performance_schema.dump(result)
        return jsonify(
            {"message": "performance table is updated suceussfully ", "result": result}
        )
    except Exception as e:
        return jsonify(str(e))


@bp.route("/get_performance_by_id", methods=["GET"])
@use_args({"performance_id": fields.Integer()}, location="query")
def get_performance_by_id(args):
    """getting performance by id"""
    performance = PerformanceBLC.getting_performance_by_id(args)
    if not performance:
        return (
            jsonify({"message": "performance id  not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    per = PerformanceSchema()
    result = per.dump(performance)
    return result, HTTPStatus.OK


@bp.route("/update_performance", methods=["PUT"])
@use_args(update_performance_schema, location="json")
def update_performance(args):
    """updating performance"""
    performance = PerformanceBLC.updating_performance(args)
    if not performance:
        return (
            jsonify({"message": "performance id  not found"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    per = update_performance_schema()
    result = per.dump(performance)
    return result, HTTPStatus.OK


@bp.route("/delete_performance", methods=["DELETE"])
@use_args({"performance_id": fields.Integer()}, location="query")
def delete_performance(args):
    """delete performance"""
    performance = PerformanceBLC.deleting_performance(args)
    return performance
