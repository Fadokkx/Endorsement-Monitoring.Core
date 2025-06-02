from src.processadoras.cip.convenios.govsp import ConvenioGovSP
from src.processadoras.cip.convenios.govmt import ConvenioGovMT
from src.processadoras.cip.convenios.sefazsp import ConvenioSefazSP
from src.core.file_manager import renomear_e_mover_arquivos as file_manager, upload_s3
from src.core.date_var import variaveis_data as data
from src.core.aws_config import Paths as Paths_S3
from src.core.paths import caminhos as paths
from typing import Dict, Type
from selenium.webdriver.remote.webdriver import WebDriver
import os

class CipController:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.convenios: Dict[str, Type] = {
            'govsp': ConvenioGovSP,
            'govsefazsp': ConvenioSefazSP,
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
            
            try:
                arquivo_local = file_manager(
                    pasta_origem=paths.pasta_download,
                    pasta_destino = paths.pasta_download,
                    parametro_nome= "RA015",
                    novo_nome=(f"cip_{nome_convenio}_{data.DATA_ARQUIVO}"))
                
                s3_key = f"{Paths_S3.Diretorio}/{data.DATA_PASTA}/{os.path.basename(arquivo_local)}"
                upload_s3(arquivo_local, s3_key)
        
                file_manager(
                    pasta_origem=paths.pasta_download,
                    pasta_destino=rf"C:\Relatórios\BackupsS3\{data.DATA_PASTA}",
                    parametro_nome= "cip_",
                    novo_nome=(f"cip_{nome_convenio}_{data.DATA_ARQUIVO}_Uploaded_S3"))
            
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