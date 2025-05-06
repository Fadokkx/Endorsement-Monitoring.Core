from src.processadoras.zetra.core.zetra_date_var import variaveis_data as data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv()
class EmbuLocators:
    MENU_PRINCIPAL = (By.XPATH, '//*[@id="container"]/ul/li[3]/a')
    MENU_RELATORIOS = (By.XPATH, '//*[@id="menuRelatorio"]/ul/li[1]/a')
    CAMPO_USUARIO = (By.NAME, "username")
    BOTAO_CONTINUAR = (By.XPATH, '//*[@id="no-back"]/div/div[1]/form/div[2]/div/button')
    CAMPO_SENHA = (By.NAME, "senha")
    CAMPO_CAPTCHA = (By.ID, "captcha")
    BOTAO_LOGIN = (By.XPATH, '//*[@id="btnOK"]')
    DATA_INICIO = (By.XPATH, '//*[@id="periodoIni"]')
    DATA_FIM = (By.XPATH, '//*[@id="periodoFim"]')
    CHECKBOX_DEFERIDA = (By.XPATH, '//*[@id="SAD_CODIGO7"]')
    BOTAO_GERAR = (By.XPATH, '//*[@id="btnEnvia"]')
    OPCOES_DOWNLOAD = (By.XPATH, '//*[@id="userMenu"]/div/span')
    BOTAO_DOWNLOAD = (By.XPATH, '//*[@id="dataTables"]/tbody/tr[1]/td[4]/div/div/div/a[1]')
    SELEC_OPCOES =(By.XPATH, '//*[@id="formato"]')
    OPCAO_CSV = (By.XPATH, '//*[@id="formato"]/option[4]')
    SENHA_AUTORIZER = (By.XPATH, '//*[@id="senha2aAutorizacao"]')
    BOTAO_VOLTA_TROCA_SENHA = (By.XPATH, '//*[@id="no-back"]/div/div[1]/div[3]/button')
    
class ConvenioEmbu:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("ZETRA_EMBU_URL")
        self.user = os.getenv("ZETRA_USER")
        self.password = os.getenv("ZETRA_PASS")
        self.second_password = os.getenv("ZETRA_SECOND_PASS")
        
        if not all([self.url, self.user, self.password, self.second_password]):
            raise ValueError("Variáveis de ambiente faltando!")
        
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(EmbuLocators.CAMPO_USUARIO)
            ).send_keys(self.user)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(EmbuLocators.BOTAO_CONTINUAR)
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(EmbuLocators.CAMPO_SENHA)
            ).send_keys(self.second_password)
            
            ZetraCaptchaResolver = input("Resolva o captcha e pressione Enter...: ")
            self.driver.find_element(*EmbuLocators.CAMPO_CAPTCHA).send_keys(ZetraCaptchaResolver)
            self.driver.find_element(*EmbuLocators.BOTAO_LOGIN).send_keys(Keys.RETURN)
            return True
            
        except Exception as e:
            print(f"Erro no login: {e}")
            return False
        
    def troca_senha(self):
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH,'//*[@id="senha"]').click()
            self.driver.execute_script("document.body.style.zoom='80%'")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="senha"]')))
            self.driver.find_element(By.XPATH,'//*[@id="senha"]').send_keys(self.second_password)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID,"senhaNovaConfirmacao")))
            self.driver.find_element(By.XPATH, '/html/body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.find_element(By.ID,"senhaNova").send_keys(self.password)           
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID,"senhaNovaConfirmacao")))
            self.driver.find_element(By.ID,"senhaNovaConfirmacao").send_keys(self.password)
            self.driver.find_element(By.XPATH,'//*[@id="no-back"]/div[3]/div/div[4]/a[2]').click()
            self.driver.find_element(*EmbuLocators.BOTAO_VOLTA_TROCA_SENHA).click()
        except:
            print(f"Sem necessidade de troca de senha")
            return True
    
    def confirmacao_leitura(self):
        time.sleep(1)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="no-back"]/div[3]/div/form/div[1]/div[2]/div[2]/div/div/fieldset/div/label[1]').click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="no-back"]/div[3]/div/form/div[2]/a'))).click()
            print("Confirmação de leitura realizada com sucesso.")
        except Exception as e:
            print(f"Sem necessidade de confirmação de leitura")
            return True

    def navegar_menu(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(EmbuLocators.MENU_PRINCIPAL)
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(EmbuLocators.MENU_RELATORIOS)
            ).click()
            return True
        
        except Exception as e:
            print(f"Erro na navegação: {e}")
            return False
        
    def opcoes_relatorios(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(EmbuLocators.DATA_INICIO)
            ).send_keys(data.DATA_OPERACOES)
            self.driver.execute_script("document.body.style.zoom='60%'")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(EmbuLocators.DATA_FIM)
            ).send_keys(data.DATA_FINAL)
            time.sleep(1)
            
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(EmbuLocators.CHECKBOX_DEFERIDA)).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(EmbuLocators.SELEC_OPCOES))
            self.driver.find_element(*EmbuLocators.SELEC_OPCOES).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(EmbuLocators.OPCAO_CSV)
            ).click()
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(EmbuLocators.BOTAO_GERAR))
            self.driver.find_element(*EmbuLocators.BOTAO_GERAR).click()    
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(EmbuLocators.SENHA_AUTORIZER))
            time.sleep(1)  
            return True
        except Exception as e:
            print(f"Erro nas opções de relatório: {e}")
            return False     
        
    def autorizacao_gerador(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(EmbuLocators.SENHA_AUTORIZER)).send_keys(self.second_password)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/button[2]").click()
            time.sleep(1)
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(EmbuLocators.DATA_INICIO))
            return True
        except Exception as e:
            print(f"Erro na autorização: {e}")
            return False  
            
    def download_arquivo(self):
        try:
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            self.driver.execute_script("document.body.style.zoom='33%'")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(EmbuLocators.OPCOES_DOWNLOAD)).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(EmbuLocators.BOTAO_DOWNLOAD)).click()
            time.sleep(1)
            return True
        
        except Exception as e:
            print(f"Erro no download: {e}")
            return False