from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
import time

class BalnearioLocators:
    CAMPO_USER = (By.XPATH, '//*[@id="login-username"]')
    BOTAO_CONTINUAR = (By.XPATH, '//*[@id="btn-continuar"]/span[1]/div')
    CAMPO_SENHA = (By.XPATH, '//*[@id="login-password"]')
    BOTAO_ENTRAR = (By.XPATH, '//*[@id="btn-entrar"]/span[1]/div')
    CAMPO_BUSCA_CONVENIO = (By.XPATH, '//*[@id="context-search"]')
    OPCAO_CONVENIO = (By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div/div/div/div/div/span')
    ABA_RELATORIOS = (By.XPATH, '//*[@id="menu-item-relatorios"]/div[2]/span')
    OPCAO_CONSIGNACOES = (By.XPATH, '//*[@id="menu-item-consignacoes"]/div/span')
    OPCAO_CONSIGNACAO_MENSAL = (By.XPATH, '//*[@id="menu-item-consignacao-mensal"]/div/span')
    OPCAO_XLS = (By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/form/div/div[4]/button[2]/span[1]/div")
    BOTAO_CONFIRMA_DOWNLOAD = (By.XPATH, '//*[@id="modal-btn-Confirmar"]/span[1]/div')
    BOTAO_FECHA_SUCESSO = (By.XPATH, '//*[@id="snackbar-btn-fechar"]/span[1]')
    BOTAO_PERFIL = (By.XPATH, '//*[@id="button-profile"]/span[1]/div')
    BOTAO_TROCA_PERFIL = (By.XPATH, '//*[@id="csg-appbar"]/div/div[2]/div/div/ul/li[1]/p')

class ConvenioBalneario:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("CONSIGNET_BALNEARIO_URL")
        self.user = os.getenv("CONSIGNET_USER")
        self.password = os.getenv("CONSIGNET_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BalnearioLocators.CAMPO_USER)).send_keys(self.user)
            self.driver.find_element(*BalnearioLocators.BOTAO_CONTINUAR).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BalnearioLocators.CAMPO_SENHA)).send_keys(self.password)
            self.driver.find_element(*BalnearioLocators.BOTAO_ENTRAR).click()
            time.sleep(0.5)
            return True
        except Exception as e:
            print (f"Erro {e}")
            return False
            
    def selec_convenios(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BalnearioLocators.CAMPO_BUSCA_CONVENIO)).send_keys("BALNEÁRIO CAMBORIÚ / MEUCASHCARD SAQUE")
            self.driver.find_element(*BalnearioLocators.OPCAO_CONVENIO).click()
            return True
        except Exception as e: 
            print(f"Erro {e}")
            return False
        
    def navega_menu(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BalnearioLocators.ABA_RELATORIOS)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BalnearioLocators.OPCAO_CONSIGNACOES)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BalnearioLocators.OPCAO_CONSIGNACAO_MENSAL)).click()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def baixa_relatorio(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BalnearioLocators.OPCAO_XLS)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(BalnearioLocators.BOTAO_CONFIRMA_DOWNLOAD)).click()
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(BalnearioLocators.BOTAO_FECHA_SUCESSO)).click()
            except:
                print("Sem caixa de sucesso")
            return True
        except Exception as e:
            print (f"Erro: {e}")
            return False
        
