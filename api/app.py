from flask import Flask
from flask_socketio import SocketIO
from src.controllers.infojobsController import searchInfojob

app = Flask(__name__)
app.config['SECRET_KEY'] = "test"
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return "Welcome"


@socketio.on('job')
def handle_job(job, user, password):
    print(f"{job} {user} {password}")
    searchInfojob(job, user, password)


@socketio.on('init')
def connect_to_websocket(data):
    print(data)


if __name__ == '__main__':
    app.debug = True
    socketio.run(app)
