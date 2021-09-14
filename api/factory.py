from flask import Flask
from flask_socketio import SocketIO
import os

ROOT_DIR = ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def init_socket():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app, cors_allowed_origins="*")
    return socketio, app