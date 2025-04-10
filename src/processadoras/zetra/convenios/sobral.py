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
class SobralLocators:
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
    
class ConvenioSobral:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("ZETRA_SOBRAL_URL")
        self.user = os.getenv("ZETRA_USER")
        self.password = os.getenv("ZETRA_PASS")

        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")

    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(SobralLocators.CAMPO_USUARIO)
            ).send_keys(self.user)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SobralLocators.BOTAO_CONTINUAR)
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(SobralLocators.CAMPO_SENHA)
            ).send_keys(self.password)
            
            ZetraCaptchaResolver = input("Resolva o captcha e pressione Enter...")
            self.driver.find_element(*SobralLocators.CAMPO_CAPTCHA).send_keys(ZetraCaptchaResolver)
            self.driver.find_element(*SobralLocators.BOTAO_LOGIN).send_keys(Keys.RETURN)
            return True
            
        
        except Exception as e:
            print(f"Erro no login: {e}")
            return False

    def navegar_menu(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(SobralLocators.MENU_PRINCIPAL)
            ).click()
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SobralLocators.MENU_RELATORIOS)
            ).click()
            return True
        
        except Exception as e:
            print(f"Erro na navegação: {e}")
            return False
        
    def opcoes_relatorios(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(SobralLocators.DATA_INICIO)
            ).send_keys(data.DATA_OPERACOES)
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SobralLocators.DATA_FIM)
            ).send_keys(data.DATA_FINAL)
            
            #self.driver.execute_script(scroll_to_checkbox)
            time.sleep(1)
            #CHECKBOX
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SobralLocators.CHECKBOX_DEFERIDA)
            ).click()
            time.sleep(10)
            return True
        except Exception as e:
            print(f"Erro nas opções de relatório: {e}")
            return False     
        
