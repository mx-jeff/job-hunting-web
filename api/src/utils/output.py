from flask_socketio import emit


def output(msg):
    emit('message', msg, broadcast=True, namespace='/')
    print(msg)
    