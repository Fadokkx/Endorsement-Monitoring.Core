from src.processadoras.sig.core.sig_date_var import variaveis_data as data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv()
class SantaCatarinaLocators:
    CAMPO_USER = (By.XPATH, '//*[@id="content"]/div/app-auth-page/div/div/form/fieldset/input[1]')
    CAMPO_SENHA = (By.XPATH, '//*[@id="content"]/div/app-auth-page/div/div/form/fieldset/input[2]')
    CAMPO_CAPTCHA = (By.XPATH, '//*[@id="content"]/div/app-auth-page/div/div/form/fieldset/div/input')
    BOTAO_ENTRAR = (By.XPATH, '//*[@id="content"]/div/app-auth-page/div/div/form/fieldset/fieldset[1]/button')
    ABA_RELATORIO = (By.XPATH, '//*[@id="accordionSidebar"]/li[2]/a')
    CAMPO_DATA_INI = (By.XPATH, '//*[@id="content"]/div/app-propostaemprestimo/div[2]/div/div/div/form/div[3]/div[1]/div/div[1]/app-datepicker-input/div/input')
    CAMPO_DATA_FIM = (By.XPATH, '//*[@id="content"]/div/app-propostaemprestimo/div[2]/div/div/div/form/div[3]/div[1]/div/div[2]/app-datepicker-input/div/input')
    BOTAO_CONSULTAR = (By.XPATH, '//*[@id="btnConsultar"]')
    BOTAO_DOWNLOAD = (By.XPATH, '//*[@id="content"]/div/app-propostaemprestimo/div[2]/div/div/div/form/div[4]/div/button[2]')
        
class ConvenioSantaCatarina:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("SIGCONSIG_SANTA_CATARINA_URL")
        self.user = os.getenv("SIGCONSIG_USER")
        self.password = os.getenv("SIGCONSIG_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
        
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(SantaCatarinaLocators.CAMPO_USER)).send_keys(self.user)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(SantaCatarinaLocators.CAMPO_SENHA)).send_keys(self.password)
            
            SigConsigCaptchaResolver = input("Resolva o captcha e pressione Enter...: ")
            self.driver.find_element(*SantaCatarinaLocators.CAMPO_CAPTCHA).send_keys(SigConsigCaptchaResolver)
            self.driver.find_element(*SantaCatarinaLocators.BOTAO_ENTRAR).click()
            time.sleep (10)
            return True
            
        except Exception as e:
            print(f"Erro no login: {e}")
            return False
        
    def navega_menu(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(SantaCatarinaLocators.ABA_RELATORIO)).click()
            return True
        except Exception as e:
            print (f"Erro: {e}")
            return False
            
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SantaCatarinaLocators.CAMPO_DATA_INI)).send_keys(data.DATA_INICIO)
            time.sleep(0.1)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(SantaCatarinaLocators.CAMPO_DATA_FIM)).send_keys(data.DATA_FINAL)
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
            
    def baixar_relatorio(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(SantaCatarinaLocators.BOTAO_CONSULTAR)).click()
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(SantaCatarinaLocators.BOTAO_DOWNLOAD)).click()
                return True
            except:
                print("Sem relatórios com os parâmetros")
                return True
        except Exception as e:
            print(f"Erro: {e}")
            return False