# Import from external
from flask import render_template, request, session, redirect, url_for

# Import from own app
from buddle_core import app
from buddle_core.models.users import Users


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    # Get user object
    session.clear()
    return redirect(url_for('index'))
