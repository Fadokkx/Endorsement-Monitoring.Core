from src.processadoras.siconsig.convenios.tocantins import ConvenioTocantins
from src.core.file_manager import data_management as DM
from src.core.date_var import variaveis_data as data
from src.core.paths import caminhos as paths
from typing import Dict, Type
from selenium.webdriver.remote.webdriver import WebDriver

class SiConsigController():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.convenios: Dict[str, Type] = {
        'tocantins': ConvenioTocantins
        }
    
    def executar_fluxo_completo(self, nome_convenio: str) -> bool:
        if nome_convenio not in self.convenios:
            raise ValueError(f"Convênio {nome_convenio} não existe")
        
        convenio = self.convenios[nome_convenio](self.driver)
        try:
            if not convenio.login():
                raise Exception("Falha no login")
            
            if not convenio.navega_menu():
                raise Exception("Falha na navegação de menu")
            
            if not convenio.opcoes_relatorio():
                raise Exception("Falha na seleção de opção de relatório")
            
            if not convenio.download_relatorio():
                raise Exception("Falha ao baixar relatório")
            
            try:
                DM.renomear_e_mover_arquivos(pasta_origem=paths.pasta_download, pasta_destino=rf"C:\Relatórios\{data.DATA_PASTA}", parametro_nome= "CUSTOMIZAVELDEAVERBACAO", novo_nome=(f"siconsig_{nome_convenio}_{data.DATA_ARQUIVO}"))
            except Exception as e:
                print(f"{e}")
            
            return True
                
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