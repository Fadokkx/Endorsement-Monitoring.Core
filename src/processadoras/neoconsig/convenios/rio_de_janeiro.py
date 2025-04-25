from src.processadoras.neoconsig.core.NeoConsig_date_var import variaveis_data as data
from src.processadoras.neoconsig.core.senha_automatizada import TecladoVirtualNeoConsig as VK
from src.processadoras.neoconsig.core.neoconsig_coord import NeoConsigCoord as NCC
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

class RioLocators:
    ACESSO_CONSIGNATARIA = (By.XPATH, '//*[@id="btn-acessar-sistema"]')
    SELEC_ACESSO = (By.XPATH, '//*[@id="tipo_acesso"]')
    SELEC_TIPO_ACESSO = (By.XPATH, '//*[@id="tipo_acesso"]/option[2]')
    CAMPO_LOGIN = (By.XPATH, '//*[@id="cod_acesso"]')
    CAMPO_CAPTCHA = (By.XPATH, '//*[@id="captcha_code"]')
    BOTAO_LOGIN = (By.XPATH, '//*[@id="servidor-form"]/div[3]/button[1]')
    BOTAO_SENHA = (By.XPATH, '//*[@id="senha"]')
    MENU_COMERCIAL = (By.XPATH, '/html/body/div[5]/div[1]/div/ul/li[4]/a')
    ABA_CONSIGNACOES = (By.XPATH, '/html/body/div[5]/div[1]/div/ul/li[4]/ul/li/a')
    OPCAO_CONSULTAR = (By.XPATH, '/html/body/div[5]/div[1]/div/ul/li[4]/ul/li/ul/li/a')
    BOTAO_MES = (By.XPATH, '//*[@id="s2id_mes"]/a')
    BUSCA_MES = (By.XPATH, '//*[@id="s2id_autogen1_search"]')
    BOTAO_ANO = (By.XPATH, '//*[@id="s2id_ano"]/a')
    BUSCA_ANO = (By.XPATH, '//*[@id="s2id_autogen2_search"]')
    BOTAO_TIPO_CSV = (By.XPATH, '//*[@id="content"]/div[2]/div/div/div[1]/div[3]/div[3]/div/div/div/a[2]')


class ConvenioRio:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("RIOCONSIG_URL")
        self.refresh = os.getenv("RIOCONSIG_REFRESH_URL")
        self.user = os.getenv("NEOCONSIG_USER")
        self.password = os.getenv("NEOCONSIG_PASS")
        
        if not all([self.url, self.user, self.password, self.refresh]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RioLocators.ACESSO_CONSIGNATARIA)).click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RioLocators.SELEC_ACESSO)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RioLocators.SELEC_TIPO_ACESSO)).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(RioLocators.CAMPO_LOGIN))
            self.driver.find_element(*RioLocators.CAMPO_LOGIN).send_keys(self.user)
            time.sleep(1)
            NC_CAPTCHA_RESOLVER = input("Digite o Captcha e aperte enter: ")
            self.driver.find_element(*RioLocators.CAMPO_CAPTCHA).send_keys(NC_CAPTCHA_RESOLVER)
            self.driver.find_element(*RioLocators.BOTAO_LOGIN).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
    
    def acesso_senha(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(RioLocators.BOTAO_SENHA)).click()

            senha = VK(self.driver)
            if not senha.enter_password(self.password):
                raise Exception("Falha ao inserir senha no teclado virtual")
            time.sleep(2)
            
            pg.moveTo(NCC.Login_pos_senha_rio, duration= 1)
            pg.click()
            time.sleep(3)
            return True
        
        except Exception as e:
            print(f"ERRO no acesso_final: {str(e)}")
    
    def navega_menu(self):
        try:
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RioLocators.MENU_COMERCIAL)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RioLocators.ABA_CONSIGNACOES)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RioLocators.OPCAO_CONSULTAR)).click()
            self.driver.get(self.refresh)
            time.sleep(3)
            return True
        except Exception as e:
            print (f"{e}")
            return False
        
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RioLocators.BOTAO_MES)).click()
            self.driver.find_element(*RioLocators.BUSCA_MES).send_keys(data.MES_ATUAL)
            self.driver.find_element(*RioLocators.BUSCA_MES).send_keys(Keys.ENTER)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RioLocators.BOTAO_ANO)).click()
            self.driver.find_element(*RioLocators.BUSCA_ANO).send_keys(data.ANO_ATUAL)
            self.driver.find_element(*RioLocators.BUSCA_ANO).send_keys(Keys.ENTER)
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Erro {e}")
            return False
            
    def download_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RioLocators.BOTAO_TIPO_CSV)).click()
            time.sleep(30)
            return True
        except Exception as e:
            print (f"Erro {e}")
            return False