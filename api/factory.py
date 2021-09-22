from flask import Flask
from flask_socketio import SocketIO
import os
from flask_sqlalchemy import SQLAlchemy


ROOT_DIR = ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    return app


def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///status.sqlite"
    db = SQLAlchemy(app)
    return db


def init_socket(app):
    socketio = SocketIO(app, cors_allowed_origins="*")
    return socketio
