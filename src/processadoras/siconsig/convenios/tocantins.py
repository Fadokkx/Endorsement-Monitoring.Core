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
    CAMPO_DASHBOARD =(By.XPATH, '//*[@id="grpmenu1"]')
    ABA_CONSIGNANTES = (By.XPATH, "/html/body/div[1]/div[1]/div/div[4]/div/ul[2]/li/a")
    ABA_PESQUISAR = (By.XPATH, '//*[@id="kname8"]')
    OPCAO_RELATORIO = (By.XPATH, '//*[@id="drop4"]')
    REL_CUSTOM = (By.XPATH,'//*[@id="menu4"]/li[1]/a')
    CAMPO_PESQUISA = (By.XPATH, "/html/body/div/div[2]/div[2]/div/input")
    SELEC_REL = (By.XPATH, "/html/body/div/div[2]/div[2]/ul/li/a")
    BOTAO_GERAR = (By.XPATH, '//*[@id="CadDoRelatorio"]/div/div[3]/input[1]')
    GERACAO_DOWNLOAD = (By.XPATH, '//*[@id="PParametrosRpor"]/div/div[2]/input[1]')
    GERACAO_RELATORIO = (By.XPATH, "/html/body/div/div[3]/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/p")
    
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
            time.sleep(2)
            return True
            
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def navega_menu (self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(TocantinsLocators.CAMPO_DASHBOARD)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TocantinsLocators.ABA_CONSIGNANTES)).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(TocantinsLocators.ABA_PESQUISAR)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return True
        
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TocantinsLocators.OPCAO_RELATORIO)).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(TocantinsLocators.REL_CUSTOM)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def download_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TocantinsLocators.CAMPO_PESQUISA)).send_keys("averb")
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(TocantinsLocators.SELEC_REL)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TocantinsLocators.BOTAO_GERAR)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TocantinsLocators.GERACAO_DOWNLOAD)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TocantinsLocators.GERACAO_RELATORIO)).click()
            return True 
        
        except Exception as e:
            print(f"Erro: {e}")
            return False