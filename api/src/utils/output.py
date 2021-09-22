from flask_socketio import emit
from src.utils.status_file import Status_job
from src.controllers.statusController import selectAll


def output(driver, msg):
    emit('message', msg, broadcast=True, namespace='/')
    # if Status_job().check_status():
    if len(selectAll()) == 0:
        driver.quitSearch()
        emit('error', str(''))

    print(msg)
    