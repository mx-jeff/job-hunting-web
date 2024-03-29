from src.utils.output import output
from jobhunting.Models.vagasCom import VagasCom
from scrapper_boilerplate.setup import setSelenium


def searchVagasCom(targetJob, vagasUser, vagasPassword, auto_webdriver=False):
    driver = setSelenium(remote_webdriver=auto_webdriver)
    driver.set_window_size(1400, 1000)
    vagas = VagasCom(driver)
    job_site = vagas.appName

    output(vagas, f'{job_site} Iniciando...')
    try:
        output(vagas, f'{job_site} Tentando logar...')
        if not vagas.login(vagasUser, vagasPassword):
            vagas.quitSearch()
            output(vagas, f'{job_site} Login inválido ou campos errados!')
            output(vagas, "[Vagas.com] Saindo... volte sempre :)")
            return 

        output(vagas, f'{job_site} logado com sucesso!')

        output(vagas, f'{job_site} A selecionar vaga...')
        vagas.insertJob(targetJob)
        output(vagas, f'{job_site} Vaga selecionada!')

        output(vagas, f'{job_site} A ajustar opções...')
        vagas.searchOptions()
        output(vagas, f'{job_site} Feito!')

        output(vagas, f'{job_site} Listando Vagas...')
        vagas.selectJobs()
        output(vagas, f'{job_site} Feito!')
        output(vagas, f"{len(vagas.targetLink)} vagas encontradas!")

        success = 0
        fail = 0
        output(vagas, f"{job_site} Se inscrevendo nas vagas...")

        try:
            for index, target in enumerate(vagas.targetLink):
                if target.startswith("https://") or target.startswith("http://"):
                    status = vagas.subscribeJob(target)
                    if status:
                        success += 1

                    else:
                        fail += 1

                    output(vagas, f"{job_site} {index + 1}/{len(vagas.targetLink)} vaga, status: {'Vaga cadastrada!' if status else 'Vaga não cadastrada!'}")

        except Exception:  
            output(vagas, f"{job_site} erro ao se inscrever!")

        finally:
            vagas.quitSearch()

        output(vagas, f'{job_site} Vagas inscritas: {success}')
        output(vagas, f'{job_site} Vagas ja inscritas anteriomente ou requer preenchimento adicional: {fail}')
        output(vagas, f"{job_site} Saindo... volte sempre :)")

    except Exception as error:
        vagas.quitSearch()
        output(vagas, "Algum problema ocorreu e/ou as informações estão erradas!")
        output(vagas, f"{job_site} Saindo... volte sempre :)")

    except KeyboardInterrupt:
        vagas.quitSearch()
        output(vagas, f"{job_site} Saindo... volte sempre :)")
        
