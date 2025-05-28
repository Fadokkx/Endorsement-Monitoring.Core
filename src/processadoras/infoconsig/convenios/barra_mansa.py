from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv()

class BarraMansaLocators:
    CAMPO_USER = (By.XPATH, '//*[@id="username"]')
    CAMPO_SENHA = (By.XPATH, '//*[@id="password"]')

class ConvenioBarraMansa:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("INFOCONSIG_URL")
        self.user = os.getenv("INFOCONSIG_USER")
        self.password = os.getenv("INFOCONSIG_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
        
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(BarraMansaLocators.CAMPO_USER)).send_keys(self.user)
            time.sleep(0.1)
            self.driver.find_element(*BarraMansaLocators.CAMPO_USER).send_keys(Keys.ENTER)
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(BarraMansaLocators.CAMPO_SENHA)).send_keys(self.password)
            time.sleep(0.1)
            self.driver.find_element(*BarraMansaLocators.CAMPO_SENHA).send_keys(Keys.ENTER)
            
            time.sleep(10)
            return True
        except Exception as e:
            print(f"Erro: {e}")