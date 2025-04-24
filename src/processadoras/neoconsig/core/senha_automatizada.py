from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TecladoVirtualNeoConsig:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
    
    def enter_password(self, password, timeout=None):
        timeout = timeout or self.timeout
        password_str = str(password).strip()
        
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.bt_senha.btn-success')))
            
            for digit in password_str:
                self._click_digit(digit, timeout)
            
            print("Senha inserida com sucesso!")
            return True
            
        except Exception as e:
            print(f"ERRO ao inserir senha: {str(e)}")
            self._take_screenshot(f"erro_senha_{password_str}")
            return False
    
    def _click_digit(self, digit, timeout):
        botoes = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.bt_senha.btn-success')))
        
        for botao in botoes:
            # Normaliza o texto do botão (case-insensitive e remove espaços)
            options = [opt.strip() for opt in botao.text.upper().split('OU')]
            if digit in options:
                botao.click()
                time.sleep(0.3)
                
                #Retirar apenas para Checagem de clicks 
                #print(f"Clicado no dígito: {digit} (Opções: {botao.text})")
                
                return
        
        # Se não encontrou o dígito, gera mensagem de erro detalhada
        available_digits = []
        for b in botoes:
            opts = [opt.strip() for opt in b.text.upper().split('OU')]
            available_digits.extend(opts)
        
        raise ValueError(
            f"Dígito '{digit}' não encontrado. "
            f"Dígitos disponíveis: {sorted(set(available_digits))}\n"
            f"Botões atuais: {[b.text for b in botoes]}"
        )