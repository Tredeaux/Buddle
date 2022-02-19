from flask_mail import Message

from buddle_core import app, db, mail
from buddle_core.models.users import Users


def register_user(username, email, password):
    user = Users(user_name=username, email=email, password=password)
    try:
        db.session.add(user)
        db.session.commit()

        msg = Message('Buddle', sender='tredeaux.pitout@gmail.com', recipients=[email])
        msg.body = f"Welcome to Buddle! \n Click here to verify your email: http://0.0.0.0:5000/verify/{user.id}"
        mail.send(msg)

        return user
    except Exception as e:
        print(e)
        return False
