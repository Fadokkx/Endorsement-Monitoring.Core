from src.core.browser import iniciar_navegador
from src.controllers.zetra_controller import ZetraController
from src.controllers.cip_controller import CipController
#from src.controllers.consigfacil_controller import ConsigFacilController
from dotenv import load_dotenv

def main():
    load_dotenv()
    driver = iniciar_navegador()

    try:
        zetra = ZetraController(driver)
        
        # Seletor de convênios (pode vir de um arquivo de configuração)
        convenios = ['uberlandia']  #[None] #para todos
        
        resultados = zetra.executar_todos_convenios(convenios)
        
        # Exibe relatório bonito
        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}")

    try:
        cip = CipController(driver)
        
        #Seletor de convênios
        convenios = ['govmt', 'govsp', 'govsefazsp']  # Ou None para todos
        
        resultados = cip.executar_todos_convenios(convenios)
        
        # Exibe relatório bonito
        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}")
    
        """
    try:
        consigfacil = ConsigFacilController(driver)
        #Seletor de convênios
        convenios = ['govmt', 'govsp', 'govsefazsp']  # Ou None para todos
        
        resultados = consigfacil.executar_todos_convenios(convenios)
        
        # Exibe relatório bonito
        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}")
        """

    finally:
        driver.quit()
    
if __name__ == "__main__":
        main()
        """
    try:
        ConsigFacil = ConsigFacilController(driver)
    except Exception as e:
        print(f"Erro {e}")
        """

