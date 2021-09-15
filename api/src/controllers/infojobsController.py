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
        output("Algum problema ocorreu e/ou as inforamções estão erradas!")
        output(f"Erro {error}, contate o adminstrador do sistema")
        jobs.quitSearch()
        emit('error', str(error))

    except KeyboardInterrupt:
        output('Saindo, volte sempre!')
        jobs.quitSearch()
        emit('error', str(''))
