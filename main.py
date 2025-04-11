from src.core.browser import iniciar_navegador
from src.processadoras.zetra.convenios.sobral import ConvenioSobral
from dotenv import load_dotenv
def main():
    load_dotenv()
    driver = iniciar_navegador()
    
    try:
        sobral = ConvenioSobral(driver)
        
        if sobral.login():
            print("Login realizado com sucesso!")
        
            if sobral.navegar_menu():
                print("Navegação no menu concluída!")
        
                if sobral.opcoes_relatorios():
                    print("Opções de relatórios acessadas com sucesso!")
                    
                    if sobral.autorizer():
                        print("Autorização cedida com sucesso!")
                    else:
                        print(f"Falha na autorização")
                else:
                    print("Falha ao acessar opções de relatórios")
            else:
                print("Falha na navegação do menu")
        else:
            print("Falha no login")                            
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        driver.quit()
if __name__ == "__main__":
    main()