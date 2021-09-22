from flask_socketio import emit
from src.controllers.statusController import selectAll


def output(driver, msg):
    emit('message', msg, broadcast=True, namespace='/')

    if len(selectAll()) == 0:
        driver.quitSearch()
        emit('error', str(''))

    print(msg)
    