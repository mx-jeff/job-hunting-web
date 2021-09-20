from flask_socketio import emit
from src.utils.status_file import Status_job


def output(driver, msg):
    emit('message', msg, broadcast=True, namespace='/')
    if Status_job().check_status():
        driver.quitSearch()
        emit('error', str(''))

    print(msg)
    