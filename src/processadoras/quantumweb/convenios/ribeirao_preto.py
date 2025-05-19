from src.processadoras.quantumweb.core.quantumweb_date_var import variaveis_data as data
from src.processadoras.quantumweb.core.qw_paths import Diretorios_Imagem as DI
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pyautogui as pg
import time
import os

load_dotenv()

class RibeiraoLocators:
    CAMPO_LOGIN = (By.NAME, "txtUsuario")
    CAMPO_SENHA = (By.NAME, "txtSenha")
    CAMPO_CAPTCHA = (By.NAME, "txtPalavraChave")
    BOTAO_LOGIN = (By.NAME, "btnLogin")
    BOTAO_NOTIFICACAO = (By.XPATH, '//*[@id="mdlBtnOpe0"]')
    ABA_RELATORIO = (By.XPATH, '//*[@id="menu93"]')
    OPCAO_CONTRATO = (By.XPATH, '//*[@id="ul-menu"]/li[1]/ul/li/a')
    CAMPO_DATA_INI = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_txtFiltroDataInicial"]')
    CAMPO_DATA_FIM = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_txtFiltroDataFinal"]')
    BOTAO_TIPO_ARQUIVO = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_cmbExportar"]')
    OPCAO_CSV = (By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_cmbExportar"]/option[6]')

class ConvenioRibeirao:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("QUANTUMWEB_RIBEIRAO_PRETO_URL")
        self.user = os.getenv("QUANTUMWEB_USER")
        self.password = os.getenv("QUANTUMWEB_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(RibeiraoLocators.CAMPO_LOGIN)).send_keys(self.user)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(RibeiraoLocators.CAMPO_SENHA)).send_keys(self.password)
            QWCaptchaResolver = input("Digite o captcha: ")
            self.driver.find_element(*RibeiraoLocators.CAMPO_CAPTCHA).send_keys(QWCaptchaResolver)
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(RibeiraoLocators.BOTAO_LOGIN)).click()
            try:
                WebDriverWait(self.driver, 2.5).until(
                    EC.presence_of_element_located(RibeiraoLocators.ABA_RELATORIO))
                return True
                 
            except:
                while True:
                    try:
                        WebDriverWait(self.driver, 1).until(
                            EC.element_to_be_clickable(RibeiraoLocators.BOTAO_NOTIFICACAO)).click()                        
                        WebDriverWait(self.driver, 1).until(
                            EC.presence_of_element_located(RibeiraoLocators.CAMPO_SENHA)).send_keys(self.password)
                        QWCaptchaResolver = input("Digite o captcha: ")
                        self.driver.find_element(*RibeiraoLocators.CAMPO_CAPTCHA).clear()
                        self.driver.find_element(*RibeiraoLocators.CAMPO_CAPTCHA).send_keys(QWCaptchaResolver)
                        WebDriverWait(self.driver, 3).until(
                            EC.element_to_be_clickable(RibeiraoLocators.BOTAO_LOGIN)).click()
                        WebDriverWait(self.driver, 1.5).until(
                            EC.presence_of_element_located(RibeiraoLocators.ABA_RELATORIO))
                        return True
                    except:
                        print("Captcha incorreto digitado, favor tentar novamente")
                        time.sleep(0.5)
        
        except Exception as e:
            print(f"Erro: {e}")
            
    def navega_menu(self):
        try:
            AbaRelatorio = pg.locateOnScreen(
                DI.aba_relatorio,
                confidence=0.9,
                minSearchTime=3
            )
            pg.moveTo(AbaRelatorio)
            WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(RibeiraoLocators.OPCAO_CONTRATO)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(RibeiraoLocators.CAMPO_DATA_INI)).clear()
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(RibeiraoLocators.CAMPO_DATA_INI)).send_keys(data.DATA_INICIAL)
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(RibeiraoLocators.CAMPO_DATA_FIM)).clear()
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(RibeiraoLocators.CAMPO_DATA_FIM)).send_keys(data.DATA_FINAL)
            return True
        except Exception as e:
            print(f"Erro: {e}")
        
    def download_relatorio(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(RibeiraoLocators.BOTAO_TIPO_ARQUIVO)).click()
            WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(RibeiraoLocators.OPCAO_CSV)).click()
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Erro: {e}")
            