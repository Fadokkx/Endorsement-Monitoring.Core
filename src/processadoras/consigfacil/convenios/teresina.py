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

class TeresinaLocators:
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
class ConvenioTeresina:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("CONSIGFACIL_TERESINA_URL")
        self.user = os.getenv("CONSIGFACIL_USER")
        self.password = os.getenv("CONSIGFACIL_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(TeresinaLocators.CAMPO_LOGIN)
            )
            self.driver.find_element(*TeresinaLocators.CAMPO_LOGIN).send_keys(self.user)
            self.driver.find_element(*TeresinaLocators.CAMPO_SENHA).send_keys(self.password)
            CF_CAPTCHA_RESOLVER = input ("Digite o Captcha: ")
            self.driver.find_element(*TeresinaLocators.CAMPO_CAPTCHA).send_keys(CF_CAPTCHA_RESOLVER)
            self.driver.find_element(*TeresinaLocators.CAMPO_CAPTCHA).send_keys(Keys.ENTER)
            time.sleep(1)
            return True
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def confirmacao_leitura_novidades(self):
        try:
            try:
                if not self.driver.find_element(*TeresinaLocators.BOTAO_NOVIDADES).click():
                    raise Exception("Sem novidades")
            except Exception as e:
                print("Sem novidades.")
            
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(TeresinaLocators.BOTAO_CONFIRMA_LEITURA)
                )
                if not self.driver.find_element(*TeresinaLocators.BOTAO_CONFIRMA_LEITURA).click():
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
                EC.element_to_be_clickable(TeresinaLocators.ABA_RELATORIO)
            )
            self.driver.find_element(*TeresinaLocators.ABA_RELATORIO).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(TeresinaLocators.SELEC_RELATORIO)
            )
            self.driver.find_element(*TeresinaLocators.SELEC_RELATORIO).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
        
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(TeresinaLocators.DATA_INICIO)
            )
            self.driver.find_element(*TeresinaLocators.DATA_INICIO).send_keys(data.DATA_OPERACOES)
            self.driver.find_element(*TeresinaLocators.DATA_FIM).send_keys(data.DATA_FINAL)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.find_element(*TeresinaLocators.OPCAO_REL).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeresinaLocators.TIPO_CSV)
            )
            self.driver.find_element(*TeresinaLocators.TIPO_CSV).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(TeresinaLocators.BOTAO_GERAR)
            )
            return True

        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def baixar_relatorio(self):
        try:
            self.driver.execute_script("document.body.style.zoom='80%'")
            self.driver.find_element(*TeresinaLocators.BOTAO_GERAR).click()
            time.sleep(2)
            return True
        except Exception as e:
            print (f"Erro: {e}")
        