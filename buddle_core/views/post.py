# Import from external
import datetime

from flask import render_template, request, session, flash, redirect, url_for
import os
# Import from own app
from buddle_core import app, db
from buddle_core.models.users import Users
from buddle_core.models.posts import Posts


@app.route('/post', methods=['POST', 'GET'])
def post():
    # Get user object
    user = Users.query.filter(Users.id == session.get('user')).first()
    if user is None:
        flash('Please log in to perform such action')
        return redirect(url_for('logout'))

    if request.method == 'POST':
        if request.form['title'] != '' and request.form['description'] != '' and request.files['file'] != '':
            uploads_dir = os.path.join('buddle_core/static', 'uploads', f'user_{user.id}')

            os.makedirs(uploads_dir, exist_ok=True)

            file = request.files['file']
            filename = f'{datetime.datetime.utcnow()}_{file.filename}'
            file.save(os.path.join(uploads_dir, filename))
            image_location = os.path.join('uploads', f'user_{user.id}', filename)

            post = Posts(title=request.form['title'],
                         description=request.form['description'],
                         creator_id=user.id,
                         image=image_location)

            db.session.add(post)
            db.session.commit()
            flash('Post have been made succesfully')

    return render_template('post.html', user=user)

