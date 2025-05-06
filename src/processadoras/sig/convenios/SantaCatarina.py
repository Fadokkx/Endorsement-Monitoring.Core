from src.processadoras.zetra.core.zetra_date_var import variaveis_data as data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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