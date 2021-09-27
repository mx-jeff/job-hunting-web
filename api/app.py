from src.controllers.statusController import selectAll
import socketio
import eventlet
from factory import init_socket
from flask_socketio import emit

from src.controllers.statusController import insert, remove_db
from src.controllers.infojobsController import searchInfojob
from src.controllers.vagasComController import searchVagasCom
from src.Models.database import app


eventlet.monkey_patch()
socketio = init_socket(app)
BASE_URL = "http://localhost:5000"



@app.route('/')
def index():
    return "Welcome"


@socketio.on('close')
def close_connection():
    remove_db()


@socketio.on('open')
def open_connection():
    insert('open')


@socketio.on('job')
def handle_job(conpany, job, infojobs_user, infojobs_password, vagas_user, vagas_password):
    emit('message', 'Iniciando...')
    print('iniciando...')
    print("conpany: ",conpany)


    if conpany == "infojobs":
        emit('message', "iniciando infojobs...")
        searchInfojob(job, infojobs_user, infojobs_password)

    elif conpany == "vagas.com":
        emit('message', 'iniciando vagas.com...')
        searchVagasCom(job, vagas_user, vagas_password)


@socketio.on('init')
def connect_to_websocket(data):
    print(data)


if __name__ == '__main__':
    app.debug = True
    socketio.run(app)
