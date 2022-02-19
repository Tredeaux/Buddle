# Import from external
from flask import render_template, request, session, flash, redirect, url_for

# Import from own app
from buddle_core import app
from services import register_user


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if request.form['username'] != '' and request.form['password'] != '' and request.form['email'] != '':
            # User register user service
            response = register_user(request.form['username'], request.form['email'], request.form['password'])
            if response is False:
                flash('Could not register user. please try again')
                return redirect(url_for('index'))
            else:
                session['user'] = response.id
                return redirect(url_for('verify'))
        else:
            flash('Registration information is not valid. please try again')
            return redirect(url_for('index'))
    return render_template('register.html', navbar_disabled=True)

