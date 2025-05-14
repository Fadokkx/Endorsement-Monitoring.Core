from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from src.processadoras.consiglog.core.consiglog_date_var import variaveis_data as data
from dotenv import load_dotenv
import time
import os

load_dotenv()

class DuqueLocators:
    CAMPO_USER = (By.XPATH, '//*[@id="txtLogin"]')
    BOTAO_CONTINUAR = (By.XPATH, '//*[@id="Entrar"]')
    CAMPO_SENHA = (By.XPATH, '//*[@id="txtSenha"]')
    BOTAO_ENTRAR = (By.XPATH, '//*[@id="Entrar"]')
    BOTAO_LOGOUT_SESSAO_INATIV = (By.XPATH, '//*[@id="ucAjaxModalPopupConfirmacao1_btnConfirmarPopup"]')
    CONVENIO_PREFDUQUE = (By.XPATH, "/html/body/form/div[5]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[3]/input")
    CONFIRMACAO_LEITURA = (By.XPATH, '//*[@id="body_ucModalPopupAvisos1_btnConfirmarPopup"]')
    FECHA_POPUP_CONF_LEITURA = (By.XPATH, '//*[@id="body_ucModalPopupAvisos1_ucAjaxModalDoModal1_btnConfirmarPopup"]')
    COOKIES_NOTIF = (By.XPATH, '//*[@id="entendi-cookies"]')
    ABA_RELATORIO = (By.XPATH, '//*[@id="Div1"]/ul/li[6]')
    OPCOES_CONSIGNACOES = (By.XPATH, '//*[@id="subMenuItem"]')
    OPCAO_CONSIGNACAO = (By.XPATH, '//*[@id="RepeaterSub"]/ul/li/a')
    BOTAO_TIPO_REL = (By.XPATH, '//*[@id="body_ddlTiposRelatorio"]')
    TIPO_ANDEFERIDO = (By.XPATH, '//*[@id="body_ddlTiposRelatorio"]/option[12]') 
    BOTAO_CONV_SELEC = (By.XPATH, "/html/body/form/div[8]/div/div/fieldset/div[3]/div/button")
    CHECK_ALL_CONV = (By.XPATH, '//*[@id="body_divConvenio"]/div/div/ul/li[1]/label/input')
    BOTAO_ORGAOS_SELEC = (By.XPATH, "/html/body/form/div[8]/div/div/fieldset/div[4]/div/button")
    CHECK_ALL_ORG = (By.XPATH, '//*[@id="conteudo"]/div/div/fieldset/div[4]/div/div/ul/li[1]/label/input')
    CAMPO_PER_INI = (By.XPATH, '//*[@id="body_dataIniTextBox"]')
    CAMPO_PER_FIM = (By.XPATH, '//*[@id="body_dataFinTextBox"]')
    BOTAO_SERVICO = (By.XPATH, "/html/body/form/div[8]/div/div/fieldset/div[6]/div/button")
    CHECK_ALL_SERVICES = (By.XPATH, '//*[@id="conteudo"]/div/div/fieldset/div[6]/div/div/ul/li[1]/label/input')
    BOTAO_OPCOES_REL = (By.XPATH, '//*[@id="body_ddlTipoVisualizacao"]')
    OPCAO_XLSX = (By.XPATH, '//*[@id="body_ddlTipoVisualizacao"]/option[3]')
    BOTAO_GERAR_REL = (By.XPATH, '//*[@id="body_pesquisarButton"]')
    
class ConvenioDuqueDeCaxias:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("CONSIGLOG_DUQUE_DE_CAXIAS_URL")
        self.user = os.getenv("CONSIGLOG_USER")
        self.password = os.getenv("CONSIGLOG_PASS")

        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DuqueLocators.CAMPO_USER)).send_keys(self.user)
            self.driver.find_element(*DuqueLocators.BOTAO_CONTINUAR).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DuqueLocators.CAMPO_SENHA)).send_keys(self.password)
            self.driver.find_element(*DuqueLocators.BOTAO_ENTRAR).click()
            
            try:
                WebDriverWait(self.driver, 1.5).until(
                    EC.element_to_be_clickable(DuqueLocators.BOTAO_LOGOUT_SESSAO_INATIV)).click()
            except:
                print("Sem necessidade de logout de outras sessões")
                
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def selec_convenio(self):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DuqueLocators.CONVENIO_PREFDUQUE)).click()
            time.sleep(0.1)
            return True
        except Exception as e:
            print(f"Erro {e}")
            return False
            
    def navega_menu(self):
        try:
            try:
                while True:
                    WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable(DuqueLocators.CONFIRMACAO_LEITURA)).click()
                    WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable(DuqueLocators.FECHA_POPUP_CONF_LEITURA)).click()
                    time.sleep(0.5)
            except:
                print("Sem necessidade de confirmação")
            
            try:
                WebDriverWait(self.driver, 4).until(
                    EC.element_to_be_clickable(DuqueLocators.COOKIES_NOTIF)).click()        
            except:
                print("Sem necessidade de confirmação de cookies")
                
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(DuqueLocators.ABA_RELATORIO)).click()
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(DuqueLocators.OPCOES_CONSIGNACOES)).click()
            WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(DuqueLocators.OPCAO_CONSIGNACAO)).click()
            return True
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def opcoes_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DuqueLocators.BOTAO_TIPO_REL)).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(DuqueLocators.TIPO_ANDEFERIDO)).click()
            time.sleep(0.5)
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(DuqueLocators.BOTAO_CONV_SELEC)).click()
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(DuqueLocators.CHECK_ALL_CONV)).click()
            time.sleep(0.5)
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(DuqueLocators.BOTAO_ORGAOS_SELEC)).click()
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(DuqueLocators.CHECK_ALL_ORG)).click()
            time.sleep(0.5)
            try:
                self.driver.find_element(*DuqueLocators.BOTAO_ORGAOS_SELEC).click()
            except Exception as e:
                print(f"Erro: {e}")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DuqueLocators.CAMPO_PER_INI)).send_keys(data.DATA_INICIO)
            time.sleep(0.1)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(DuqueLocators.CAMPO_PER_FIM)).send_keys(data.DATA_FINAL)
            time.sleep(0.5)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DuqueLocators.BOTAO_SERVICO)).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(DuqueLocators.CHECK_ALL_SERVICES)).click()
            time.sleep(0.5)
            try:
                self.driver.find_element(*DuqueLocators.BOTAO_SERVICO).click()
            except Exception as e:
                print(f"Erro: {e}")                
            return True
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def download_relatorio(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DuqueLocators.BOTAO_OPCOES_REL)).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(DuqueLocators.OPCAO_XLSX)).click()
            
            try:
                self.driver.find_element(*DuqueLocators.BOTAO_OPCOES_REL).click()
            except Exception as e:
                print(f"Erro: {e}")
                
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(DuqueLocators.BOTAO_GERAR_REL)).click()
            time.sleep(1.5)
            return True
        
        except:
            return False