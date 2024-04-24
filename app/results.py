from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.auth import login_required
from app.db import get_db


bp = Blueprint('results', __name__)


@bp.route('/student/<id>', methods=('GET', 'POST'))
def display_results(id=None):
    db = get_db()
    results = db.execute(
        'SELECT *'
        'FROM results WHERE id=?;', (id,)
    ).fetchall()
    no_results = "No results"
    print(results)
    print(bool(results))
        
    return render_template('student/results.html', results=results, no_results=no_results)


@bp.route('/results/add', methods=('GET', 'POST'))
@login_required
def add_results():
    if request.method == 'POST':
        score = request.form['score']
        error = None
        
        if not score:
            error = 'Score is required.'

        if error is not None:
            flash(error)
            
        else:
            db = get_db()
            db.execute(
                'INSERT INTO results (score)'
                ' VALUES (?)',
                (score)
            )
            db.commit()
            return redirect(url_for('display_results'))

    return render_template('student/add_results.html')

# , url_prefix='/student'
