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
class PrefRioLocators:
    CAMPO_USUARIO = (By.NAME, "username")
    BOTAO_CONTINUAR = (By.XPATH, '//*[@id="no-back"]/div/div[1]/form/div[2]/div[2]/button')
    CAMPO_SENHA = (By.NAME, "senha")
    CAMPO_CAPTCHA = (By.ID, "captcha")
    BOTAO_LOGIN = (By.XPATH, '//*[@id="btnOK"]')
    MENU_PRINCIPAL = (By.XPATH, '//*[@id="container"]/ul/li[3]/a')
    MENU_RELATORIOS = (By.XPATH, '//*[@id="menuRelatorio"]/ul/li[1]/a')
    DATA_INICIO = (By.XPATH, '//*[@id="periodoIni"]')
    DATA_FIM = (By.XPATH, '//*[@id="periodoFim"]')
    CHECKBOX_DEFERIDA = (By.XPATH, '//*[@id="SAD_CODIGO5"]')
    BOTAO_GERAR = (By.XPATH, '//*[@id="btnEnvia"]')
    BOTAO_AUTORIZA_GERADOR = (By.XPATH, "/html/body/div[2]/div[3]/div/button[2]")
    OPCOES_DOWNLOAD = (By.XPATH, '//*[@id="userMenu"]/div/span')
    BOTAO_DOWNLOAD = (By.XPATH, '//*[@id="dataTables"]/tbody/tr[1]/td[4]/div/div/div/a[1]')
    SELEC_OPCOES =(By.XPATH, '//*[@id="formato"]')
    OPCAO_CSV = (By.XPATH, '//*[@id="formato"]/option[4]')
    SENHA_AUTORIZER = (By.XPATH, '//*[@id="senha2aAutorizacao"]')
    CAMPO_SENHA_TROCA = (By.XPATH,'//*[@id="senha"]')
    CAMPO_NOVA_SENHA_CONFIRMA = (By.ID,"senhaNovaConfirmacao")    
    CAMPO_NOVA_SENHA_TROCA = (By.ID,"senhaNova")
    BOTAO_CONFIRMA_TROCA = (By.XPATH,'//*[@id="no-back"]/div[3]/div/div[4]/a[2]')
    BOTAO_VOLTA_TROCA_SENHA = (By.XPATH, '//*[@id="no-back"]/div/div[1]/div[3]/button') 
    BOTAO_CONFIRMA_LEITURA = (By.XPATH, '//*[@id="no-back"]/div[3]/div/form/div[2]/a')
    RADIO_CONFIRMA_LEITURA = (By.XPATH, '//*[@id="no-back"]/div[3]/div/form/div[1]/div[2]/div[2]/div[1]/div/fieldset/div/label[1]')
    RADIO_CONFIRMA_SEG_LEITURA =(By.XPATH, '//*[@id="no-back"]/div[3]/div/form/div[1]/div[2]/div[2]/div[2]/div/fieldset/div/label[1]')    
    BODY = (By.XPATH, "/html/body")
    
