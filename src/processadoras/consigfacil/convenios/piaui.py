from src.processadoras.consigfacil.core.consigfacil_date_var import variaveis_data as data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv()

class PiauiLocators:
    CAMPO_LOGIN = (By.XPATH, '//*[@id="usuario"]')
    CAMPO_SENHA = (By.XPATH,'//*[@id="senha"]')
    CAMPO_CAPTCHA = (By.XPATH,'//*[@id="captcha"]')
    BOTAO_LOGIN = (By.XPATH,'//*[@id="html"]/body/div[1]/div[2]/form/button')
    BOTAO_CONFIRMA_LEITURA = (By.XPATH, '//*[@id="staticBackdrop"]/div/div/div[3]/button[1]')
    BOTAO_NOVIDADES = (By.XPATH, '//*[@id="modalExibeBanners"]/div/div/div[1]/button')
    ABA_RELATORIO = (By.XPATH, '//*[@id="sidebar"]/ul/div[1]/div[2]/div/div/div/li[2]/a')
    SELEC_RELATORIO = (By.XPATH, '//*[@id="objeto_1009"]')
    DATA_INICIO = (By.XPATH, '//*[@id="de"]')
    DATA_FIM = (By.XPATH, '//*[@id="ate"]')
    ORDER_BY = (By.XPATH, '//*[@id="ordenar"]')
    OPCAO_REL = (By.XPATH, '//*[@id="opcao_geracao_relatorio"]')
    BOTAO_GERAR = (By.XPATH, '//*[@id="t_dadosp"]/tbody/tr[13]/td/p/input')
    TIPO_CSV = (By.XPATH, '//*[@id="opcao_geracao_relatorio"]/option[2]')
    CAMPO_SENHA_TROCA = (By.XPATH, '//*[@id="t_dadosp"]/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
    CAMPO_NOVA_SENHA_TROCA = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td/input")
    CAMPO_NOVA_SENHA_CONFIRMA = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/form/table/tbody/tr[2]/td/table/tbody/tr[6]/td/input")
    BOTAO_ENTRAR_TROCA_SENHA = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div/div/form/table/tbody/tr[3]/td/input")
    BODY = (By.XPATH, "/html/body")
    
class ConvenioPiaui:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("CONSIGFACIL_PIAUI_URL")
        self.user = os.getenv("CONSIGFACIL_USER")
        self.password = os.getenv("CONSIGFACIL_PASS")
        self.second_password = os.getenv("CONSIGFACIL_SECOND_PASS")
        
        if not all([self.url, self.user, self.password, self.second_password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PiauiLocators.CAMPO_LOGIN)
            )
            self.driver.find_element(*PiauiLocators.CAMPO_LOGIN).send_keys(self.user)
            self.driver.find_element(*PiauiLocators.CAMPO_SENHA).send_keys(self.password)
            CF_CAPTCHA_RESOLVER = input ("Digite o Captcha: ")
            self.driver.find_element(*PiauiLocators.CAMPO_CAPTCHA).send_keys(CF_CAPTCHA_RESOLVER)
            self.driver.find_element(*PiauiLocators.CAMPO_CAPTCHA).send_keys(Keys.ENTER)
            try:
                WebDriverWait(self.driver, 1.5).until(
                        EC.element_to_be_clickable(PiauiLocators.ABA_RELATORIO))
                return True
            except:
                print("Captcha digitado incorretamente, tentar novamente")
    
            while True:
                try:
                    WebDriverWait(self.driver, 1).until(
                        EC.presence_of_element_located(PiauiLocators.CAMPO_LOGIN)).send_keys(self.user)
                    self.driver.find_element(*PiauiLocators.CAMPO_SENHA).send_keys(self.password)
                    CF_CAPTCHA_RESOLVER = input ("Digite o Captcha: ")
                    self.driver.find_element(*PiauiLocators.CAMPO_CAPTCHA).send_keys(CF_CAPTCHA_RESOLVER)
                    self.driver.find_element(*PiauiLocators.CAMPO_CAPTCHA).send_keys(Keys.ENTER)
                    WebDriverWait(self.driver, 1.5).until(
                        EC.element_to_be_clickable(PiauiLocators.ABA_RELATORIO)) 
                    return True
                except:
                    print("Captcha digitado incorretamente, tentar novamente")
                    time.sleep(0.5)
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def troca_senha(self):
        try:
            WebDriverWait(self.driver, 1.5).until(
                EC.element_to_be_clickable(PiauiLocators.CAMPO_NOVA_SENHA_CONFIRMA))
            self.driver.find_element(*PiauiLocators.CAMPO_SENHA_TROCA).click()
            self.driver.find_element(*PiauiLocators.CAMPO_SENHA_TROCA).send_keys(self.password)
            time.sleep(0.5)
            WebDriverWait(self.driver, 1.5).until(
                EC.element_to_be_clickable(PiauiLocators.CAMPO_NOVA_SENHA_TROCA)).send_keys(self.second_password)
            WebDriverWait(self.driver, 1.5).until(
                EC.element_to_be_clickable(PiauiLocators.CAMPO_NOVA_SENHA_CONFIRMA)).send_keys(self.second_password)
            time.sleep(0.3)
            self.driver.find_element(*PiauiLocators.BODY).send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
            WebDriverWait(self.driver, 1.5).until(
                EC.element_to_be_clickable(PiauiLocators.BOTAO_ENTRAR_TROCA_SENHA)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False 
    def confirmacao_leitura_novidades(self):
        try:
            try:
                if not self.driver.find_element(*PiauiLocators.BOTAO_NOVIDADES).click():
                    raise Exception("Sem novidades")
            except Exception as e:
                print("Sem novidades.")
            
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(PiauiLocators.BOTAO_CONFIRMA_LEITURA)
                )
                if not self.driver.find_element(*PiauiLocators.BOTAO_CONFIRMA_LEITURA).click():
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
                EC.element_to_be_clickable(PiauiLocators.ABA_RELATORIO)
            )
            self.driver.find_element(*PiauiLocators.ABA_RELATORIO).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(PiauiLocators.SELEC_RELATORIO)
            )
            self.driver.find_element(*PiauiLocators.SELEC_RELATORIO).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
        
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PiauiLocators.DATA_INICIO)
            )
            self.driver.find_element(*PiauiLocators.DATA_INICIO).send_keys(data.DATA_OPERACOES)
            self.driver.find_element(*PiauiLocators.DATA_FIM).send_keys(data.DATA_FINAL)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.find_element(*PiauiLocators.OPCAO_REL).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PiauiLocators.TIPO_CSV)
            )
            self.driver.find_element(*PiauiLocators.TIPO_CSV).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PiauiLocators.BOTAO_GERAR)
            )
            return True

        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def baixar_relatorio(self):
        try:
            self.driver.execute_script("document.body.style.zoom='80%'")
            self.driver.find_element(*PiauiLocators.BOTAO_GERAR).click()
            time.sleep(2)
            return True
        except Exception as e:
            print (f"Erro: {e}")
        