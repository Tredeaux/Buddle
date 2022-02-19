import os


class BaseConfig:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_DIR = BASEDIR + "/static"

    # Database
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
    DB_HOST = os.environ.get('DB_HOST', 'postgres')
    DB_DOMAIN = os.environ.get('DB_DOMAIN' 'localhost')
    DB_PORT = str(os.environ.get('DB_PORT', 5432))

    # Mail
    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] = 465
    # app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
    # app.config['MAIL_PASSWORD'] = '*****'
    # app.config['MAIL_USE_TLS'] = False
    # app.config['MAIL_USE_SSL'] = True