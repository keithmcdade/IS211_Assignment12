from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.auth import login_required
from app.db import get_db


bp = Blueprint('results', __name__)


@bp.route('/student/<id>', methods=('GET', 'POST'))
@login_required
def display_results(id=None):
    db = get_db()
    sql = '''SELECT results.id, quizzes.subject, quizzes.date, results.score, students.first_name, students.last_name
                FROM results
                INNER JOIN quizzes ON results.quiz_id=quizzes.id
                INNER JOIN students ON results.student_id=students.id
                WHERE student_id=?;'''
    args = (id) 
    results = db.execute(sql, args).fetchall()
    student_sql = 'SELECT * FROM students WHERE id=?;'
    args = id
    students = db.execute(student_sql, args).fetchall()
    student = {}
    for row in students:
        student.update({'fname':row['first_name'], 'lname':row['last_name']})
    print(student)
    return render_template('student/results.html', results=results, student=student)


@bp.route('/results/add', methods=('GET', 'POST'))
@login_required
def add_results():
    db = get_db()
    students = db.execute(
        'SELECT *'
        'FROM students;'
    ).fetchall()
    quizzes = db.execute(
        'SELECT *'
        'FROM quizzes;'
    ).fetchall() 
    
    if request.method == 'POST':
        
        student_id = int(request.form['students'])
        quiz_id = int(request.form['quizzes'])
        score = int(request.form['score'])
        error = None
        
        if not score:
            error = 'Score is required.'
            
        if error is not None:
            flash(error)
            
        else:
            db = get_db()
            db.execute(
                'INSERT INTO results (score, student_id, quiz_id)'
                ' VALUES (?, ?, ?)',
                (score, student_id, quiz_id)
            )
            db.commit()
            return redirect(url_for('results.display_results', id=student_id))

    return render_template('student/add_results.html', students=students, quizzes=quizzes)

# , url_prefix='/student'
