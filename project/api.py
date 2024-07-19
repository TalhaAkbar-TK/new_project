from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from project.app.db import db
from flask_migrate import Migrate
from project.blueprint.department import bp as department_bp
from project.blueprint.job import bp as job_bp
from project.blueprint.employee import bp as employee_bp
from project.blueprint.attendance import bp as attendance_bp

migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"postgresql+psycopg2://{config.DB_USER}:{config.DB_PWD}@{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}"

    db.init_app(app)
    migrate.init_app(app,db)
    # from project.app.models import Department,Employee,Job
    app.register_blueprint(department_bp)
    app.register_blueprint(job_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(attendance_bp)
    return app


    