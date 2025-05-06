from src.processadoras.consigtec.core.consigtec_date_var import variaveis_data as data
from src.processadoras.consigtec.core.check_report import Diretorios_Imagem as DI
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os
import pyautogui as pg

load_dotenv()

class PortoNacionalLocators:
    CAMPO_USER = (By.XPATH, '//*[@id="username"]')
    CAMPO_SENHA = (By.XPATH, '//*[@id="password"]')
    BOTAO_ENTRAR = (By.XPATH, '//*[@id="form"]/div/div/div[2]/div[1]/div[3]/div[2]/div[2]/button')
    BOTAO_PERFIL = (By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/a')
    BOTAO_TROCA_PERFIL = (By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/ul/li[3]/ul/li[3]/a')
    OPCAO_PORTO_NACIONAL = (By.XPATH, '//*[@id="j_idt73:tbl_data"]/tr[4]/td[1]/div/a')
    MENU_RELATORIO = (By.XPATH, '//*[@id="menuform:j_idt107"]/a')
    OPCAO_PRODUCAO = (By.XPATH, '//*[@id="menuform:j_idt109"]/a')
    CAMPO_DATA_INI = (By.XPATH, '//*[@id="j_idt169:startDate_input"]')
    CAMPO_DATA_FIM = (By.XPATH, '//*[@id="j_idt169:endDate_input"]')
    BOTAO_OPERACOES = (By.XPATH, '//*[@id="j_idt169:j_idt181"]')
    OPCAO_OPERACAO_ATIVA = (By.XPATH, '//*[@id="j_idt169:j_idt181_1"]')
    BOTAO_GERAR = (By.XPATH, '//*[@id="j_idt169"]/div[2]/div/div/table/tbody/tr/td/input')
    
class ConvenioPortoNacional:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("CONSIGTEC_MARINGA_URL")
        self.user = os.getenv("CONSIGTEC_USER")
        self.password = os.getenv("CONSIGTEC_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    
    def login (self):
        try:
            try:
                WebDriverWait(self.driver, 1.5).until(
                    EC.element_to_be_clickable(PortoNacionalLocators.BOTAO_PERFIL)).click()
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(PortoNacionalLocators.BOTAO_TROCA_PERFIL)).click()
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(PortoNacionalLocators.OPCAO_PORTO_NACIONAL)).click()
                return True
            
            except:
                self.driver.get(self.url)
                self.driver.find_element(*PortoNacionalLocators.CAMPO_USER).click()
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(PortoNacionalLocators.CAMPO_USER)).send_keys(self.user)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(PortoNacionalLocators.CAMPO_SENHA)).send_keys(self.password)
                self.driver.find_element(*PortoNacionalLocators.BOTAO_ENTRAR).click()
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(PortoNacionalLocators.OPCAO_PORTO_NACIONAL)).click()
                return True
            
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def navega_meu(self):
        try:
            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(PortoNacionalLocators.MENU_RELATORIO)).click()
            WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(PortoNacionalLocators.OPCAO_PRODUCAO)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(PortoNacionalLocators.CAMPO_DATA_INI)).send_keys(data.DATA_INICIO)
            time.sleep(1)
            self.driver.find_element(*PortoNacionalLocators.CAMPO_DATA_FIM).click()
            WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(PortoNacionalLocators.CAMPO_DATA_FIM)).send_keys(data.DATA_FINAL)
            time.sleep(0.1)
            return True
        except Exception as e:
            print (f"Erro: {e}")
            return False
        
    def download_relatorio(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(PortoNacionalLocators.BOTAO_GERAR)).click()
            time.sleep(1)
            try:
                pg.locateOnScreen(
                    DI.sem_relatorio,
                    confidence= 0.8,
                    minSearchTime= 1.5
                )
                print("Sem relatórios encontrados com os parâmetros")
                return True
            except Exception as e:
                print (f"Erro: {e}")
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False