from dotenv.main import load_dotenv, find_dotenv
from flask import Flask
from flask_socketio import SocketIO
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(find_dotenv())


def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    return app


def init_db(app, database_link):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_link # "postgresql://jkpdcxvy:2r55GlNMqYFfJIkJKg4fsNtHaTgg1f7Y@tuffi.db.elephantsql.com/jkpdcxvy"
    db = SQLAlchemy(app)
    return db


def init_socket(app):
    socketio = SocketIO(app, cors_allowed_origins="*")
    return socketio

print(os.environ.get("POSTGRESQL_LINK"))
app = init_app()
db = init_db(app, database_link=os.environ.get("POSTGRESQL_LINK"))
