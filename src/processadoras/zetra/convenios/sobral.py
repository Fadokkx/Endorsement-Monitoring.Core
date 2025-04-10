from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()

class ConvenioSobral:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = os.getenv("ZETRA_SOBRAL_URL")
        self.user = os.getenv("ZETRA_USER")
        self.password = os.getenv("ZETRA_PASS")

        # Verificação DENTRO do __init__
        if not all([self.url, self.user, self.password]):
            raise ValueError(
                "Variáveis de ambiente faltando! Verifique se no .env tem:\n"
                "ZETRA_SOBRAL_URL (URL do site)\n"
                "ZETRA_USER (seu usuário)\n"
                "ZETRA_PASS (sua senha)"
            )
    
    def login(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.NAME, "username"))
            ).send_keys(self.user)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="no-back"]/div/div[1]/form/div[2]/div[2]/button')))
            self.driver.find_element(By.XPATH, '//*[@id="no-back"]/div/div[1]/form/div[2]/div[2]/button').click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "senha"))
            ).send_keys(self.password)
            ZetraCaptchaResolver = input("Resolva o captcha e pressione Enter para continuar...: ")
            ZetraCaptcha = self.driver.find_element(By.ID, "captcha")
            ZetraCaptcha.send_keys(ZetraCaptchaResolver)
            self.driver.find_element(By.XPATH, '//*[@id="btnOK"]').click()
            time.sleep(10)
        except Exception as e:
            print(f"Erro no login: {e}")
            return False