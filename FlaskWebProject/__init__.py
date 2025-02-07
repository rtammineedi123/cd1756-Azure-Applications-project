"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
import os

app = Flask(__name__)
app.config.from_object(Config)

if not os.path.exists('logs'):
  os.mkdir('logs')

path = os.path.join('logs','flaskapp.log')
# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File Handler for logging to a file
file_handler = logging.FileHandler(path)
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter(
    '%(pathname)s:%(lineno)d - %(message)s; %(asctime)s [%(levelname)s]'
)
file_handler.setFormatter(file_formatter)

# Stream Handler for logging to the console (log stream)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_formatter = logging.Formatter('%(message)s - %(asctime)s')
stream_handler.setFormatter(stream_formatter)

# Add both handlers to the root logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Optionally, if you have a specific app logger
app.logger.handlers = logger.handlers
app.logger.setLevel(logger.level)

app.logger.info('Starting WebProject')

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
