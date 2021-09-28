from factory import init_socket, init_app
from src.Models.Infojobs import Infojobs
from src.utils.output import output
from flask_socketio import emit


def searchInfojob(jobTarget, login, password):
    jobs = Infojobs()

    try:
        jobs.login(login, password)
        jobs.searchList(jobTarget)
        jobs.searchOptions()
        jobs.getJob()
        jobs.quitSearch()

    except Exception as error:
        output(jobs, "[Infojobs] Algum problema ocorreu e/ou as informações estão erradas!")
        jobs.quitSearch()
        emit('error', str(error))

    except KeyboardInterrupt:
        output(jobs, 'Saindo, volte sempre!')
        jobs.quitSearch()
        emit('error', str(''))
