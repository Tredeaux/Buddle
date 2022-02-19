import datetime
from buddle_core import db


class Users(db.Model):
    __tablename__ = 'users'
    __modelname__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    deleted_at = db.Column(db.DateTime())
    creation_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    # Relationship
    posts = db.relationship("Posts")

    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.password = password
