from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.JobSchema import JobSchema, update_job_schema
from project.app.blc.JobBLC import JobBLC
from marshmallow import fields
from http import HTTPStatus

bp = Blueprint("job", __name__)


@bp.route("/job", methods=["POST"])
@use_args(JobSchema(), location="json")
def add_job(args):
    try:
        result = JobBLC.add_job(args)
        job_schema = JobSchema()
        result = job_schema.dump(result)
        return jsonify({"message": "job add succussfully", "result": result}), 201
    except Exception as e:
        return jsonify(str(e)), 500


@bp.route("/get_job_by_id", methods=["GET"])
@use_args({"job_id": fields.Integer(required=True)}, location="query")
def get_job_by_id(args):
    """getting job by id"""
    job = JobBLC.getting_job_by_id(args)
    if not job:
        return (jsonify({"message": "job not found"}), HTTPStatus.UNPROCESSABLE_ENTITY)
    jo = JobSchema()
    result = jo.dump(job)
    return result, HTTPStatus.OK


@bp.route("/update_job", methods=["PUT"])
@use_args(update_job_schema, location="json")
def update_job(args):
    """update job data"""
    job = JobBLC.updating_job_data(args)
    if not job:
        return jsonify(
            {"message": "job not found"},
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
    jo = update_job_schema()
    result = jo.dump(job)
    return result, HTTPStatus.OK


@bp.route("/delete_job", methods=["DELETE"])
@use_args({"job_id": fields.Integer()}, location="query")
def delete_job(args):
    """Delete the job"""
    job = JobBLC.deleting_job(args)
    return job
