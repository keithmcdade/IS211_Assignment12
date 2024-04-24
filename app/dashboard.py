# some of the following code is copied from flaskr tutorial with some modifications
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.auth import login_required
from app.db import get_db


bp = Blueprint('dashboard', __name__)


@bp.route('/')
def index():
    db = get_db()
    student_sql = 'SELECT * FROM students;'
    students = db.execute(student_sql).fetchall()
    quizzes_sql = 'SELECT "id", "subject", "date", "questions" FROM quizzes;'
    quizzes = db.execute(quizzes_sql).fetchall()
    return render_template('dashboard/index.html', students=students, quizzes=quizzes)


@bp.route('/student/add', methods=('GET', 'POST'))
@login_required
def add_student():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        error = None
        
        if not first_name and last_name:
            error = 'Student name is required.'
        if not first_name:
            error = 'First name is required.'
        if not last_name:
            error = 'Last name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO students (first_name, last_name)'
                ' VALUES (?, ?)',
                (first_name, last_name)
            )
            db.commit()
            return redirect(url_for('dashboard.index'))

    return render_template('dashboard/student/add.html')


@bp.route('/quiz/add', methods=('GET', 'POST'))
@login_required
def add_quiz():
    if request.method == 'POST':
        subject = request.form['subject']
        date = request.form['date']
        questions = request.form['questions']
        error = None
        
        if not subject:
            error = 'Subject is required.'
        if not date:
            error = 'Date is required.'
        if not questions:
            error = 'Number of questions is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO quizzes (subject, date, questions)'
                ' VALUES (?, ?, ?)',
                (subject, date, questions)
            )
            db.commit()
            return redirect(url_for('dashboard.index'))

    return render_template('dashboard/quiz/add.html')
