from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
import time

class NavegantesLocators:
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

class ConvenioNavegantes:
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("CONSIGNET_URL")
        self.user = os.getenv("CONSIGNET_USER")
        self.password = os.getenv("CONSIGNET_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
    
    def login(self):
            try:
                try:
                    WebDriverWait(self.driver, 2).until(
                            EC.element_to_be_clickable(NavegantesLocators.BOTAO_PERFIL)).click()
                    WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable(NavegantesLocators.BOTAO_TROCA_PERFIL)).click()
                    time.sleep(1)
                except:
                    self.driver.get(self.url)
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(NavegantesLocators.CAMPO_USER)).send_keys(self.user)
                    self.driver.find_element(*NavegantesLocators.BOTAO_CONTINUAR).click()
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(NavegantesLocators.CAMPO_SENHA)).send_keys(self.password)
                    self.driver.find_element(*NavegantesLocators.BOTAO_ENTRAR).click()
                    time.sleep(0.5)
                return True
            except Exception as e:
                print (f"Erro {e}")
                return False
            
    def selec_convenios(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(NavegantesLocators.CAMPO_BUSCA_CONVENIO)).send_keys("PREF. NAVEGANTES - SC / MEUCASHCARD BENEFICIOS (SAQUE E COMPRA)")
            self.driver.find_element(*NavegantesLocators.OPCAO_CONVENIO).click()
            return True
        except Exception as e: 
            print(f"Erro {e}")
            return False
        
    def navega_menu(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(NavegantesLocators.ABA_RELATORIOS)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(NavegantesLocators.OPCAO_CONSIGNACOES)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(NavegantesLocators.OPCAO_CONSIGNACAO_MENSAL)).click()
            return True
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
    
    def baixa_relatorio(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(NavegantesLocators.OPCAO_XLS)).click()
            
            try:  
                WebDriverWait(self.driver, 1.5).until(
                    EC.element_to_be_clickable(NavegantesLocators.BOTAO_CONFIRMA_DOWNLOAD)).click()
            except:
                print("Sem necessidade de confirmar download")
  
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(NavegantesLocators.BOTAO_FECHA_SUCESSO)).click()
            except:
                print("Sem caixa de sucesso")
            return True
        
        except Exception as e:
            print (f"Erro: {e}")
            return False
        
