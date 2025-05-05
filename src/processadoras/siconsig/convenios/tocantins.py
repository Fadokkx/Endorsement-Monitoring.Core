from src.processadoras.serpro.core.serpro_date_var import variaveis_data as data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os
import pyautogui as pg

load_dotenv()

class TocantinsLocators:
    CAMPO_USER = (By.XPATH, '//*[@id="login-email"]')
    CAMPO_SENHA = (By.XPATH, '//*[@id="login-password"]')
    BOTAO_ENTRAR = (By.XPATH, '//*[@id="btacesso"]')
    
class ConvenioTocantins:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("SICONSIG_TOCANTINS_URL")
        self.user = os.getenv("SICONSIG_USER")
        self.password = os.getenv("SICONSIG_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    
    def login (self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TocantinsLocators.BOTAO_ENTRAR)
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TocantinsLocators.CAMPO_USER)).send_keys(self.user)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TocantinsLocators.CAMPO_SENHA)).send_keys(self.password)
            time.sleep(0.5)
            self.driver.find_element(*TocantinsLocators.BOTAO_ENTRAR).click()
            time.sleep(10)
            return True
            
        except Exception as e:
            print(f"Erro: {e}")
            return False