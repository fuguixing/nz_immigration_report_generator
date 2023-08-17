import pytest
from flask import Flask
from models import db, User, Report
from services import UserService, ReportService

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

@pytest.fixture
def client():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_create_user(client):
    user = UserService.create_user('Bachelor', 'Computer Science', 'IELTS 7.0')
    assert user.education == 'Bachelor'
    assert user.qualifications == 'Computer Science'
    assert user.english_levels == 'IELTS 7.0'

def test_update_user_info(client):
    user = UserService.create_user('Bachelor', 'Computer Science', 'IELTS 7.0')
    updated_user = UserService.update_user_info(user, 'Master', 'Software Engineering', 'IELTS 7.5')
    assert updated_user.education == 'Master'
    assert updated_user.qualifications == 'Software Engineering'
    assert updated_user.english_levels == 'IELTS 7.5'

def test_generate_report(client):
    user = UserService.create_user('Bachelor', 'Computer Science', 'IELTS 7.0')
    report = ReportService.generate_report(user)
    assert report.user == user
    assert report.content is not None

def test_save_report(client):
    user = UserService.create_user('Bachelor', 'Computer Science', 'IELTS 7.0')
    report = ReportService.generate_report(user)
    result = ReportService.save_report(report)
    assert result['status'] == 'success'

def test_print_report(client):
    user = UserService.create_user('Bachelor', 'Computer Science', 'IELTS 7.0')
    report = ReportService.generate_report(user)
    result = ReportService.print_report(report)
    assert result['status'] == 'success'
