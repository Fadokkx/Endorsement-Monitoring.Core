from src.processadoras.neoconsig.core.NeoConsig_date_var import variaveis_data as data
from src.processadoras.neoconsig.core.senha_automatizada import TecladoVirtualNeoConsig as VK
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
    BOTAO_SENHA = (By.XPATH, '//*[@id="senha"]')
    BOTAO_ACESSO = (By.CLASS_NAME, "/html/body/div[4]/div/div/div[2]/div[1]/div[2]/form/div[2]/button[1]")
    CAMPO_SENHA = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[1]/div[2]/form/div[1]/input')


class ConvenioAlagoas:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("NEOCONSIG_URL")
        self.user = os.getenv("NEOCONSIG_USER")
        self.password = os.getenv("NEOCONSIG_PASS")
        
        if not all([self.url, self.user, self.password]):
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
            self.driver.find_element(*AlagoasLocators.SELEC_CONVENIO_BUSCA).send_keys("GOIáS - GOV. DO ESTADO")
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
    
    def acesso_senha(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(AlagoasLocators.BOTAO_SENHA)).click()

            senha = VK(self.driver)
            if not senha.enter_password(self.password):
                raise Exception("Falha ao inserir senha no teclado virtual")
            time.sleep(4)
            
            self.driver.find_element(*AlagoasLocators.CAMPO_SENHA).send_keys(Keys.TAB)
            self.driver.find_element(*AlagoasLocators.CAMPO_SENHA).send_keys(Keys.ENTER)
            time.sleep(10)
            return True
        
        except Exception as e:
            print(f"ERRO no acesso_final: {str(e)}")