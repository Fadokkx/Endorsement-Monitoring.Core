from src.processadoras.safeconsig.core.safeconsig_date_var import variaveis_data as data
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

class CearaLocators:
    CAMPO_USER = (By.XPATH, '//*[@id="idLogin"]')
    CAMPO_SENHA = (By.XPATH, '//*[@id="senhaUsuario"]')
    BOTAO_ENTRAR = (By.XPATH, '//*[@id="loginButtom"]/span[2]')
    ABA_RELATORIO = (By.XPATH, '//*[@id="menuform:j_idt146"]/a')
    MENU_MOVIMENT = (By.XPATH, '//*[@id="menuform:j_idt147"]/a')
    OPCAO_AVERB =(By.XPATH, '//*[@id="menuform:j_idt150"]/a')
    CAMPO_SERVICOS = (By.XPATH, '//*[@id="j_idt343:j_idt355:input_label"]')
    OPCAO_SAQUE = (By.XPATH, '//*[@id="j_idt343:j_idt355:input_1"]')
    CAMPO_DATA_INI = (By.XPATH, '//*[@id="j_idt343:j_idt393:j_idt393_input"]')
    CAMPO_DATA_FIM = (By.XPATH, '//*[@id="j_idt343:j_idt397:j_idt397_input"]')
    BOTAO_EXPORT_REL = (By.XPATH, '//*[@id="j_idt343:j_idt402"]/span[2]')
    OPCAO_CSV = (By.XPATH, "/html/body/div[1]/div[3]/div[3]/form/div/div/div/span/fieldset/div/button[3]/span[2]")
    
class ConvenioCeara:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("SAFECONSIG_CEARA_URL")
        self.user = os.getenv("SAFECONSIG_CEARA_USER")
        self.password = os.getenv("SAFECONSIG_CEARA_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    
    def login (self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CearaLocators.CAMPO_USER)
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CearaLocators.CAMPO_USER)).send_keys(self.user)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CearaLocators.CAMPO_SENHA)).send_keys(self.password)
            time.sleep(0.5)
            self.driver.find_element(*CearaLocators.BOTAO_ENTRAR).click()
            return True
            
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def navega_menu(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CearaLocators.ABA_RELATORIO)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CearaLocators.MENU_MOVIMENT)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CearaLocators.OPCAO_AVERB)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CearaLocators.CAMPO_SERVICOS)).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(CearaLocators.OPCAO_SAQUE)).click()
            time.sleep(0.1)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(CearaLocators.CAMPO_DATA_INI)).clear()
            self.driver.find_element(*CearaLocators.CAMPO_DATA_INI).send_keys(data.DATA_INICIAL)
            time.sleep(0.1)
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(CearaLocators.CAMPO_DATA_FIM)).clear()
            self.driver.find_element(*CearaLocators.CAMPO_DATA_FIM).send_keys(data.DATA_FINAL)
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"Erro {e}")
            return False
        
    def baixar_relatorio(self):
        try:
            WebDriverWait(self.driver, 3.5).until(
                EC.element_to_be_clickable(CearaLocators.BOTAO_EXPORT_REL)).click()
            time.sleep(0.1)
            try:
                self.driver.execute_script("document.body.style.zoom='80%'")
                WebDriverWait(self.driver, 2.5).until(
                    EC.element_to_be_clickable(CearaLocators.OPCAO_CSV)).click()
                time.sleep(0.1)
            except:
                print("Sem relatórios com o parâmetro desejado")
            return True
        
        except Exception as e:
            print(f"Erro {e}")
            return False