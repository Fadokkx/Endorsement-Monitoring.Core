from src.core.browser import iniciar_navegador
from src.controllers.asban_controller import AsbanController
from src.controllers.cip_controller import CipController
from src.controllers.consigfacil_controller import ConsigFacilController
from src.controllers.consiglog_controller import ConsigLogController
from src.controllers.consignet_controller import ConsigNetController
from src.controllers.consigtec_controller import ConsigTecController
from src.controllers.digitalconsig_controller import DigitalConsigController
from src.controllers.neoconsig_controller import NeoConsigController
from src.controllers.safeconsig_controller import SafeConsigController
from src.controllers.serpro_controller import SerproController
from src.controllers.siconsig_controller import SiConsigController
from src.controllers.sigconsig_controller import SigConsigController
from src.controllers.zetra_controller import ZetraController

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

        convenios = [None] #[None] OU ['cachoeirinha']
        
        resultados = Asban.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    except Exception as e:
        print(f"Erro {e}")
        
    try:
        consignet = ConsigNetController(driver)    
        
        convenios = [None] #[None] ou ['balneario', 'campo_largo', 'maringa_prev', 'navegantes', 'navegantes_prev']
        
        resultados = consignet.executar_todos_convenios(convenios)
                
        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    
    except Exception as e:
        print(f"Erro {e}")
    
    try:
        consiglog = ConsigLogController(driver)
        
        convenios = ['amazonas'] #[None] ou ['amazonas', 'duque_de_caxias']
        
        resultados = consiglog.executar_todos_convenios(convenios)

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