from src.processadoras.digitalconsig.core.digitalconsig_date_var import variaveis_data as data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os
import pyautogui as pg

load_dotenv()

class SorrisoLocators:
    CAMPO_USER = (By.ID, 'txtLogin')
    CAMPO_SENHA = (By.ID, 'txtSenha')
    BOTAO_ENTRAR = (By.XPATH, "/html/body/div/div[1]/form/div[3]/div/div/div/div/div[2]/input[1]")
    CAMPO_SELEC_ORGAO = (By.XPATH, '//*[@id="body_btnVincular"]')
    ABA_CONSULTA = (By.XPATH, '//*[@id="menu1"]/div/div/div/ul/li[2]/a')
    OPCAO_CONSULTA =(By.XPATH, '//*[@id="menu1"]/div/div/div/ul/li[2]/ul/li/a')
    CAMPO_DATA_INI = (By.XPATH, '//*[@id="body_dataIniTextBox"]')
    CAMPO_DATA_FIM = (By.XPATH, '//*[@id="body_dataFinTextBox"]')
    BOTAO_PESQUISAR = (By.XPATH, '//*[@id="body_pesquisarButton"]')
    BOTAO_EXPORT_REL = (By.XPATH, '//*[@id="body_btn_exportar"]')
    
class ConvenioSorriso:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("DIGITALCONSIG_SORRISO_URL")
        self.user = os.getenv("DIGITALCONSIG_USER")
        self.password = os.getenv("DIGITALCONSIG_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    
    def login (self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SorrisoLocators.BOTAO_ENTRAR)
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SorrisoLocators.CAMPO_USER)).send_keys(self.user)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SorrisoLocators.CAMPO_SENHA)).send_keys(self.password)
            time.sleep(0.5)
            self.driver.find_element(*SorrisoLocators.BOTAO_ENTRAR).click()
            return True
            
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def navega_menu(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SorrisoLocators.CAMPO_SELEC_ORGAO)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SorrisoLocators.ABA_CONSULTA)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SorrisoLocators.OPCAO_CONSULTA)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(SorrisoLocators.CAMPO_DATA_INI)).send_keys(data.DATA_INICIAL)
            time.sleep(0.1)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(SorrisoLocators.CAMPO_DATA_FIM)).send_keys(data.DATA_FINAL)
            time.sleep(0.1)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(SorrisoLocators.BOTAO_PESQUISAR)).click()
            return True
        except Exception as e:
            print(f"Erro {e}")
            return False
        
    def baixar_relatorio(self):
        try:
            WebDriverWait(self.driver, 3.5).until(
                EC.element_to_be_clickable(SorrisoLocators.BOTAO_EXPORT_REL)).click()
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Erro {e}")
            return False