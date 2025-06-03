from src.processadoras.neoconsig.convenios.rio_de_janeiro import ConvenioRio
from src.processadoras.neoconsig.convenios.alagoas import ConvenioAlagoas
from src.processadoras.neoconsig.convenios.sorocaba import ConvenioSorocaba
from src.processadoras.neoconsig.convenios.goias import ConvenioGoias
from src.core.file_manager import data_management as DM
from src.core.aws_config import Paths as Paths_S3
from src.core.date_var import variaveis_data as data
from src.core.paths import caminhos as paths
from typing import Dict, Type
from selenium.webdriver.remote.webdriver import WebDriver
import os

class NeoConsigController:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.convenios: Dict[str, Type] = {
            'rio': ConvenioRio,
            'goias': ConvenioGoias,
            'alagoas': ConvenioAlagoas,
            'sorocaba': ConvenioSorocaba
        }

    def executar_fluxo_completo(self, nome_convenio: str) -> bool:
        #Executa todo o fluxo para um convênio específico com tratamento detalhado de erros
        if nome_convenio not in self.convenios:
            raise ValueError(f"Convênio {nome_convenio} não existe")
        
        convenio = self.convenios[nome_convenio](self.driver)
        try:
            if not convenio.login():
                raise Exception("Falha no login")
            
            if not convenio.acesso_senha():
                raise Exception("Falha no acesso via senha")
            
            if not convenio.navega_menu():
                raise Exception ("Falha na navegação no menu")
            
            if not convenio.opcoes_relatorio():
                raise Exception ("Falha na seleção de opções de relatório")
            
            if not convenio.download_relatorio():
                raise Exception ("Falha no download do relatório")
            
            try:
                arquivo_local = DM.renomear_e_mover_arquivos(
                    pasta_origem=paths.pasta_download, 
                    pasta_destino=paths.pasta_download, 
                    parametro_nome= "operacaoEmprestimo", 
                    novo_nome=(f"neoconsig_{nome_convenio}_{data.DATA_ARQUIVO}"))
                
                #DM.alteracao_neoconsig()
                        
                s3_key = f"{Paths_S3.Diretorio}/{data.DATA_PASTA}/{os.path.basename(arquivo_local)}"
                DM.upload_s3(arquivo_local, s3_key)
                
                DM.renomear_e_mover_arquivos(
                    pasta_origem=paths.pasta_download, 
                    pasta_destino=rf"C:\Relatórios\BackupsS3\{data.DATA_PASTA}",
                    parametro_nome= "neoconsig_", 
                    novo_nome=(f"neoconsig_{nome_convenio}_{data.DATA_ARQUIVO}_uploadedS3"))
                    
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