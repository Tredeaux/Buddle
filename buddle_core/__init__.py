# Importing from external
from flask import Flask, redirect, url_for, flash
from flask_mail import Mail, Message

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from config import BaseConfig
import hashlib
import os

# Configs


# Create the Flask App
app = Flask('buddle_core')
app.config.from_object(BaseConfig)
app.secret_key = 'buddle_secret'

# Database
if os.environ.get('DATABASE_URL'):
    uri = os.environ.get('DATABASE_URL')
else:
    uri = f"postgresql://" \
          f"{app.config.get('DB_USER')}:" \
          f"{app.config.get('DB_PASSWORD')}@" \
          f"{app.config.get('DB_HOST')}:" \
          f"{app.config.get('DB_PORT')}"

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
engine = create_engine(uri)

# Mail
app.config['MAIL_SERVER']='smtp.elasticemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tredeaux.pitout@gmail.com'
app.config['MAIL_PASSWORD'] = 'FD5D5C4E61FC63A178E43D2966B0713186CE'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



# Import all models (Insert all models here)
from buddle_core.models.users import Users
from buddle_core.models.posts import Posts


# Build Database Tables
try:
    db.create_all()
    print(f"Created tables from models")
except Exception as e:
    app.logger.error(f"Could not create models: {e}")

# Add views
from buddle_core.views import index, register, home, settings, logout, post, verify

# 404 handler
@app.errorhandler(404)
def invalid_route(e):
    flash(f'{e}')
    return redirect('/')
