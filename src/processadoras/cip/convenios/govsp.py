from src.processadoras.zetra.core.zetra_date_var import variaveis_data as data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv()
class CipLocators:
    MENU_PRINCIPAL = (By.XPATH, '//*[@id="container"]/ul/li[2]/a')
    MENU_RELATORIOS = (By.XPATH, '//*[@id="menuRelatorio"]/ul/li/a')
    CAMPO_USUARIO = (By.NAME, "username")
    BOTAO_CONTINUAR = (By.XPATH, '//*[@id="no-back"]/div/div[1]/form/div[2]/div[2]/button')
    CAMPO_SENHA = (By.NAME, "senha")
    CAMPO_CAPTCHA = (By.ID, "captcha")
    BOTAO_LOGIN = (By.XPATH, '//*[@id="btnOK"]')
    DATA_INICIO = (By.XPATH, '//*[@id="periodoIni"]')
    DATA_FIM = (By.XPATH, '//*[@id="periodoFim"]')
    CHECKBOX_DEFERIDA = (By.XPATH, '//*[@id="SAD_CODIGO7"]')
    BOTAO_GERAR = (By.XPATH, '//*[@id="btnEnvia"]')
    OPCOES_DOWNLOAD = (By.XPATH, '//*[@id="userMenu"]')
    BOTAO_DOWNLOAD = (By.XPATH, '//*[@id="dataTables"]/tbody/tr[1]/td[4]/div/div/div/a[1]')
    SELEC_OPCOES =(By.XPATH, '//*[@id="formato"]')
    OPCAO_CSV = (By.XPATH, '//*[@id="formato"]/option[4]')
    SENHA_AUTORIZER = (By.XPATH, '//*[@id="senha2aAutorizacao"]')

class ConvenioGovSP:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("CIP_GOVSP_URL")
        self.user = os.getenv("CIP_USER")
        self.password = os.getenv("CIP_PASS")

        if not all([self.url, self.user, self.password, self.second_password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(CipLocators.CAMPO_USUARIO)
            ).send_keys(self.user)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CipLocators.BOTAO_CONTINUAR)
            ).click()
        except Exception as e:
            print (f"Erro ao acessar a página de login: {e}")