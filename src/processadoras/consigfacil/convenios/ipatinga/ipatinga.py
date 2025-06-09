from src.processadoras.consigfacil.convenios.ipatinga.locators import IpatingaLocators
from src.processadoras.consigfacil.core.consigfacil_date_var import variaveis_data as data
from src.processadoras.consigfacil.core.cf_paths import Diretorios_Imagem as DI
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
    
class ConvenioIpatinga:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("CONSIGFACIL_IPATINGA_URL")
        self.user = os.getenv("CONSIGFACIL_USER")
        self.password = os.getenv("CONSIGFACIL_PASS")
        self.second_password = os.getenv("CONSIGFACIL_SECOND_PASS")
        
        if not all([self.url, self.user, self.password, self.second_password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(IpatingaLocators.CAMPO_LOGIN)).send_keys(self.user)
            self.driver.find_element(*IpatingaLocators.CAMPO_SENHA).send_keys(self.second_password)
            CF_CAPTCHA_RESOLVER = input ("Digite o Captcha: ")
            self.driver.find_element(*IpatingaLocators.CAMPO_CAPTCHA).send_keys(CF_CAPTCHA_RESOLVER)
            self.driver.find_element(*IpatingaLocators.CAMPO_CAPTCHA).send_keys(Keys.ENTER)
            try:
                WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located(IpatingaLocators.ABA_RELATORIO))
                return True
            except:
                print("Captcha digitado incorretamente, tentar novamente")
    
            while True:
                try:
                    WebDriverWait(self.driver, 1).until(
                        EC.presence_of_element_located(IpatingaLocators.CAMPO_LOGIN)).send_keys(self.user)
                    self.driver.find_element(*IpatingaLocators.CAMPO_SENHA).send_keys(self.second_password)
                    CF_CAPTCHA_RESOLVER = input ("Digite o Captcha: ")
                    self.driver.find_element(*IpatingaLocators.CAMPO_CAPTCHA).send_keys(CF_CAPTCHA_RESOLVER)
                    self.driver.find_element(*IpatingaLocators.CAMPO_CAPTCHA).send_keys(Keys.ENTER)
                    WebDriverWait(self.driver, 1.5).until(
                        EC.presence_of_element_located(IpatingaLocators.ABA_RELATORIO))
                    return True
                except:
                    print("Captcha digitado incorretamente, tentar novamente")
                    time.sleep(0.5)
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def troca_senha(self):
        try:
            try:
                self.driver.find_element(*IpatingaLocators.CAMPO_SENHA_TROCA).click()
                self.driver.find_element(*IpatingaLocators.CAMPO_SENHA_TROCA).send_keys(self.second_password)
                time.sleep(0.5)
                WebDriverWait(self.driver, 1.5).until(
                    EC.element_to_be_clickable(IpatingaLocators.CAMPO_NOVA_SENHA_TROCA)).send_keys(self.password)
                WebDriverWait(self.driver, 1.5).until(
                    EC.element_to_be_clickable(IpatingaLocators.CAMPO_NOVA_SENHA_CONFIRMA)).send_keys(self.password)
                time.sleep(0.3)
                WebDriverWait(self.driver, 1.0).until(
                    EC.element_to_be_clickable(IpatingaLocators.BODY)).click()
                self.driver.find_element(*IpatingaLocators.BODY).send_keys(Keys.PAGE_DOWN)
                time.sleep(0.1)
                WebDriverWait(self.driver, 1.5).until(
                    EC.element_to_be_clickable(IpatingaLocators.BOTAO_ENTRAR_TROCA_SENHA)).click()
                return True
            except Exception as e:
                print(f"Erro: {e}")
                return False
        except:
            print("Sem necessidade de troca de senha")
            return True

    def confirmacao_leitura_novidades(self):
        try:
            try:
                if not self.driver.find_element(*IpatingaLocators.BOTAO_NOVIDADES).click():
                    raise Exception("Sem novidades")
            except Exception as e:
                print("Sem novidades.")
            
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(IpatingaLocators.BOTAO_CONFIRMA_LEITURA)
                )
                if not self.driver.find_element(*IpatingaLocators.BOTAO_CONFIRMA_LEITURA).click():
                    raise Exception("Sem novidades")
                print(f"Erro {e}")
            except Exception as e:
                print(f"Erro: {e}")
            return True
            
        except Exception as e:
                print(f"Erro: {e}")
                return False
            
    def navega_menu(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(IpatingaLocators.ABA_RELATORIO)).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(IpatingaLocators.SELEC_RELATORIO)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
        
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(IpatingaLocators.DATA_INICIO)).send_keys(data.DATA_OPERACOES)
            self.driver.find_element(*IpatingaLocators.DATA_FIM).send_keys(data.DATA_FINAL)
            time.sleep(0.1)
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(IpatingaLocators.OPCAO_REL)).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(IpatingaLocators.TIPO_CSV)).click()
            return True

        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def baixar_relatorio(self):
        try:
            self.driver.execute_script("document.body.style.zoom='80%'")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(IpatingaLocators.BOTAO_GERAR)).click()
            time.sleep(1.5)
            pg.hotkey('ctrl', 'w')
            time.sleep(0.1)
            pg.hotkey('ctrl', 'w')
            return True
        except Exception as e:
            print (f"Erro: {e}")
            return False
        