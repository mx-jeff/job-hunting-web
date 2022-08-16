import os
import socketio
import eventlet
from flask_socketio import emit
from factory import init_socket

from src.controllers.statusController import selectAll
from src.controllers.statusController import insert, remove_db
from src.controllers.infojobsController import searchInfojob
from src.controllers.vagasComController import searchVagasCom
from factory import app
from dotenv import load_dotenv


eventlet.monkey_patch()
load_dotenv()
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


@socketio.on('disconnect')
def logout():
    remove_db()


@socketio.on('job')
def handle_job(conpany, job, infojobs_user, infojobs_password, vagas_user, vagas_password):
    emit('message', 'Iniciando...', broadcast=True, namespace='/')
    print('iniciando...')
    print("conpany: ",conpany)


    if conpany == "infojobs":
        emit('message', "iniciando infojobs...", broadcast=True, namespace='/')
        searchInfojob(job, infojobs_user, infojobs_password)

    elif conpany == "vagas.com":
        emit('message', 'iniciando vagas.com...', broadcast=True, namespace='/')
        searchVagasCom(job, vagas_user, vagas_password)


# @socketio.on('disconnect')
# def close_app():
#     remove_db()


@socketio.on('init')
def connect_to_websocket(data):
    print(data)


if __name__ == '__main__':
    # app.debug = True
    socketio.run(app)
