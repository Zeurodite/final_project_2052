from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes import main
    from app.auth_routes import auth
    from app.article_routes import article_bp

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(article_bp)

    return app
