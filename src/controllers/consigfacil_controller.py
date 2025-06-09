from src.processadoras.consigfacil.convenios.campina_grande.campina_grande import ConvenioCampinaGrande
from src.processadoras.consigfacil.convenios.cuiaba.cuiaba import ConvenioCuiaba
from src.processadoras.consigfacil.convenios.ipatinga.ipatinga import ConvenioIpatinga
from src.processadoras.consigfacil.convenios.joao_pessoa.joao_pessoa import ConvenioJoaoPessoa
from src.processadoras.consigfacil.convenios.juazeiro.juazeiro_do_norte import ConvenioJuazeiro
from src.processadoras.consigfacil.convenios.maranhao.maranhao import ConvenioMaranhao
from src.processadoras.consigfacil.convenios.pernambuco.pernambuco import ConvenioPernambuco
from src.processadoras.consigfacil.convenios.piaui.piaui import ConvenioPiaui
from src.processadoras.consigfacil.convenios.porto_velho.porto_velho import ConvenioPortoVelho
from src.processadoras.consigfacil.convenios.recife.recife import ConvenioRecife
from src.processadoras.consigfacil.convenios.teresina.teresina import ConvenioTeresina
from src.core.file_manager import data_management as DM
from src.core.aws_config import Paths as Paths_S3
from src.core.date_var import variaveis_data as data
from src.core.paths import caminhos as paths
from typing import Dict, Type
from selenium.webdriver.remote.webdriver import WebDriver
import os
import time

class ConsigFacilController():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.convenios: Dict[str, Type] = {
            'campina_grande': ConvenioCampinaGrande,
            'cuiaba': ConvenioCuiaba,
            'ipatinga': ConvenioIpatinga,
            'joao_pessoa': ConvenioJoaoPessoa,
            'juazeiro': ConvenioJuazeiro,
            'maranhao': ConvenioMaranhao,
            'pernambuco': ConvenioPernambuco,
            'piaui': ConvenioPiaui,
            'porto_velho': ConvenioPortoVelho,
            'recife': ConvenioRecife,
            'teresina': ConvenioTeresina
        }
    
    def executar_fluxo_completo(self, nome_convenio: str) -> bool:
        if nome_convenio not in self.convenios:
            raise ValueError(f"Convênio {nome_convenio} não existe")
        
        convenio = self.convenios[nome_convenio](self.driver)
        try:
            if not convenio.login():
                raise Exception("Falha no login")
            
            try:
                if not convenio.troca_senha():
                    raise Exception("Falha na troca de senha")
            except:
                print("Sem necessidade de troca de senha")

            if not convenio.confirmacao_leitura_novidades():
                raise Exception ("Falha na Confirmação de leitura.") 
            
            if not convenio.navega_menu():
                raise Exception ("Falha na navegação do menu")
            
            if not convenio.opcoes_relatorio():
                raise Exception ("Falha ao selecionar as opções de relatório")
            
            if not convenio.baixar_relatorio():
                raise Exception ("Falha ao baixar relatório")
            
            try:
                DM.remove_arquivo_consigfacil()
                time.sleep(0.1)
                
                arquivo_local = DM.renomear_e_mover_arquivos(
                    pasta_origem=paths.pasta_download,
                    pasta_destino = paths.pasta_download,
                    parametro_nome= "relatorio",
                    novo_nome=(f"consigfacil_{nome_convenio}_{data.DATA_ARQUIVO}"))
                
                s3_key = f"{Paths_S3.Diretorio}/{data.DATA_PASTA}/{os.path.basename(arquivo_local)}"
                DM.upload_s3(arquivo_local, s3_key)
        
                DM.renomear_e_mover_arquivos(
                    pasta_origem=paths.pasta_download,
                    pasta_destino=rf"C:\Relatórios\BackupsS3\{data.DATA_PASTA}",
                    parametro_nome= "consigfacil_",
                    novo_nome=(f"consigfacil_{nome_convenio}_{data.DATA_ARQUIVO}_Uploaded_S3"))    
            
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