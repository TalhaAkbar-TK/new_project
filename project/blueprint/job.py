from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from project.app.schemas.JobSchema import JobSchema
from project.app.blc.JobBLC import JobBLC

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
        print("i am here")
        return jsonify(str(e)), 500
