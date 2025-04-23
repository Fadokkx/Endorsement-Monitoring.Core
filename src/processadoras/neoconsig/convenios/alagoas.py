from src.processadoras.neoconsig.core.NeoConsig_date_var import variaveis_data as data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv()

class AlagoasLocators:
    SELEC_PORTAL = (By.XPATH, "/html/body/header/nav/div/div[2]/ul/li/a/button")
    PORTAL_CONSIG = (By.XPATH, '/html/body/header/nav/div/div[2]/ul/li/ul/li[3]/a')
    CAMPO_LOGIN = (By.XPATH, '//*[@id="login"]')
    BOTAO_SEQUENCIA = (By.XPATH,"/html/body/header/nav/div/div[4]/form/div/button")
    SELEC_CONVENIO_BOTAO = (By.XPATH, '//*[@id="s2id_cod_convenio"]/a')
    SELEC_CONVENIO_BUSCA = (By.XPATH, '//*[@id="s2id_autogen1_search"]')
    SELEC_ACESSO_BOTAO = (By.XPATH, '//*[@id="tipo_acesso"]')
    SELEC_ACESSO_OPCAO = (By.XPATH, '//*[@id="tipo_acesso"]/option[2]')
    CAMPO_CAPTCHA = (By.XPATH,'//*[@id="captcha_code"]')
    BOTAO_LOGIN = (By.XPATH,'//*[@id="servidor-form"]/div[6]/a')

    """
    BOTAO_NOVIDADES = (By.XPATH, '//*[@id="modalExibeBanners"]/div/div/div[1]/button')
    ABA_RELATORIO = (By.XPATH, '//*[@id="sidebar"]/ul/div[1]/div[2]/div/div/div/li[2]/a')
    SELEC_RELATORIO = (By.XPATH, '//*[@id="objeto_1009"]')
    DATA_INICIO = (By.XPATH, '//*[@id="de"]')
    DATA_FIM = (By.XPATH, '//*[@id="ate"]')
    ORDER_BY = (By.XPATH, '//*[@id="ordenar"]')
    OPCAO_REL = (By.XPATH, '//*[@id="opcao_geracao_relatorio"]')
    BOTAO_GERAR = (By.XPATH, '//*[@id="t_dadosp"]/tbody/tr[13]/td/p/input')
    TIPO_CSV = (By.XPATH, '//*[@id="opcao_geracao_relatorio"]/option[2]')
    """
class ConvenioAlagoas:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("NEOCONSIG_URL")
        self.user = os.getenv("NEOCONSIG_USER")
        
        if not all([self.url, self.user]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
        try:
            self.driver.get(self.url)
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AlagoasLocators.SELEC_PORTAL))
            self.driver.find_element(*AlagoasLocators.SELEC_PORTAL).click()
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AlagoasLocators.PORTAL_CONSIG))
            self.driver.find_element(*AlagoasLocators.PORTAL_CONSIG).click()
            
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(AlagoasLocators.CAMPO_LOGIN))
            self.driver.find_element(*AlagoasLocators.CAMPO_LOGIN).send_keys(self.user)
            time.sleep(0.5)
            self.driver.find_element(*AlagoasLocators.BOTAO_SEQUENCIA).click()
            
            time.sleep(4)
            
            self.driver.find_element(*AlagoasLocators.SELEC_CONVENIO_BOTAO).click()
            self.driver.find_element(*AlagoasLocators.SELEC_CONVENIO_BUSCA).send_keys("GOVERNO DO ESTADO DE ALAGOAS")
            self.driver.find_element(*AlagoasLocators.SELEC_CONVENIO_BUSCA).send_keys(Keys.ENTER)
            
            self.driver.find_element(*AlagoasLocators.SELEC_ACESSO_BOTAO).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(AlagoasLocators.SELEC_ACESSO_BOTAO))
            self.driver.find_element(*AlagoasLocators.SELEC_ACESSO_OPCAO).click()
            
            self.driver.find_element(By.XPATH, "/html/body").click()
            
            NC_CAPTCHA_RESOLVER = input("Digite o Captcha e aperte enter: ")
            self.driver.find_element(*AlagoasLocators.CAMPO_CAPTCHA).send_keys(NC_CAPTCHA_RESOLVER)
            
            self.driver.find_element(*AlagoasLocators.BOTAO_LOGIN).click()
            return True
        except Exception as e:
            pass
    
    def acesso_final(self):
        try:
            pass
        except:
            pass