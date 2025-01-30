"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

if not os.path.exists('logs'):
  os.mkdir('logs')

path = os.path.join('logs','flaskapp.log')

logging.basicConfig(
    filename = path,
    level=logging.INFO,
    format='%(pathname)s:%(lineno)d - %(message)s; %(asctime)s [%(levelname)s]'
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler_format = logging.Formatter('%(message)s - %(asctime)s')
handler.setFormatter(handler_format)

app.logger.addHandler(handler)
app.logger.info('Starting WebProject')

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
