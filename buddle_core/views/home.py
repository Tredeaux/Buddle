# Import from external
from flask import render_template, request, session

# Import from own app
from buddle_core import app
from buddle_core.models.users import Users
from buddle_core.models.posts import Posts


@app.route('/home', methods=['POST', 'GET'])
def home():
    user = Users.query.filter(Users.id == session.get('user_id')).first()
    posts = Posts.query.order_by(Posts.id.desc()).all()
    return render_template('home.html', user=user, posts=posts)

