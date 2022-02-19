# Import from external
from flask import render_template, request, session, redirect, url_for, flash
from flask_mail import Mail, Message

# Import from own app
from buddle_core import app, mail
from buddle_core.models.users import Users


@app.route('/', methods=['POST', 'GET'])
def index():
    # Check if user already logged in
    if session.get('user') is not None:
        return redirect(url_for('home'))

    if request.method == 'POST':
        if request.form['email'] != '' and request.form['password'] != '':
            user = Users.query.filter(Users.email == request.form['email'],
                                      Users.password == request.form['password']).first()
            if user is not None:
                session['user'] = user.id
                return redirect(url_for('home'))
            else:
                flash('Could not find account, Check your email & password, or register an account')

    return render_template('index.html', navbar_disabled=True)

