from src.core.browser import iniciar_navegador
from src.controllers.asban_controller import AsbanController
from src.controllers.cip_controller import CipController
from src.controllers.consigfacil_controller import ConsigFacilController
from src.controllers.consiglog_controller import ConsigLogController
from src.controllers.consignet_controller import ConsigNetController
from src.controllers.consigtec_controller import ConsigTecController
from src.controllers.digitalconsig_controller import DigitalConsigController
from src.controllers.infoconsig_controller import InfoConsigController
from src.controllers.neoconsig_controller import NeoConsigController
from src.controllers.proconsig_controller import ProConsigController
from src.controllers.quantumweb_controller import QuantumWebController
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
        
        convenios = [None] #[None] Ou ['pref_rio', 'nova_lima','curitiba','sobral','embu', 'hortolandia', 'hospital_do_servidor_publico', 'igeprev', 'maua', 'sbc', 'serra','uberlandia']
        
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

        convenios = ['joao_pessoa'] #[None] #OU #['campina_grande', 'cuiaba', 'ipatinga', 'joao_pessoa', 'juazeiro', 'maranhao', 'pernambuco', 'piaui', 'porto_velho', 'recife', 'teresina']        
        
        resultados = consigfacil.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}")
        
    try:
        Asban = AsbanController(driver)

        convenios = [None] #[None] OU ['cachoeirinha', 'varzea_grande']
        
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
        
        convenios = [None] #[None] ou ['iprev_santo_andre', 'amazonas', 'duque_de_caxias']
        
        resultados = consiglog.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    
    except Exception as e:
        print(f"Erro {e}")
        
    try:
        consigtec = ConsigTecController(driver)
        
        convenios = [None] #[None] ou ['maringa', 'porto_nacional']
        
        resultados = consigtec.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    
    except Exception as e:
        print(f"Erro {e}")
    
    try:
        digitalconsig = DigitalConsigController(driver)
        
        convenios = [None] #[None] ou ['sorriso']
        
        resultados = digitalconsig.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    
    except Exception as e:
        print(f"Erro {e}")
        
    try:
        safeconsig = SafeConsigController(driver)
        
        convenios = ['ceara', 'cabo_frio'] #[None] ou ['ceara', 'cabo_frio']
        
        resultados = safeconsig.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    
    except Exception as e:
        print(f"Erro {e}")
        
    try:
        serpro = SerproController(driver)
        
        convenios = [None] #[None] ou ['guarulhos']
        
        resultados = serpro.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    
    except Exception as e:
        print(f"Erro {e}")
        
    try:
        siconsig = SiConsigController(driver)
        
        convenios = [None] #[None] ou ['tocantins']
        
        resultados = siconsig.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    
    except Exception as e:
        print(f"Erro {e}")
        
    try:
        sigconsig = SigConsigController(driver)
        
        convenios = [None] #[None] ou ['santa_catarina']
        
        resultados = sigconsig.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")
    
    except Exception as e:
        print(f"Erro {e}")
        
    try:
        quantum = QuantumWebController(driver)
        
        convenios = [None] #[None] Ou ['ribeirao']
        
        resultados = quantum.executar_todos_convenios(convenios)

        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}") 
        
    try:
        infoconsig = InfoConsigController(driver)
        
        convenios = [None] #None ou ['barra_mansa', 'florianopolis']
        
        resultados = infoconsig.executar_todos_convenios(convenios)
        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}")

    try:
        proconsig = ProConsigController(driver)
        
        convenios = [None] #None ou ['porto_alegre']
        
        resultados = proconsig.executar_todos_convenios(convenios)
        print("\n=== RESUMO DE EXECUÇÃO ===")
        for convenio, dados in resultados.items():
            print(f"{convenio.upper():<15} {dados['status']}")
            if dados['erro']:
                print(f"   → {dados['erro']}")           
    except Exception as e:
        print(f"\n ERRO GLOBAL: {str(e)}")
        
    try:
        NeoConsig = NeoConsigController(driver)

        convenios = ['goias', 'rio', 'sorocaba', 'alagoas'] #[None] OU ['goias', 'rio', 'sorocaba', 'alagoas']
        
        resultados = NeoConsig.executar_todos_convenios(convenios)

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