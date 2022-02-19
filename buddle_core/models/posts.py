import datetime
from buddle_core import db


class Posts(db.Model):
    __tablename__ = 'posts'
    __modelname__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    deleted_at = db.Column(db.DateTime())
    creation_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    # Foreign Keys
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, description, creator_id, image):
        self.title = title
        self.description = description
        self.creator_id = creator_id
        self.image = image
