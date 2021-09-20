from flask_socketio import emit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from src.utils import timer, alert

from src.config import setSelenium
from src.credentails import vagasUser, vagasPassword
from src.utils.output import output
import sys


class VagasCom:
    appName = "[Vagas.com]"

    def __init__(self):
        self.driver = setSelenium("https://www.vagas.com.br")
        output(self.driver ,f'{self.appName} Iniciando...')

    def login(self, login, password):
        driver = self.driver
        
        try:
            output(self.driver ,f'{self.appName} Tentando logar...')

            # Click on login page
            driver.find_element_by_xpath('//*[@id="loginCandidatoDesktop"]').click()
            timer()

            # insert credentials and login-in
            login_form = driver.find_element_by_id('new_login_candidatos_form')

            current_page = driver.current_url

            login_form.find_element_by_id("login_candidatos_form_usuario").send_keys(login or vagasUser)
            login_form.find_element_by_id("login_candidatos_form_senha").send_keys(password or vagasPassword)
            # login_form.find_element_by_id("submitLogin").click()
            login_form.submit()

        except Exception as error:
            output(self.driver ,f"{self.appName} Error: {error}")
            self.quitSearch()
            emit('error', str(error))
            sys.exit()

        if driver.current_url == current_page:
            output(self.driver ,f"{self.appName} login inválido! verifique os seus dados e tende novamente")
            self.quitSearch()
            emit('error', str(''))
            sys.exit()

        output(self.driver ,f'{self.appName} Logado com sucesso')
        timer()

    def insertJob(self, job):
        driver = self.driver

        output(self.driver ,f'{self.appName} A selecionar vaga...')
        # Insert a select job type and click it!
        inputJob = driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div[3]/div/section/div[1]/div[1]/input').send_keys(job)
        driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div[3]/div/section/div[1]/div[3]/button').click()
        timer()
        output(self.driver ,f'{self.appName} Vaga selecionada!')

    def searchOptions(self):
        # filter jobs-options
        output(self.driver ,f'{self.appName} A ajustar opções...')
        driver = self.driver
        timer()

        try:
            # get container of location links
            cityContainer = driver.find_element_by_xpath('//*[@id="pesquisaFiltros"]/div[2]/div[1]/ul')
            
            filterSp = cityContainer.find_elements_by_partial_link_text('São Paulo')[0]
            driver.execute_script("arguments[0].click();", filterSp)
        
        except IndexError:
            print(f'{self.appName} Erro aconteceu com a localidade...')
            pass
        
        timer()
        try:
            filterJunior = driver.find_elements_by_partial_link_text('Júnior/Trainee')[0]
            driver.execute_script("arguments[0].click();", filterJunior)

        except IndexError:
            output(self.driver ,f"{self.appName} Não há vagas para junior :(")
            pass

        output(self.driver ,f'{self.appName} Feito!')

    def selectJobs(self):
        output(self.driver ,f'{self.appName} Listando Vagas...')
        driver = self.driver

        container = driver.find_element_by_id('pesquisaResultado')
        #return container.get_attribute('outerHTML')

        links = container.find_elements_by_tag_name('a')

        # save all links 
        self.targetLink = [link.get_attribute('href') for link in links]
        
        output(self.driver ,f'{self.appName} Feito!')
        return self.targetLink

    @staticmethod
    def saveFile(html):
        with open('file.html','w') as file:
            file.write(html)

    def subscribeJob(self):
        output(self.driver ,f'{self.appName} Se inscrevendo na vaga...')
        driver = self.driver

        # Job page            
        for link in self.targetLink:
            driver.get(link)
            
            try:
                driver.find_element_by_name('bt-candidatura').click()
                
                try:
                    timer()
                    alert(driver)
                    driver.find_element_by_xpath('//*[@id="LtC"]/td[1]/table/tbody/tr/td[1]/a').click()
                    output(self.driver ,f'{self.appName} Inscrição realizada com sucesso :) ')
                    driver.back()
                    driver.back()

                except:
                    output(self.driver ,f'{self.appName} Inscrição realizada com sucesso :) ')
                    driver.back()
                
            except NoSuchElementException:
                output(self.driver ,f'{self.appName} Inscrição realizada anteriormente ;) ')
                driver.back()

            except Exception as error: 
                output(self.driver ,f'{self.appName} Erro na inscrição :( \nError: {error}')

            output(self.driver ,f'{self.appName} Feito!')

    def quitSearch(self):
        output(self.driver ,f'{self.appName} Saindo... volte sempre :)')
        self.driver.quit()
        emit('error', str('Saindo...'))