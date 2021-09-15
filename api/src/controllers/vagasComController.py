from time import sleep

from src.Models.vagasCom import VagasCom
from src.utils.output import output
from flask_socketio import emit


def searchVagasCom(targetJob, login, password):
    vagas = VagasCom()
    try:
        vagas.login(login, password)
        vagas.insertJob(targetJob)
        vagas.searchOptions()
        vagas.selectJobs()
        vagas.subscribeJob()
        vagas.quitSearch()

    except Exception as error:
        output("Algum problema ocorreu e/ou as informações estão erradas!")
        vagas.quitSearch()
        emit('error', str(error))

    except KeyboardInterrupt:
        output('Saindo, volte sempre!')
        vagas.quitSearch()
        emit('error', str())
        
