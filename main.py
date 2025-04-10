from src.processadoras.zetra.convenios.sobral import ConvenioSobral
from src.core.browser import iniciar_navegador
from dotenv import load_dotenv

def main():
    load_dotenv()
    driver = iniciar_navegador()
    
    try:
        convenio = ConvenioSobral(driver)
        convenio.login()
        print("Login realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao realizar login: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()