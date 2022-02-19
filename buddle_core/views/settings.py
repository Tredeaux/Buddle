# Import from external
from flask import render_template, request, session

# Import from own app
from buddle_core import app
from buddle_core.models.users import Users


@app.route('/settings', methods=['POST', 'GET'])
def settings():
    # Get user object
    user = Users.query.filter(Users.id == session.get('user')).first()

    return render_template('settings.html', user=user)

