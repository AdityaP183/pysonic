from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = "pysonic_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pysonic.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.artist import artist_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(artist_bp)

    with app.app_context():
        db.create_all()

    return app
