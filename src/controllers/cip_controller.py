#from src.processadoras.cip.convenios.govsp import ConvenioGovSP
from src.processadoras.cip.convenios.govmt import ConvenioGovMT
#from src.processadoras.cip.convenios.sefazsp import ConvenioSefazSP
from src.core.file_manager import renomear_e_mover_arquivos as file_manager
from src.core.date_var import variaveis_data as data
from src.core.paths import caminhos as paths
from typing import Dict, Type
from selenium.webdriver.remote.webdriver import WebDriver

class CipController:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.convenios: Dict[str, Type] = {
            #'govsp': ConvenioGovSP,
            #'govsefazsp': ConvenioSefazSP,
            'govmt': ConvenioGovMT
        }

    def executar_fluxo_completo(self, nome_convenio: str) -> bool:
        #Executa todo o fluxo para um convênio específico com tratamento detalhado de erros
        if nome_convenio not in self.convenios:
            raise ValueError(f"Convênio {nome_convenio} não existe")
        
        convenio = self.convenios[nome_convenio](self.driver)
        try:
            if not convenio.login():
                raise Exception("Falha no login")
            
            if not convenio.selec_perfil():
                raise Exception("Falha na seleção de perfil")
            
            if not convenio.navegar_menu():
                    raise Exception("Falha na navegação do menu")
            
            if not convenio.Tipos_Relatorio():
                raise Exception("Falha na seleção de tipos de relatório")
            
            if not convenio.Opcoes_Relatorios():
                raise Exception("Falha na seleção de opções de relatórios")
            
            if not convenio.download_arquivo():
                raise Exception("Falha no download do arquivo")
            
            
        except Exception as e:
            raise Exception(f"[{nome_convenio.upper()}] {str(e)}") from e

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