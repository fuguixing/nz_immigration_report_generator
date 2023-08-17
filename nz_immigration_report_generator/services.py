from typing import Dict
from .models import User, Report, db

class UserService:
    """Service for handling user-related operations."""

    @staticmethod
    def create_user(education: str, qualifications: str, english_levels: str) -> User:
        user = User(education, qualifications, english_levels)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user_info(user: User, education: str, qualifications: str, english_levels: str) -> User:
        user.update_info(education, qualifications, english_levels)
        return user

class ReportService:
    """Service for handling report-related operations."""

    @staticmethod
    def generate_report(user: User) -> Report:
        report = Report(user)
        report.generate()
        db.session.add(report)
        db.session.commit()
        return report

    @staticmethod
    def save_report(report: Report) -> Dict[str, str]:
        report.save()
        return {'status': 'success', 'message': 'Report saved successfully'}

    @staticmethod
    def print_report(report: Report) -> Dict[str, str]:
        report.print()
        return {'status': 'success', 'message': 'Report printed successfully'}
