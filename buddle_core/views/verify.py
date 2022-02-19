# Import from external
from flask import render_template, request, session, flash, redirect, url_for

# Import from own app
from buddle_core import app
from services import register_user


@app.route('/verify', methods=['POST', 'GET'])
@app.route('/verify/<int:id>', methods=['POST', 'GET'])
def verify(id=None):
    if id is not None:
        flash('You have been verified')
        return redirect(url_for('index'))
    else:
        return render_template('verify.html', navbar_disabled=True)

