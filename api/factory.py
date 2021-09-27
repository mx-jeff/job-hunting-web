from flask import Flask
from flask_socketio import SocketIO
import os
from flask_sqlalchemy import SQLAlchemy


ROOT_DIR = ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://jkpdcxvy:2r55GlNMqYFfJIkJKg4fsNtHaTgg1f7Y@tuffi.db.elephantsql.com/jkpdcxvy" #"sqlite:///status.sqlite"
    db = SQLAlchemy(app)
    return db


def init_socket(app):
    socketio = SocketIO(app, cors_allowed_origins="*")
    return socketio
