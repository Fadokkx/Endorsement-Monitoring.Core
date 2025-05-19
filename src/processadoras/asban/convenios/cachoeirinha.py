from src.processadoras.asban.core.asban_date_var import variaveis_data as data
from src.processadoras.asban.core.asban_paths import Diretorios_Imagem as DI
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

class CachoerinhaLocator:
    BOTAO_ENTRAR = (By.XPATH, '/html/body/section/div/div[2]/a')
    CAMPO_LOGIN = (By.XPATH, '//*[@id="id_username"]')
    CAMPO_SENHA = (By.XPATH, '//*[@id="id_password"]')
    CAMPO_CAPTCHA_BOTAO = (By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
    BOTAO_LOGIN = (By.XPATH, '//*[@id="submete_login"]')
    ABA_RELATORIO = (By.XPATH, '/html/body/div[1]/div/div[2]/ul/li[3]/a')
    CAMPO_PERIODO = (By.XPATH, '//*[@id="dtperiodo"]')
    BOTAO_CONFIRMA_PERIODO = (By.XPATH, '/html/body/div[2]/div[3]/div/button[1]')
    OPCAO_TODOS_ORGAOS = (By.XPATH, '//*[@id="orgao"]/option[1]')
    TIPO_CSV = (By.XPATH, "/html/body/section/div/div/form/div[2]/table/tbody/tr[2]/td[2]/button[3]")
    
    
class ConvenioCachoeirinha:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("ASBAN_CACHOEIRINHA_URL")
        self.user = os.getenv("ASBAN_USER")
        self.password = os.getenv("ASBAN_PASS")
        
        if not all ([self.url, self.user, self.password]):
            raise ValueError("Variaveis de ambiente faltando")
        
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CachoerinhaLocator.CAMPO_LOGIN)).send_keys(self.user)
            self.driver.find_element(*CachoerinhaLocator.CAMPO_SENHA).send_keys(self.password)
            
            campo_captcha = pg.locateOnScreen(
                DI.campo_captcha,
                confidence=0.8,
                minSearchTime=3
            )
            pg.moveTo(campo_captcha)
            pg.click()
            
            #Tempo pra clicar e fazer o captcha
            time.sleep(5)
            self.driver.find_element(*CachoerinhaLocator.BOTAO_LOGIN).click()
            time.sleep(1)
            return True
        
        except Exception as e:
            print(f"Erro {e}")
            return False
               
    def navega_menu(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(CachoerinhaLocator.ABA_RELATORIO)).click()
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Erro {e}")
            return False
    
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(CachoerinhaLocator.CAMPO_PERIODO)).send_keys(data.PERIODO_ASBAN)
            self.driver.find_element(*CachoerinhaLocator.BOTAO_CONFIRMA_PERIODO).click()
            self.driver.find_element(*CachoerinhaLocator.OPCAO_TODOS_ORGAOS).click()
            time.sleep(1)
            return True
            
        except Exception as e:
            print(f"Erro {e}")
            return False
    
    def download_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CachoerinhaLocator.TIPO_CSV)).click()
            time.sleep(1.5)
            return True
        except Exception as e:
            print(f"Erro {e}")
            return False