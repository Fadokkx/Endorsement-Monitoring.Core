from src.processadoras.consignet.convenios.balneario import ConvenioBalneario
from src.processadoras.consignet.convenios.CampoLargo import ConvenioCampoLargo
#from src.processadoras.consignet.convenios.MaringaPrev import ConvenioMaringaPrev
#from src.processadoras.consignet.convenios.NavegantesPrev import ConvenioNavegantesPrev
#from src.processadoras.consignet.convenios.navegantes import ConvenioNavegantes
from src.core.file_manager import renomear_e_mover_arquivos as file_manager
from selenium.webdriver.remote.webdriver import WebDriver
from src.core.date_var import variaveis_data as data
from src.core.paths import caminhos as paths
from typing import Dict, Type

class ConsigNetController():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.convenios: Dict[str, Type] = {
            'balneario': ConvenioBalneario,
            'campo_largo': ConvenioCampoLargo
            #'maringa_prev': ConvenioMaringaPrev,
            #'navegantes': ConvenioNavegantes,
            #'navegantes_prev': ConvenioNavegantesPrev
        }
    def executar_fluxo_completo(self, nome_convenio: str) -> bool:
        #Executa todo o fluxo para um convênio específico com tratamento detalhado de erros
        
        if nome_convenio not in self.convenios:
            raise ValueError(f"Convênio {nome_convenio} não existe")
        
        convenio = self.convenios[nome_convenio](self.driver)
        
        try:
            if not convenio.login():
                raise Exception("Falha no login") 
            
            if not convenio.selec_convenios():
                raise Exception("Falha na Seleção de convenio")
            
            if not convenio.navega_menu():
                raise Exception("Falha na navegação de menu")
            
            if not convenio.baixa_relatorio():
                raise Exception("Falha no download de relatórios")
            try:
                file_manager(pasta_origem=paths.pasta_download, pasta_destino=rf"C:\Relatórios\{data.DATA_PASTA}", parametro_nome= "RelConsignacaoMensal_", novo_nome=(f"consignet_{nome_convenio}_{data.DATA_ARQUIVO}"))
            except:
                print(f"Erro: {e}")

        except Exception as e:
            print(f"Erro: {e}")
            #raise Exception(f"[{nome_convenio.upper()}] {str(e)}") from e
    
    def executar_todos_convenios(self, convenios_selecionados: list = None):
        """Executa vários convênios em sequência"""
        resultados = {}
        convenios = convenios_selecionados or self.convenios.keys()
        
        for nome in convenios:
            try:
                sucesso = self.executar_fluxo_completo(nome)
                resultados[nome] = {
                    'status': 'Sucesso' if sucesso else 'Falha',
                    'erro': None
                }
            except Exception as e:
                resultados[nome] = {
                    'status': 'Erro crítico',
                    'erro': str(e)
                }
        return resultados