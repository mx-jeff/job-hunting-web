from src.utils.status_file import Status_job
from flask import Flask
from flask_socketio import SocketIO, emit
from src.controllers.infojobsController import searchInfojob
from src.controllers.vagasComController import searchVagasCom


BASE_URL = "http://localhost:5000"
app = Flask(__name__)
app.config['SECRET_KEY'] = "test"
socketio = SocketIO(app, cors_allowed_origins="*")
pending = Status_job()


@app.route('/')
def index():
    return "Welcome"


@app.route('/shutdown')
def shutdown():
    import requests
    
    try:
        requests.get(f"{BASE_URL}/close_socket")
    except requests.exceptions.ConnectionError as e:
        print("Shutdown with Connection Error" + e.__str__())
    except BaseException as e:
        print("Shutdown Error " + e.__str__())
    except Exception:
        pass


@app.route('/close_socket')
def close_socket():
    socketio.stop()
    exec('*.py')
    # return "Shutting down..."


@socketio.on('close')
def close_connection():
    # socketio.stop()
    # socketio.run(app)
    pending.set_status('1')


@socketio.on('open')
def open_connection():
    pending.set_status('0')


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

    # print(job, conpany, infojobs_user, infojobs_password, vagas_user, vagas_password)


@socketio.on('init')
def connect_to_websocket(data):
    print(data)


if __name__ == '__main__':
    # app.debug = True
    socketio.run(app)