class ConvenioPrefRio:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("ZETRA_RIO_DE_JANEIRO_PREF")
        self.user = os.getenv("ZETRA_USER")
        self.second_user = os.getenv("ZETRA_SECOND_USER")
        self.password = os.getenv("ZETRA_PASS")
        self.second_password = os.getenv("ZETRA_SECOND_PASS")
        
        if not all([self.url, self.user, self.second_user, self.password, self.second_password]):
            raise ValueError("Variáveis de ambiente faltando!")
        
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(PrefRioLocators.CAMPO_USUARIO)).send_keys(self.second_user)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PrefRioLocators.BOTAO_CONTINUAR)).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PrefRioLocators.CAMPO_SENHA)).send_keys(self.password)
            ZetraCaptchaResolver = input("Resolva o captcha e pressione Enter...: ")
            self.driver.find_element(*PrefRioLocators.CAMPO_CAPTCHA).send_keys(ZetraCaptchaResolver)
            self.driver.find_element(*PrefRioLocators.BOTAO_LOGIN).send_keys(Keys.RETURN)
            time.sleep(0.1)
            try:
                WebDriverWait(self.driver, 1.5).until(
                            EC.presence_of_element_located(PrefRioLocators.MENU_PRINCIPAL))
                return True
            except Exception as e:
                print(f"Falha no login ou CAPTCHA incorreto. Tentando novamente")
            
            while True:
                try:
                    WebDriverWait(self.driver, 1.5).until(
                        EC.presence_of_element_located(PrefRioLocators.CAMPO_USUARIO)).send_keys(self.second_user)
                    WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable(PrefRioLocators.BOTAO_CONTINUAR)).click()
                    WebDriverWait(self.driver, 2).until(
                        EC.element_to_be_clickable(PrefRioLocators.CAMPO_SENHA)).send_keys(self.password)
                    ZetraCaptchaResolver = input("Resolva o captcha e pressione Enter: ")
                    WebDriverWait(self.driver, 1).until(
                        EC.presence_of_element_located(PrefRioLocators.CAMPO_CAPTCHA)).send_keys(ZetraCaptchaResolver)
                    self.driver.find_element(*PrefRioLocators.CAMPO_CAPTCHA).send_keys(Keys.ENTER)
                    WebDriverWait(self.driver, 1.5).until(
                        EC.presence_of_element_located(PrefRioLocators.MENU_PRINCIPAL))
                    return True

                except Exception as e:
                    print(f"Falha no login ou CAPTCHA incorreto. Tentando novamente")
                    time.sleep(0.7)
            
        except Exception as e:
            print(f"Erro no login: {e}")
            return False
        
    def troca_senha(self):
        time.sleep(1)
        try:
            self.driver.find_element(PrefRioLocators.CAMPO_SENHA).click()
            self.driver.execute_script("document.body.style.zoom='80%'")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PrefRioLocators.CAMPO_SENHA_TROCA))
            self.driver.find_element(*PrefRioLocators.CAMPO_SENHA_TROCA).send_keys(self.password)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located())
            self.driver.find_element(PrefRioLocators.BODY).send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(PrefRioLocators.CAMPO_NOVA_SENHA_TROCA)).send_keys(self.second_password)          
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PrefRioLocators.CAMPO_NOVA_SENHA_CONFIRMA)).send_keys(self.second_password)
            self.driver.find_element(PrefRioLocators.BOTAO_CONFIRMA_TROCA).click()
            self.driver.find_element(*PrefRioLocators.BOTAO_VOLTA_TROCA_SENHA).click()
        except:
            print(f"Sem necessidade de troca de senha")
            return True
    
    def confirmacao_leitura(self):
        time.sleep(0.5)
        try:
            self.driver.find_element(*PrefRioLocators.RADIO_CONFIRMA_LEITURA).click()
            time.sleep(0.1)
            self.driver.find_element(*PrefRioLocators.BODY).send_keys(Keys.PAGE_DOWN)
            try:
                WebDriverWait(self.driver, 1.5).until(
                    EC.element_to_be_clickable(PrefRioLocators.RADIO_CONFIRMA_SEG_LEITURA)).click()
            except:
                print("Sem segunda leitura necessária")
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(PrefRioLocators.BOTAO_CONFIRMA_LEITURA)).click()
            print("Confirmação de leitura realizada com sucesso.")
        except Exception as e:
            print(f"Sem necessidade de confirmação de leitura")
            return True

    def navegar_menu(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(PrefRioLocators.MENU_PRINCIPAL)
            ).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PrefRioLocators.MENU_RELATORIOS)
            ).click()
            return True
        
        except Exception as e:
            print(f"Erro na navegação: {e}")
            return False
        
    def opcoes_relatorios(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(PrefRioLocators.DATA_INICIO)
            ).send_keys(data.DATA_OPERACOES)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PrefRioLocators.DATA_FIM)
            ).send_keys(data.DATA_FINAL)
            time.sleep(0.1)
            self.driver.find_element(*PrefRioLocators.BODY).send_keys(Keys.PAGE_DOWN)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PrefRioLocators.CHECKBOX_DEFERIDA)).click()
            time.sleep(0.1)
            self.driver.find_element(*PrefRioLocators.BODY).send_keys(Keys.PAGE_DOWN)
            self.driver.execute_script("document.body.style.zoom='80%'")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PrefRioLocators.SELEC_OPCOES))
            self.driver.find_element(*PrefRioLocators.SELEC_OPCOES).click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PrefRioLocators.OPCAO_CSV)).click()
            time.sleep(0.1)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PrefRioLocators.BOTAO_GERAR))
            self.driver.find_element(*PrefRioLocators.BOTAO_GERAR).click()    
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PrefRioLocators.SENHA_AUTORIZER)) 
            return True
        except Exception as e:
            print(f"Erro nas opções de relatório: {e}")
            return False     
        
    def autorizacao_gerador(self):
        try: 
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(PrefRioLocators.SENHA_AUTORIZER)).send_keys(self.password)
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(PrefRioLocators.BOTAO_AUTORIZA_GERADOR)).click()
            time.sleep(1)
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(PrefRioLocators.DATA_INICIO))
            return True
        except Exception as e:
            print(f"Erro na autorização: {e}")
            return False  
            
    def download_arquivo(self):
        try:
            time.sleep(0.5)
            self.driver.find_element(*PrefRioLocators.BODY).send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
            self.driver.find_element(*PrefRioLocators.BODY).send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
            self.driver.execute_script("document.body.style.zoom='33%'")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PrefRioLocators.OPCOES_DOWNLOAD)).click()
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(PrefRioLocators.BOTAO_DOWNLOAD)).click()
            time.sleep(1)
            return True
        
        except Exception as e:
            print(f"Erro no download: {e}")
            return False