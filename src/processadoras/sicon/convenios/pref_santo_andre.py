from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from src.processadoras.consiglog.core.consiglog_date_var import variaveis_data as data
from dotenv import load_dotenv
import time
import os

load_dotenv()
class SantoAndreLocators:
    CAMPO_USER = (By.XPATH, '//*[@id="txtLogin"]')
    BOTAO_CONTINUAR = (By.XPATH, '//*[@id="btnContinuar"]')
    CAMPO_SENHA = (By.XPATH, '//*[@id="txtSenha"]')
    BOTAO_ACESSO = (By.XPATH, '//*[@id="cmdUISubmit"]')
    SELEC_ORGAO = (By.XPATH, '//*[@id="ucOrgaoModalPopup1_gvOrgao_imgEntrarNome_0"]')
    BOTAO_FECHA_NOTIFICACAO = (By.XPATH, '//*[@id="ExemploModalCentralizado"]/div/div/div[3]/button')
    ABA_RELATORIOS = (By.XPATH, '//*[@id="menu1"]/div/div/div/ul/li[2]/a')
    OPCAO_RELATORIOS_CONC = (By.XPATH, '//*[@id="menu1"]/div/div/div/ul/li[2]/ul/li/a')
    BOTAO_MES = (By.XPATH, '//*[@id="body_ddlMesFechamento_chosen"]/a')
    CAMPO_MES = (By.XPATH, '//*[@id="body_ddlMesFechamento_chosen"]/div/div/input')

    
class ConvenioPrefSantoAndre:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("SICON_SANTO_ANDRE_PREF_URL")
        self.user = os.getenv("SICON_USER")
        self.password = os.getenv("SICON_PASS")

        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SantoAndreLocators.CAMPO_USER)).send_keys(self.user)
            self.driver.find_element(*SantoAndreLocators.BOTAO_CONTINUAR).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SantoAndreLocators.CAMPO_SENHA)).send_keys(self.password)
            self.driver.find_element(*SantoAndreLocators.BOTAO_ENTRAR).click()
                        
            try:
                WebDriverWait(self.driver, 1.5).until(
                    EC.element_to_be_clickable(SantoAndreLocators.BOTAO_LOGOUT_SESSAO_INATIV)).click()
            except:
                print("Sem necessidade de logout de outras sessões")
                
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
