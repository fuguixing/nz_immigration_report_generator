"""config.py"""

from typing import Tuple

class Config:
    """Configuration settings for the NZ Immigration Report Generator application."""

    # Database connection settings
    DATABASE: str = 'sqlite:///nz_immigration_report.db'
    SQLALCHEMY_DATABASE_URI: str = DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Application settings
    SECRET_KEY: str = 'secret-key'
    DEBUG: bool = True
    TESTING: bool = False

    # Report generation settings
    REPORT_TEMPLATE: str = 'templates/report.html'
    REPORT_SAVE_PATH: str = 'reports/'
    REPORT_PRINT_FORMAT: Tuple[str, str] = ('PDF', 'A4')

    @staticmethod
    def init_app(app):
        pass
