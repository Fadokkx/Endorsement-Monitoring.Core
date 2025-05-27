from src.processadoras.proconsig.core.proconsig_date_var import variaveis_data as data
from src.processadoras.proconsig.core.pc_paths import Diretorios_Imagem as DI
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

class PoaLocators:
    CAMPO_CODIGO = (By.XPATH, "/html/body/form/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/input")
    CAMPO_USUARIO = (By.XPATH, "/html/body/form/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input")
    CAMPO_SENHA = (By.XPATH, "/html/body/form/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/input")
    BOTAO_LOGIN = (By.XPATH, "/html/body/form/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td[2]/input")
    OPC_CONSIGNACAO = (By.XPATH, "/html/body/div/div[2]")
    CAMPO_DATA_INI = (By.XPATH, "/html/body/form/center/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input")
    CAMPO_DATA_FIM = (By.XPATH, "/html/body/form/center/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td[5]/input")
    BOTAO_PESQUISAR = (By.XPATH, "/html/body/form/center/table/tbody/tr[2]/td/table/tbody/tr/td/div/input")
    BOTAO_DOWNLOAD = (By.XPATH, "/html/body/form/div[1]/center/table/tbody/tr/td[1]/input[2]")

class ConvenioPortoAlegre:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("PROCONSIG_URL")
        self.user = os.getenv("PROCONSIG_USER")
        self.codigo_promotora = os.getenv("PROCONSIG_CODE_PROMOT")
        self.password = os.getenv("PROCONSIG_PASS")
        
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(PoaLocators.CAMPO_CODIGO)).send_keys(self.codigo_promotora)
            self.driver.find_element(*PoaLocators.CAMPO_USUARIO).send_keys(self.user)
            self.driver.find_element(*PoaLocators.CAMPO_SENHA).send_keys(self.password)
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(PoaLocators.BOTAO_LOGIN)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def navegar_menu(self):
        try:
            AbaRelatorio = pg.locateOnScreen(
                DI.aba_relatorio,
                confidence=0.9,
                minSearchTime=5
            )
            pg.moveTo(AbaRelatorio)
            
            Opcao_consign = pg.locateOnScreen(
                DI.opcao_consignacao,
                confidence=0.9,
                minSearchTime=3
            )
            pg.moveTo(Opcao_consign)
            pg.click()            
            return True
        except Exception as e:
            print(f"Erro: {e}")
    
    def Opcoes_Relatorios(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(PoaLocators.CAMPO_DATA_INI)).send_keys(data.DATA_OPERACOES)
            self.driver.find_element(*PoaLocators.CAMPO_DATA_FIM).send_keys(data.DATA_FINAL)
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(PoaLocators.BOTAO_PESQUISAR)).click()
            time.sleep(0.7)
            return True
        except Exception as e:
            print(f"Erro: {e}")
    
    def download_arquivo(self):
        try:
            WebDriverWait(self.driver, 120).until(
                EC.element_to_be_clickable(PoaLocators.BOTAO_DOWNLOAD)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
        