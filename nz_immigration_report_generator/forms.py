from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UserInfoForm(FlaskForm):
    """Form for users to input their education, qualifications, and English levels."""
    education = StringField('Education', validators=[DataRequired(), Length(max=100)])
    qualifications = StringField('Qualifications', validators=[DataRequired(), Length(max=100)])
    english_levels = StringField('English Levels', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Generate Report')
