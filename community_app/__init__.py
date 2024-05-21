from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from community_app.routers.questions import questions_bp
from community_app.routers.response import response_bp
from config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(questions_bp)
    app.register_blueprint(response_bp)

    return app
