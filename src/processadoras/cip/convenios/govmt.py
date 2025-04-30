from src.processadoras.cip.core.cip_date_var import variaveis_data as data
from src.processadoras.cip.core.cip_checkbox import CheckBoxes as check
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from src.processadoras.cip.core.coord import CipCoord as CC
from dotenv import load_dotenv
import time
import os
import pyautogui as pg

load_dotenv()
class CipLocators:
    ABA_LOGIN = (By.XPATH, '//*[@id="guias"]/div[2]/span')
    CAMPO_USUARIO = (By.XPATH, '//*[@id="username"]')
    CAMPO_SENHA = (By.XPATH, '//*[@id="password"]')
    CAMPO_CAPTCHA = (By.ID, "captcha")
    BOTAO_LOGIN = (By.XPATH, '//*[@id="idc"]')
    SELEC_PERFIL = (By.CLASS_NAME, "btExpandir")
    OPCAO_PERFIL = (By.XPATH, "/html/body/div[1]/div/form/div[2]/div/div[4]/div[2]/fieldset/div/div[2]/fieldset/span/label/input")
    BOTAO_CONTINUAR = (By.NAME, "acessar")
    MENU_PRINCIPAL = (By.CLASS_NAME, "expandir1")
    MENU_RELATORIOS = (By.CLASS_NAME,"nivel2")
    OPCAO_VISAO_REL = (By.CLASS_NAME, "w675")
    OPCAO_VISAO_AVERB = (By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[4]/div/div[4]/div[1]/select/option[2]")
    OPCAO_TIPO_REL = (By.CLASS_NAME, "w675")
    OPCAO_TIPO_015 = (By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[4]/div/div[4]/div[2]/select/option[2]")
    DATA_INICIO = (By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[4]/div/div[5]/div[2]/div[3]/div[1]/input")
    DATA_FIM = (By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[4]/div/div[5]/div[2]/div[3]/div[3]/input")
    BOTAO_SELEC_ALLCONV = (By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[4]/div/div[5]/div[2]/div[6]/div/div[2]/span/div[2]/div/button[3]")
    BOTAO_SELEC_ALLESPE = (By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div[4]/div/div[5]/div[2]/div[9]/div/div[2]/span/div[2]/div/button[3]")
    BOTAO_GERAR_REL = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/div/div[7]/input[2]")
    BOTAO_TROCA_PERFIL = (By.XPATH, "/html/body/div/div/div[1]/div/div[3]/a")
    BOTAO_GOVSP = (By.XPATH, "/html/body/div/div/form/div[2]/div/div[5]/div[2]/fieldset/div/div[1]/span[2]/input")
    RADIO_GOVSP = (By.XPATH, "/html/body/div/div/form/div[2]/div/div[5]/div[2]/fieldset/div/div[2]/fieldset/span/label/input")

class ConvenioGovMT:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("CIP_GOVSP_URL")
        self.user = os.getenv("CIP_USER")
        self.password = os.getenv("CIP_PASS")
        
        if not all([self.url, self.user, self.password]):
            raise ValueError("Variáveis de ambiente faltando!")
        
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(CipLocators.ABA_LOGIN))
            self.driver.find_element(*CipLocators.ABA_LOGIN).click()
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(CipLocators.CAMPO_USUARIO))
            
            self.driver.find_element(*CipLocators.CAMPO_USUARIO).send_keys(self.user)
            self.driver.find_element(*CipLocators.CAMPO_SENHA).send_keys(self.password)
            CipCaptchaResolver = input("Resolva o captcha e pressione Enter: ")
            self.driver.find_element(*CipLocators.CAMPO_CAPTCHA).send_keys(CipCaptchaResolver)
            self.driver.find_element(*CipLocators.BOTAO_LOGIN).send_keys(Keys.RETURN)
            time.sleep(2)
            return True
        
        except Exception as e:
            print(f"{e}")
            return False
    
    def selec_perfil(self):
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(CipLocators.SELEC_PERFIL))
            self.driver.find_element(*CipLocators.SELEC_PERFIL).click()
            
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(CipLocators.OPCAO_PERFIL))
            self.driver.find_element(*CipLocators.OPCAO_PERFIL).click()
            time.sleep(1)
            
            self.driver.find_element(*CipLocators.BOTAO_CONTINUAR).click()
            time.sleep(1)
            return True
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def navegar_menu(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(CipLocators.MENU_PRINCIPAL)
                )
            self.driver.find_element(*CipLocators.MENU_PRINCIPAL).click()
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(CipLocators.MENU_RELATORIOS)
                )
            self.driver.find_element(*CipLocators.MENU_RELATORIOS).click()
            return True
        
        except Exception as e:
            print(f"{e}")
            return False
        
    def Tipos_Relatorio(self):
        try:    
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(CipLocators.OPCAO_VISAO_REL))
            self.driver.find_element(*CipLocators.OPCAO_VISAO_REL).click()
            self.driver.find_element(*CipLocators.OPCAO_VISAO_AVERB).click()
            time.sleep(1)
            WebDriverWait (self.driver, 15).until(
                EC.element_to_be_clickable(CipLocators.OPCAO_TIPO_REL))
            self.driver.find_element(*CipLocators.OPCAO_TIPO_REL).click()
            self.driver.find_element(*CipLocators.OPCAO_TIPO_015).click()
            time.sleep(1)
            return True
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def Opcoes_Relatorios(self):
        try:
            WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(CipLocators.DATA_INICIO)
            )
            self.driver.find_element(*CipLocators.DATA_INICIO).send_keys(data.DATA_OPERACOES)
            self.driver.find_element(*CipLocators.DATA_FIM).send_keys(data.DATA_FINAL)
            self.driver.find_element(*CipLocators.BOTAO_SELEC_ALLCONV).click()
            self.driver.find_element(*CipLocators.BOTAO_SELEC_ALLESPE).click()
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            
            #Checkbox
            self.driver.find_element(*check.MATRICULA).send_keys(Keys.SPACE)
            self.driver.find_element(*check.CPF).send_keys(Keys.SPACE)
            self.driver.find_element(*check.NOME).send_keys(Keys.SPACE)
            self.driver.find_element(*check.NOME_REDUZ_ORG).send_keys(Keys.SPACE)
            self.driver.find_element(*check.DESCRICAO).send_keys(Keys.SPACE)
            self.driver.find_element(*check.AVERB_NUM).send_keys(Keys.SPACE)
            self.driver.find_element(*check.CONTRACT_NUM).send_keys(Keys.SPACE)
            self.driver.find_element(*check.AVERB_SIT).send_keys(Keys.SPACE)
            self.driver.find_element(*check.QUANT_PARCELAS).send_keys(Keys.SPACE)
            self.driver.find_element(*check.VALOR_PRCL).send_keys(Keys.SPACE)
            self.driver.find_element(*check.VALOR_LIB).send_keys(Keys.SPACE)
            self.driver.find_element(*check.LAST_PRCL).send_keys(Keys.SPACE)
            self.driver.find_element(*check.CONTRACT_INICIO).send_keys(Keys.SPACE)
            self.driver.find_element(*check.DATA_INCLUSAO_AVERB).send_keys(Keys.SPACE)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            
            self.driver.find_element(*CipLocators.BOTAO_GERAR_REL).send_keys(Keys.SPACE)
            time.sleep(5)
            return True
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
        
    def download_arquivo(self):
        try:
            try:
                time.sleep(1)
                janela_relatorio = pg.locateOnScreen(rf".\resources\Sem_Resultados_Parametro.png", confidence=0.7)
                if janela_relatorio:
                    print("Não foi encontrado nenhum relatório com esses parâmetros.")
                else:
                    pg.moveTo(CC.ExportarBotão, duration=1)
                    pg.moveTo(CC.TipoCSV, duration=1)
                    pg.click()
                    time.sleep(4)
                    pg.hotkey('ctrl', 'w')
                    time.sleep(1)
            except pg.ImageNotFoundException:
                print("Imagem não encontrada")
            return True
        
        except Exception as e:
            print(f"Erro: {e}")
            return False
            

