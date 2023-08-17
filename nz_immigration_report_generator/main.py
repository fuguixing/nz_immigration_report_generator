from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, User, Report
from forms import UserInfoForm
from services import UserService, ReportService
from views import app

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
