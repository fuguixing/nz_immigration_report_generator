from flask import Flask, render_template, request, redirect, url_for, flash
from .forms import UserInfoForm
from .models import db
from .services import UserService, ReportService

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserInfoForm()
    if form.validate_on_submit():
        education = form.education.data
        qualifications = form.qualifications.data
        english_levels = form.english_levels.data
        user = UserService.create_user(education, qualifications, english_levels)
        report = ReportService.generate_report(user)
        flash('Report generated successfully', 'success')
        return redirect(url_for('report', report_id=report.id))
    return render_template('index.html', form=form)

@app.route('/report/<int:report_id>', methods=['GET'])
def report(report_id):
    report = Report.query.get_or_404(report_id)
    return render_template('report.html', report=report)

@app.route('/report/<int:report_id>/save', methods=['POST'])
def save_report(report_id):
    report = Report.query.get_or_404(report_id)
    result = ReportService.save_report(report)
    flash(result['message'], 'success' if result['status'] == 'success' else 'error')
    return redirect(url_for('report', report_id=report.id))

@app.route('/report/<int:report_id>/print', methods=['POST'])
def print_report(report_id):
    report = Report.query.get_or_404(report_id)
    result = ReportService.print_report(report)
    flash(result['message'], 'success' if result['status'] == 'success' else 'error')
    return redirect(url_for('report', report_id=report.id))

@app.route('/user/<int:user_id>/update', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserInfoForm(obj=user)
    if form.validate_on_submit():
        education = form.education.data
        qualifications = form.qualifications.data
        english_levels = form.english_levels.data
        updated_user = UserService.update_user_info(user, education, qualifications, english_levels)
        report = ReportService.generate_report(updated_user)
        flash('User information updated and report regenerated successfully', 'success')
        return redirect(url_for('report', report_id=report.id))
    return render_template('update_user.html', form=form)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
