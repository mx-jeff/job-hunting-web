from flask import Flask
from flask_socketio import SocketIO, emit
from src.controllers.infojobsController import searchInfojob
from src.controllers.vagasComController import searchVagasCom
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "test"
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def index():
    return "Welcome"


@socketio.on('job')
def handle_job(conpany, job, infojobs_user, infojobs_password, vagas_user, vagas_password):
    emit('message', 'Iniciando...')

    print("conpany: ",conpany)
    if conpany == "infojobs":
        emit('message', "iniciando infojobs...")
        searchInfojob(job, infojobs_user, infojobs_password)

    elif conpany == "vagas.com":
        emit('message', 'iniciando vagas.com...')
        searchVagasCom(job, vagas_user, vagas_password)

    # print(job, conpany, infojobs_user, infojobs_password, vagas_user, vagas_password)


@socketio.on('init')
def connect_to_websocket(data):
    print(data)


if __name__ == '__main__':
    app.debug = True
    socketio.run(app)
