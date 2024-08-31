import logging

import auth as auth
from flask import g
from flask_basicauth import BasicAuth
import os


def create_basic_authentication(app):
    try:
        app.config['BASIC_AUTH_USERNAME'] = os.environ.get('SECRET_USERNAME') or 'admin'
        app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('SECRET_PASSWORD') or 'password'

        basic_auth = BasicAuth(app)
        return basic_auth
    except Exception as e:
        logging.getLogger().error("An exception occurred while creating basic authentication object", repr(e))