from src.core.browser import iniciar_navegador
from src.controllers.zetra_controller import ZetraController
from src.controllers.cip_controller import CipController
from src.controllers.consigfacil_controller import ConsigFacilController
from src.controllers.neoconsig_controller import NeoConsigController
from src.controllers.asban_controller import AsbanController
from dotenv import load_dotenv

def main():
    load_dotenv()
    driver = iniciar_navegador()

    try:
        zetra = ZetraController(driver)
        
        convenios = [None] #[None] Ou ['nova_lima','curitiba','sobral','embu', 'hortolandia', 'hospital_do_servidor_publico', 'igeprev', 'sbc', 'serra','uberlandia']  #[None] #para todos
        
        resultados = zetra.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}")

    try:
        cip = CipController(driver)
        
        convenios = [None] #[None] OU ['govmt', 'govsp', 'govsefazsp']
        
        resultados = cip.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}")
       
    try:
        consigfacil = ConsigFacilController(driver)

        convenios = [None] #[None] #OU #['campina_grande', 'cuiaba', 'ipatinga', 'joao_pessoa', 'juazeiro', 'maranhao', 'pernambuco', 'piaui', 'porto_velho', 'recife', 'teresina']        
        
        resultados = consigfacil.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}")
        
    
    try:
        NeoConsig = NeoConsigController(driver)

        convenios = [None] #[None] OU ['goias', 'rio', 'sorocaba', 'alagoas']
        
        resultados = NeoConsig.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    except Exception as e:
        print(f"Erro {e}")    
    
    
    try:
        Asban = AsbanController(driver)

        convenios = ['cachoeirinha'] #[None] OU ['cachoeirinha']
        
        resultados = Asban.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    except Exception as e:
        print(f"Erro {e}")    
    
    finally:
        driver.quit()
        
if __name__ == "__main__":
        main()