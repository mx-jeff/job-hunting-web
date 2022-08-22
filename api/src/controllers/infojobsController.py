from src.utils.output import output
from jobhunting.Models.Infojobs import Infojobs
from scrapper_boilerplate import setSelenium, TelegramBot
from src.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

from jobhunting.utils.errors import send_error_to_telegram


def searchInfojob(jobTarget, user, password, auto_webdriver=False):
    """
    Infojobs automatic subscription job

    :jobTarget: target job to subsscribe
    :login: infojobs user to login
    :password: password to login
    """

    driver = setSelenium(remote_webdriver=auto_webdriver)
    driver.set_window_size(1900, 1400)
    jobs = Infojobs(driver, TELEGRAM_BOT_TOKEN, [TELEGRAM_CHAT_ID])
    site_job = jobs.appName
    job_type = jobTarget
    telegram = TelegramBot(TELEGRAM_BOT_TOKEN, [TELEGRAM_CHAT_ID])

    try:
        output(jobs, f'{site_job} Iniciando...')
        output(jobs, f'{site_job} Tentando logar...')

        if not jobs.login(user, password):
            output(jobs, f"{site_job} Login inválido ou campos errados!")
            jobs.quitSearch()
            return

        output(jobs, f'{site_job} Selecionando vaga...')
        jobs.searchList(job_type)
        output(jobs, f'{site_job} Feito!, buscando vagas para {jobTarget}')

        output(jobs, f'{site_job} Selecionando vagas disponiveis...')
        jobs.getJob()
        output(jobs, f'{site_job} {len(jobs.jobsLink)} Vagas selecionadas!')

        success = 0
        fail = 0
        output(jobs, f"{site_job} Se inscrevendo nas vagas...")

        try:
            for index, target in enumerate(jobs.jobsLink):
                if target.startswith("https://") or target.startswith("http://"):
                    status = jobs.subscribeJob(target)
                    if status:
                        success += 1

                    else:
                        fail += 1

                    output(jobs, f"{site_job} {index + 1}/{len(jobs.jobsLink)} vaga, status: {'vaga cadastrada' if status else 'vaga não cadastrada'}")
        
        except Exception:
            output(jobs, f"{site_job} Erro ao se cadastrar, saindo...")

        jobs.quitSearch()

        output(jobs, f'{site_job} Vagas inscritas: {success}')
        output(jobs, f'{site_job} Vagas ja inscritas anteriomente ou requer preenchimento adicional: {fail}')
        output(jobs, f"{site_job} Saindo... volte sempre :)")

    except Exception as error:
        send_error_to_telegram(error=error, driver=driver, title=jobs.appName, telegram=telegram)
        jobs.quitSearch()
        output(jobs, "Algum problema ocorreu e/ou as inforamções estão erradas!")
        output(jobs, f"Erro {error}, contate o adminstrador do sistema")
        output(jobs, f"{site_job} Saindo... volte sempre :)")

    except KeyboardInterrupt:
        output(jobs, f"{site_job} Saindo... volte sempre :)")
        jobs.quitSearch()